import asyncio, os, re, html
from playwright.async_api import async_playwright, Page, Route, BrowserContext


class EtymonlineWordScraper:
    def __init__(self, words: list[str], output_dir: str = "etymology_archive") -> None:
        self.words = words
        self.output_dir = output_dir
        self.base_url = "https://www.etymonline.com/tw/word/"

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

            if re.match(r"^[a-zA-Z-\s]+\([a-z./, \s0-9]+\)$", line):
                formatted_lines.append(f"### {line}")
                continue

            if re.match(r"^(also from|同樣來自) .+$", line, re.IGNORECASE):
                continue

            formatted_lines.append(line)

        return "\n".join(formatted_lines).strip()

    async def extract_word_page(self, page: Page, word: str) -> list[dict[str, str]]:
        url: str = f"{self.base_url}{word}"
        print(f"--- 正在處理單字: {word} ---")
        log.append(f"--- 正在處理單字: {word} ---")

        await page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # 檢測是否有內容標題，若無則視為 404
        content_header = page.locator("h1")
        if await content_header.count() == 0 or "Page Not Found" in await page.title():
            print(f"[{word}] 抓不到單字頁面，轉向搜尋...")
            log.append(f"[{word}] 抓不到單字頁面")

            # 使用標準搜尋 (不帶 /tw/)
            search_url: str = f"https://www.etymonline.com/search?q={word}"
            await page.goto(search_url, wait_until="domcontentloaded", timeout=60000)

            # 檢查是否有搜尋結果
            result_links = page.locator("a.w-full.group[href*='/word/']")
            if await result_links.count() == 0:
                print(f"[{word}] 搜尋結果：找不到任何相關單字")
                log.append(f"[{word}] 搜尋結果：找不到任何相關單字")
                return []

            # 取得第一個搜尋結果
            first_href = await result_links.first.get_attribute("href")
            if first_href:
                stem_word: str = first_href.split("/word/")[-1].split("?")[0].split("#")[0]
                print(f"[{word}] 搜尋結果：發現詞幹 [{stem_word}]")
                log.append(f"[{word}] 搜尋結果：發現詞幹 [{stem_word}]")

                if stem_word.lower() != word.lower() and stem_word not in self.words:
                    self.words.append(stem_word)
                    print(f"[{word}] 已將 [{stem_word}] 加入待執行列表")
                    log.append(f"[{word}] 已將 [{stem_word}] 加入待執行列表")
            return []

        # 正常抓取內容
        extracted_data: list[dict[str, str]] = await page.evaluate(
            """() => {
            const data = [];
            const headers = document.querySelectorAll('h2.scroll-m-16');
            
            headers.forEach(header => {
                let title = header.innerText.replace(/\\n/g, ' ').trim();
                let container = header.closest('div').nextElementSibling;
                
                while (container && container.tagName.toLowerCase() !== 'section') {
                    container = container.nextElementSibling;
                }
                
                if (!container) return;

                let result = "";
                function walk(node, isInsideQuote = false) {
                    if (node.nodeType === Node.TEXT_NODE) {
                        result += node.textContent;
                    } else if (node.nodeType === Node.ELEMENT_NODE) {
                        const tagName = node.tagName.toLowerCase();
                        if (tagName === 'button' || node.classList.contains('ad-space')) return;
                        if (tagName === 'a') {
                            let href = node.getAttribute('href') || '';
                            if (href.startsWith('/')) href = 'https://www.etymonline.com/tw' + href;
                            result += `[${node.innerText.trim()}](${href})`;
                            return; 
                        }
                        const isQuote = tagName === 'blockquote';
                        if (isQuote) result += '\\n[[BLOCKQUOTE_START]]';
                        node.childNodes.forEach(child => walk(child, isInsideQuote || isQuote));
                        if (isQuote) result += '[[BLOCKQUOTE_END]]\\n';
                        else if (['p', 'div', 'br', 'section'].includes(tagName)) result += '\\n';
                    }
                }
                walk(container);
                data.push({ title: title, content: result });
            });
            return data;
        }"""
        )

        def process_quotes(match: re.Match[str]) -> str:
            content: str = match.group(1).strip()
            quoted_lines: list[str] = [f"> {line}" if line.strip() else line for line in content.split("\n")]
            return "\n" + "\n".join(quoted_lines) + "\n"

        results: list[dict[str, str]] = []
        for item in extracted_data:
            clean_text: str = item["content"]
            clean_text = clean_text.replace("翻譯成: 繁體中文 (Traditional Chinese)", "").replace("顯示原文", "")
            clean_text = re.sub(r"\[\[BLOCKQUOTE_START\]\](.*?)\[\[BLOCKQUOTE_END\]\]", process_quotes, clean_text, flags=re.DOTALL)
            clean_text = re.sub(r"\n{3,}", "\n\n", clean_text).strip()
            results.append({"title": item["title"], "content": self.format_content(clean_text)})

        return results

    def save_to_markdown(self, word: str, data: list[dict[str, str]]) -> None:
        if not data:
            return
        file_path: str = os.path.join(self.output_dir, f"{word}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {word}\n\n")
            for item in data:
                f.write(f"## {item['title']}\n{item['content']}\n\n---\n")
        print(f"[{word}] 存檔完成: {file_path}")
        log.append(f"[{word}] 存檔完成")

    async def run(self) -> None:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context: BrowserContext = await browser.new_context(viewport={"width": 1280, "height": 1000})
            page: Page = await context.new_page()
            await self.block_ads(page)

            i: int = 0
            while i < len(self.words):
                word: str = self.words[i]
                try:
                    word_data: list[dict[str, str]] = await self.extract_word_page(page, word)
                    if word_data:
                        self.save_to_markdown(word, word_data)
                    else:
                        print(f"[{word}] 無內容可儲存")
                        log.append(f"[{word}] 無內容可儲存")
                except Exception as e:
                    print(f"[{word}] 異常: {e}")
                    log.append(f"[{word}] 異常: {e}")

                i += 1
                await asyncio.sleep(1)  # 避免過快導致請求被封鎖

            await browser.close()


def load_words_from_text(file_path: str, target_list: list[str]) -> None:
    if not os.path.exists(file_path):
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
        target_list = ["accessing", "cba", "rule"]
        scraper = EtymonlineWordScraper(target_list)
    else:
        target_list: list[str] = []
        base_path = "C:/Users/joey2/桌面/英文/"
        for f_name in ["words.txt", "affix.txt"]:
            load_words_from_text(os.path.join(base_path, f_name), target_list)
        scraper = EtymonlineWordScraper(target_list, os.path.join(base_path, "etymology_archive"))

    asyncio.run(scraper.run())

    with open("etymology_scraping_log.txt", "w", encoding="utf-8") as log_file:
        log_file.write("\n".join(log))
