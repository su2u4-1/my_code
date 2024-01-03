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
    if len(i) == 3:
        a.append(f"{i[0]} {i[1:]}")
    elif len(i) == 2:
        a.append(f"{i[0]} {i[1]}")
    elif len(i) == 4:
        a.append(f"{i[0:2]} {i[2:]}")
with open("python\\data\\1.txt", "w+") as f:
    f.write(str(a))
