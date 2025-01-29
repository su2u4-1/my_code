import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

# html = requests.get("https://game8.jp/shoujokaisen/491720")
# soup = BeautifulSoup(html.text, "html.parser")
# image_url_list = soup.find_all("a", class_="a-link")
# for i in image_url_list:
#     if i["href"].startswith("https://game8.jp/shoujokaisen/"):
#         for j in BeautifulSoup(requests.get(i["href"]).text, "html.parser").find_all("img", class_="a-img lazy lazy-non-square"):
#             if j["data-src"].endswith(".jpeg/show") or j["data-src"].endswith(".png/show"):
#                 with open("網頁and爬蟲\\image_url.txt", "a+") as f:
#                     print(j["alt"])
#                     f.write(f'{j["alt"]}: {j["data-src"]}\n')


# with open("網頁and爬蟲\\.txt", "r") as f:
#     a = f.readlines()
# for i in a:
#     for j in BeautifulSoup(requests.get(i).text, "html.parser").find_all("img", class_="a-img lazy lazy-non-square"):
#         if j["data-src"].endswith(".jpeg/original") or j["data-src"].endswith(".png/original") and not j["alt"].endswith("のアイキャッチ"):
#             with open("網頁and爬蟲\\image_url.txt", "a+") as f:
#                 print(j["alt"])
#                 f.write(f'{j["alt"]}: {j["data-src"]}\n')


# with open("網頁and爬蟲\\image_url.txt", "r") as f:
#     a = f.readlines()
# for i in a:
#     i = i.split(": ")
#     i[1] = i[1].strip()
#     image = requests.get(i[1])
#     if i[0].endswith("（UR＋）"):
#         print("UR+", end=" ")
#         path = "C:\\Users\\joey2\\桌面\\蘇定澤\\香圖\\別人的\\少女迴戰\\UR+"
#     elif i[0].endswith("（UR）"):
#         print("UR", end=" ")
#         path = "C:\\Users\\joey2\\桌面\\蘇定澤\\香圖\\別人的\\少女迴戰\\UR"
#     elif i[0].endswith("（SSR）"):
#         print("SSR", end=" ")
#         path = "C:\\Users\\joey2\\桌面\\蘇定澤\\香圖\\別人的\\少女迴戰\\SSR"
#     elif i[0].endswith("（SR）") or i[0].endswith("（R）"):
#         print("SR_&_R", end=" ")
#         path = "C:\\Users\\joey2\\桌面\\蘇定澤\\香圖\\別人的\\少女迴戰\\SR & R"
#     if i[1].endswith(".png/original"):
#         with open(f'{path}\\{i[0]}.png', 'wb') as f:
#             print(i[0], ".png")
#             f.write(image.content)
#     elif i[1].endswith(".jpeg/original"):
#         with open(f'{path}\\{i[0]}.jpg', 'wb') as f:
#             print(i[0], ".jpg")
#             f.write(image.content)

# with open("網頁and爬蟲\\image_url.txt", "r") as f:
#     a = f.readlines()
# for i in a[365:]:
#     i = i.split(": ")
#     i[1] = i[1].strip()
#     image = requests.get(i[1])
#     path = "C:\\Users\\joey2\\桌面\\蘇定澤\\香圖\\別人的\\少女迴戰\\武靈體"
#     if i[1].endswith(".png/show"):
#         with open(f'{path}\\{i[0]}.png', 'wb') as f:
#             print(i[0], ".png")
#             f.write(image.content)
#     elif i[1].endswith(".jpeg/show"):
#         with open(f'{path}\\{i[0]}.jpg', 'wb') as f:
#             print(i[0], ".jpg")
#             f.write(image.content)
