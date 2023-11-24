from bs4 import BeautifulSoup
from urllib.request import urlopen  # 用於獲取網頁

file = open("url.txt", "r", encoding="UTF-8")
url = file.readlines()
file.close
print(1)
file = open("imgurl.txt", "w+", encoding="UTF-8")
for i in url:
    print(2)
    html = urlopen(i.replace("\n", ""))
    bsObj = BeautifulSoup(html, "html.parser")
    t1 = bsObj.find_all("img")
    for t2 in t1:
        try:
            t3 = t2.get("data-src")
            if ".png/original" in t3:
                file.write(t3 + "\n")
                print(t3)
        except:
            pass
file.close
