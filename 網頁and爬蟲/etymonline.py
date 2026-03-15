import asyncio
import os
import re
import html
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

    def format_content(self, text: str) -> str:
        text = html.unescape(text)

        # 1. 處理星號轉義，但避開連結格式
        # 先將連結暫時替換，轉義星號後再換回來
        links: list[str] = re.findall(r"\[.*?\]\(http.*?\)", text)
        for i, link in enumerate(links):
            text = text.replace(link, f"__LINK{i}__")

        text = text.replace("*", r"\*")

        for i, link in enumerate(links):
            text = text.replace(f"__LINK{i}__", link)

        lines: list[str] = text.split("\n")
        formatted_lines: list[str] = []

        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append("")
                continue

            # 2. 詞性標題
            if re.match(r"^[a-zA-Z-\s]+\([a-z./, \s0-9]+\)$", line):
                formatted_lines.append(f"### {line}")
                continue

            # 3. 移除贅餘行
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
            log.append(f"[{word}] 找不到翻譯按鈕")
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

            target_container: Locator = page.locator(f"[data-scraped-id='{container_id}']")
            original_text: str = await target_container.inner_text()

            await btn.scroll_into_view_if_needed()
            await btn.click()
            print(f"[{word}] 點擊第 {loop_counter+1} 條翻譯...")
            log.append(f"[{word}] 點擊第 {loop_counter+1} 條翻譯...")

            try:
                await page.wait_for_function(
                    """([id, oldText]) => {
                        const el = document.querySelector(`[data-scraped-id="${id}"]`);
                        if (!el) return false;
                        const newText = el.innerText;
                        return newText !== oldText && /[\\u4e00-\\u9fa5]/.test(newText);
                    }""",
                    arg=[container_id, original_text],
                    timeout=15000,
                )
            except Exception:
                pass

            await asyncio.sleep(1)

            # --- 強化 DOM 遍歷邏輯：解決嵌套標籤導致重複 > 的問題 ---
            processed_text: str = await page.evaluate(
                """(id) => {
                const container = document.querySelector(`[data-scraped-id="${id}"]`);
                if (!container) return "";

                let result = "";

                function walk(node, isInsideQuote = false) {
                    if (node.nodeType === Node.TEXT_NODE) {
                        result += node.textContent;
                    } else if (node.nodeType === Node.ELEMENT_NODE) {
                        const tagName = node.tagName.toLowerCase();
                        
                        // 移除無用 UI
                        if (tagName === 'button' || node.classList.contains('ad-space')) return;

                        // 處理超連結
                        if (tagName === 'a') {
                            let href = node.getAttribute('href') || '';
                            if (href.startsWith('/')) href = 'https://www.etymonline.com' + href;
                            if (href.includes('etymonline.com/word/')) {
                                result += `[${node.innerText.trim()}](${href})`;
                                return; 
                            }
                        }

                        // 如果是 blockquote，在內容開始前標註一個特殊符號，稍後在 Python 端處理
                        const isQuote = tagName === 'blockquote';
                        if (isQuote) {
                            result += '\\n[[BLOCKQUOTE_START]]';
                        }

                        node.childNodes.forEach(child => walk(child, isInsideQuote || isQuote));

                        if (isQuote) {
                            result += '[[BLOCKQUOTE_END]]\\n';
                        } else if (['p', 'div', 'br', 'section'].includes(tagName)) {
                            result += '\\n';
                        }
                    }
                }

                walk(container);
                return result;
            }""",
                container_id,
            )

            # 在 Python 端利用預留的標記進行格式化
            def process_quotes(match: re.Match[str]) -> str:
                content: str = match.group(1).strip()
                # 將內容的每一行前面都加上 >
                quoted_lines: list[str] = [f"> {line}" if line.strip() else line for line in content.split("\n")]
                return "\n" + "\n".join(quoted_lines) + "\n"

            # 替換特殊標記
            clean_text: str = processed_text.replace("翻译成: 简体中文 (Chinese)", "").replace("显示原文", "")

            # 使用正則表達式處理所有 [[BLOCKQUOTE_START]] ... [[BLOCKQUOTE_END]] 的內容
            clean_text = re.sub(r"\[\[BLOCKQUOTE_START\]\](.*?)\[\[BLOCKQUOTE_END\]\]", process_quotes, clean_text, flags=re.DOTALL)

            # 清理過多換行
            clean_text = re.sub(r"\n{3,}", "\n\n", clean_text).strip()

            final_content: str = self.format_content(clean_text)

            title: str = f"Origin and history of {word}"
            if loop_counter > 0:
                title = f"{word} (related entry {loop_counter})"

            results.append({"title": title, "content": final_content})
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
        log.append(f"存檔完成: {file_path}")

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
                    print(f"[{word}] 執行失敗: {e}")
                    log.append(f"[{word}] 執行失敗: {e}")
            await browser.close()


def load_words_from_text(file_path: str, target_list: list[str]) -> None:
    if not os.path.exists(file_path):
        print(f"錯誤：找不到檔案 {file_path}")
        log.append(f"錯誤：找不到檔案 {file_path}")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                word: str = line.split(":", 1)[0].strip()
                if word and word not in target_list:
                    target_list.append(word)


test = False
log: list[str] = []

if __name__ == "__main__":
    if test:
        target_list = ["April", "all", "cum", "logic"]
        scraper = EtymonlineWordScraper(target_list)
    else:
        target_list: list[str] = []
        load_words_from_text("C:/Users/joey2/桌面/英文/words.txt", target_list)
        load_words_from_text("C:/Users/joey2/桌面/英文/affix.txt", target_list)
        load_words_from_text("C:/Users/joey2/桌面/英文/word.txt", target_list)
        print(f"已載入單字清單: {target_list}")
        log.append(f"已載入單字清單: {target_list}")
        scraper = EtymonlineWordScraper(target_list, "C:/Users/joey2/桌面/英文/etymology_archive")
    asyncio.run(scraper.run())

with open("etymology_scraping_log.txt", "w", encoding="utf-8") as log_file:
    log_file.write("\n".join(log))
