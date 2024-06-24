from random import choices as ch


link = "python\\data\\"
with open(link + "surname.txt", "r", encoding="utf-8") as f:
    surname: dict[str, int] = eval(f.read())
with open(link + "name1.txt", "r", encoding="utf-8") as f:
    name1: dict[str, int] = eval(f.read())
with open(link + "name2.txt", "r", encoding="utf-8") as f:
    name2: dict[str, int] = eval(f.read())
with open(link + "name1_2.txt", "r", encoding="utf-8") as f:
    name1_2: dict[str, dict[str, int]] = eval(f.read())

snk = list(surname.keys())
snv = list(surname.values())
n1k = list(name1.keys())
n1v = list(name1.values())
n2k = list(name2.keys())
n2v = list(name2.values())
n = int(input("數量:"))
for _ in range(n):
    sn = ch(snk, snv)[0]
    n1 = ch(n1k, n1v)[0]
    if ch([True, False], [1, 1])[0]:
        n2 = ch(n2k, n2v)[0]
        if n2 == "None":
            n2 = ""
    else:
        n12k = list(name1_2[n1].keys())
        n12v = list(name1_2[n1].values())
        n2 = ch(n12k, n12v)[0]
        n2 += "(根據第一字)"
        if n2 == "None(根據第一字)":
            n2 = ""
    print(sn + n1 + n2)
