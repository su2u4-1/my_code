import requests
from bs4 import BeautifulSoup

with open("網頁and爬蟲\\.txt", "r") as f:
    a = f.readlines()
for i in a:
    for j in BeautifulSoup(requests.get(i).text, "html.parser").find_all("img", class_="a-img lazy lazy-non-square"):
        if j["data-src"].endswith(".jpeg/original") or j["data-src"].endswith(".png/original") and not j["alt"].endswith("のアイキャッチ"):
            with open("網頁and爬蟲\\image_url.txt", "a+") as f:
                print(j["alt"])
                f.write(f'{j["alt"]}: {j["data-src"]}\n')
