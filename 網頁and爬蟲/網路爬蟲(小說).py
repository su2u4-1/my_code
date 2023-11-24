import requests
from bs4 import BeautifulSoup

url_base = "//czbooks.net/n/uimgl8/u2eaj"
url = url_base
text = []
a = True
file = open("《我就是神！》全章節.txt", "w+")
file.write("《我就是神！》全章節")
while a:
    try:
        while True:
            response = requests.get("https:" + url)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                contents = soup.find_all("div", class_="name")
                for content in contents:
                    try:
                        file.write(f"{content.text}")
                    except UnicodeEncodeError:
                        pass
                    txt1 = f"{content.text}"
                contents = soup.find_all("div", class_="content")
                for content in contents:
                    try:
                        file.write(f"\n{content.text}")
                    except UnicodeEncodeError:
                        pass
                file.write("\n")
                print(txt1, "下載成功")
                next_button = soup.find("a", class_="next-chapter")
                if not next_button:
                    a = False
                    break
                c = soup.find_all("a", class_="next-chapter")
                for i in c:
                    url = i.get("href")
            else:
                print(f"Request failed with status code {response.status_code}")
                break
    except:
        print(txt1, "下載失敗")
file.close
