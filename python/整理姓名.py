from typing import TypeVar, Protocol

v = TypeVar("v")


class SupportsIAdd(Protocol):
    def __iadd__(self, other: v) -> v: ...


V = TypeVar("V", bound=SupportsIAdd)


class mydict(dict[str, V]):
    def __init__(self, d: dict[str, V]):
        super().__init__(d)

    def add(self, i: str, n: V):
        if i in self:
            self[i] += n
        else:
            self[i] = n


link = "python\\data\\"
with open(link + "name.txt", "r", encoding="utf-8") as f:
    text = f.read()
text = str(text)
text = text.split(", ")
with open(link + "surname.txt", "r", encoding="utf-8") as f:
    sn = eval(f.read())
a: list[tuple[str, str]] = []
for i in text:
    if len(i) == 4:
        a.append((i[0:2], i[2:]))
    elif len(i) == 3:
        if i[0:2] not in sn:
            a.append((i[0], i[1:]))
        else:
            print(i)
    elif len(i) == 2:
        a.append((i[0], i[1:]))

with open(link + "surname.txt", "r", encoding="utf-8") as f:
    surname = mydict(eval(f.read()))
with open(link + "name1.txt", "r", encoding="utf-8") as f:
    name1 = mydict(eval(f.read()))
with open(link + "name2.txt", "r", encoding="utf-8") as f:
    name2 = mydict(eval(f.read()))
with open(link + "name1_2.txt", "r", encoding="utf-8") as f:
    name1_2 = mydict(eval(f.read()))
for i in name1_2.keys():
    name1_2[i] = mydict(name1_2[i])

for i in a:
    surname.add(i[0], 1)
    if len(i[1]) == 2:
        name2.add(i[1][1], 1)
        name1.add(i[1][0], 1)
        if i[1][0] not in name1_2:
            name1_2[i[1][0]] = mydict({})
        name1_2[i[1][0]].add(i[1][1])
    elif len(i[1]) == 1:
        name1.add(i[1][0], 1)
        name2.add("None", 1)
        if i[1][0] not in name1_2:
            name1_2[i[1][0]] = mydict({})
        name1_2[i[1][0]].add("None")

with open(link + "surname.txt", "w+", encoding="utf-8") as f:
    f.write(str(surname))
with open(link + "name1.txt", "w+", encoding="utf-8") as f:
    f.write(str(name1))
with open(link + "name2.txt", "w+", encoding="utf-8") as f:
    f.write(str(name2))
with open(link + "name1_2.txt", "w+", encoding="utf-8") as f:
    f.write(str(name1_2))
