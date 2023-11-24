from bs4 import BeautifulSoup
from urllib.request import urlopen  # 用於獲取網頁

html = urlopen("https://game8.jp/shoujokaisen/419407")
bsObj = BeautifulSoup(html, "html.parser")
t1 = bsObj.find_all("a")
file = open("url.txt", "w+", encoding="UTF-8")
for t2 in t1:
    if t2.get("class") == ["a-link"]:
        t3 = t2.get("href")
        if "https://game8.jp/shoujokaisen/" in t3:
            file.write(t3 + "\n")
file.close
