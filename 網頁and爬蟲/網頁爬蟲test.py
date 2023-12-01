from random import randint
import requests
from bs4 import BeautifulSoup

a = "game_" + str(randint(0, 99999999))
url = "https://txtpad.cn/game_"
r = requests.get(url)  # 將此頁面的HTML GET下來
soup = BeautifulSoup(r.text, "html.parser")  # 將網頁資料以html.parser
print(r.text)
sel = soup.select("div.editor-box pre")  # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
for s in sel:
    print(s.text)
