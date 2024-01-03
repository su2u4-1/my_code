text = input().split(",")
r = []
for i in range(len(text)):
    text[i] = text[i].replace(" ", "")
with open("python\\data\\處理完.txt", "w+") as f:
    f.write(str(text))

with open("python\\data\\處理完.txt", "r") as f:
    text = eval(f.read())
a = []
for i in text:
    if len(i) != 3:
        a.append(f"{i[0]} {i[1:]}")
with open("python\\data\\2.txt", "w+") as f:
    f.write(str(a))
