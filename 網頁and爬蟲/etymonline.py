import asyncio
import os
import re
from playwright.async_api import async_playwright, Page, Route, BrowserContext, Locator


class EtymonlineWordScraper:
    def __init__(self, words: list[str], output_dir: str = "etymology_archive") -> None:
        self.words = words
        self.output_dir = output_dir
        self.base_url = "https://www.etymonline.com/word/"

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    async def block_ads(self, page: Page) -> None:
        ad_domains: list[str] = ["doubleclick", "adnxs", "amazon-adsystem", "googlesyndication", "analytics"]

        async def route_handler(route: Route) -> None:
            if any(domain in route.request.url for domain in ad_domains):
                await route.abort()
            else:
                await route.continue_()

        await page.route("**/*", route_handler)

    def is_chinese(self, text: str) -> bool:
        return bool(re.search(r"[\u4e00-\u9fa5]", text))

    def format_content(self, text: str) -> str:
        lines: list[str] = text.split("\n")
        formatted_lines: list[str] = []
        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append("")
                continue
            if re.match(r"^[a-zA-Z-\s]+\([a-z./\s]+\)$", line):
                formatted_lines.append(f"### {line}")
                continue
            if line.startswith("...") or (("[" in line and "]" in line) and len(line) > 50):
                formatted_lines.append(f"> {line}\n")
                continue
            if re.match(r"^also from .+$", line, re.IGNORECASE):
                continue
            formatted_lines.append(line)
        return "\n".join(formatted_lines).strip()

    async def extract_word_page(self, page: Page, word: str) -> list[dict[str, str]]:
        url: str = f"{self.base_url}{word}"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)

        btn_selector: str = 'button:has-text("翻译成: 简体中文 (Chinese)")'
        try:
            await page.wait_for_selector(btn_selector, timeout=10000)
        except:
            print(f"[{word}] 找不到翻譯按鈕")
            return []

        results: list[dict[str, str]] = []
        loop_counter: int = 0

        while True:
            btn: Locator = page.locator(btn_selector).first
            if await btn.count() == 0:
                break

            container_id: str = f"entry_{loop_counter}"
            await btn.evaluate(
                f"""(el, id) => {{
                let container = el.closest('section.prose-lg') 
                             || el.closest('section') 
                             || el.closest('div[class*="word--"]') 
                             || el.parentElement.parentElement;
                if(container) container.setAttribute('data-scraped-id', id);
            }}""",
                container_id,
            )

            # 記錄點擊前的原始文本內容，用來比對是否已變更（即翻譯完成）
            target_container: Locator = page.locator(f"[data-scraped-id='{container_id}']")
            original_text: str = await target_container.inner_text()

            await btn.scroll_into_view_if_needed()
            await btn.click()
            print(f"[{word}] 點擊第 {loop_counter+1} 條翻譯，等待翻譯完成...")

            # 核心修正：動態等待直到內容包含中文，或者內容發生變化
            try:
                # 使用 wait_for_function 監控容器內容
                # 設定 15 秒超時，防止翻譯腳本卡死導致程式永不停止
                await page.wait_for_function(
                    """([id, oldText]) => {
                        const el = document.querySelector(`[data-scraped-id="${id}"]`);
                        if (!el) return false;
                        const newText = el.innerText;
                        // 判定條件：內容改變且包含中文字符
                        return newText !== oldText && /[\\u4e00-\\u9fa5]/.test(newText);
                    }""",
                    arg=[container_id, original_text],
                    timeout=15000,
                )
            except Exception:
                print(f"[{word}] 第 {loop_counter+1} 條翻譯等待超時，直接嘗試抓取。")

            # 額外等待 1 秒，確保翻譯內容完全渲染
            await asyncio.sleep(1)

            # 抓取並處理
            raw_text: str = await target_container.inner_text()
            clean_text: str = raw_text.replace("翻译成: 简体中文 (Chinese)", "")
            clean_text = clean_text.replace("显示原文", "").strip()
            final_content: str = self.format_content(clean_text)

            title: str = f"Origin and history of {word}"
            if loop_counter > 0:
                title = f"{word} (related entry {loop_counter})"

            results.append({"title": title, "content": final_content})
            print(f"[{word}] 第 {loop_counter+1} 條提取成功")

            loop_counter += 1

        return results

    def save_to_markdown(self, word: str, data: list[dict[str, str]]) -> None:
        if not data:
            return
        file_path: str = os.path.join(self.output_dir, f"{word}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {word}\n\n")
            for item in data:
                f.write(f"## {item['title']}\n{item['content']}\n\n---\n")
        print(f"存檔完成: {file_path}")

    async def run(self) -> None:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context: BrowserContext = await browser.new_context(viewport={"width": 1280, "height": 1000})
            page: Page = await context.new_page()
            await self.block_ads(page)
            for word in self.words:
                try:
                    word_data: list[dict[str, str]] = await self.extract_word_page(page, word)
                    self.save_to_markdown(word, word_data)
                except Exception as e:
                    print(f"[{word}] 執行崩潰: {e}")
                await asyncio.sleep(2)
            await browser.close()


def load_words_from_text(file_path: str, target_list: list[str]) -> None:
    """
    載入格式為 '單字: 釋義' 的文本文件，並將單字加入 target_list。
    """
    if not os.path.exists(file_path):
        print(f"錯誤：找不到檔案 {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # 確保行內包含冒號且不是空行
            if ":" in line:
                # 分割單字與釋義，只取第一部分並去除空白
                word: str = line.split(":", 1)[0].strip()
                if word and word not in target_list:
                    target_list.append(word)


test = True

if __name__ == "__main__":
    if test:
        target_list = ["human", "April"]  # 測試用的單字列表
        scraper = EtymonlineWordScraper(target_list)
    else:
        target_list: list[str] = []
        load_words_from_text("C:/Users/joey2/桌面/英文/words.txt", target_list)
        print(f"已載入單字清單: {target_list}")
        scraper = EtymonlineWordScraper(target_list, "C:/Users/joey2/桌面/英文/etymology_archive")
    asyncio.run(scraper.run())
