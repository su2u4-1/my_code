from random import randrange, choice
from time import sleep
from keyboard import is_pressed


class Virus:
    def __init__(self, id: int, parents: int, content: str) -> None:
        self.id = id
        self.parents = parents
        self.content = content
        if id not in virus_dict:
            virus_dict[id] = (content, parents)

    def reproduce(self) -> "Virus":
        global count
        if randrange(10) == 0:
            content = self.content
            for _ in range(randrange(1, 11)):
                n = randrange(100)
                content = content[:n] + choice("0123456789") + content[n + 1 :]
            v = Virus(count, self.id, content)
            count += 1
        else:
            v = Virus(self.id, self.parents, self.content)
        return v


class Computer:
    def __init__(self, id: int, virus: Virus, content: str = "") -> None:
        self.id = id
        if content == "":
            content = "".join(choice("0123456789") for _ in range(100))
        self.content = content
        self.virus = virus
        self.update()

    def update(self) -> None:
        self.tt = 0
        for i, j in zip(self.content, self.virus.content):
            self.tt += 1 if i <= j else -1

    def run(self) -> None:
        ct = choice(computers)
        t = 0
        for i, j in zip(ct.content, self.virus.content):
            t += 1 if i <= j else -1
        if show[0]:
            print(f"computer {self.id} [virus {self.virus.id}, {self.tt}] -> computer {ct.id} [virus {ct.virus.id}, {ct.tt}]", end=" ")
        if t >= ct.tt:
            ct.virus = self.virus.reproduce()
            ct.update()
            if show[0]:
                print("O")
        elif show[0]:
            print("X")


def save(cl: list[Computer], vd: dict[int, tuple[str, int]]) -> str:
    r: list[str] = []
    for i in cl:
        r.append(str({"id": i.id, "ct_c": i.content, "tt_c": i.tt, "id_v": i.virus.id, "ct_v": i.virus.content, "pt_v": i.virus.parents}))
    r.append("virus_dict:\n{")
    for k, v in vd.items():
        r.append(f"    {k}: {v},")
    r.append("}")
    return "\n".join(r)


# init
computers: list[Computer] = []
virus_dict: dict[int, tuple[str, int]] = {}
count = 0
s = 1
content = "".join(choice("0123456789") for _ in range(100))
print("original virus:", content)
virus = Virus(count, -1, content)
count += 1
show = [True, False]
for i in range(100):
    c = Computer(i, virus)
    computers.append(c)

# main loop
while True:
    if is_pressed("c"):
        c = input().split()
        while c[0].startswith("c"):
            c[0] = c[0][1:]
        if c[0] == "show":
            for i in computers:
                print(f"id: {i.id}, ct_c: {i.content}, tt_c: {i.tt}, id_v: {i.virus.id}, ct_v: {i.virus.content}, pt_v: {i.virus.parents}")
        elif c[0] == "save":
            if len(c) == 1:
                f = open("./virus.txt", "w+")
            else:
                f = open(c[1], "w+")
            f.write(save(computers, virus_dict))
            f.close()
        elif c[0] == "exit":
            break
        elif c[0] == "set":
            if c[1] == "show":
                show[0] = bool(c[2])
                show[1] = bool(c[3])
            elif c[1] == "fps":
                s = int(c[2])
        if input("continue?: ") in ("n", "no", "N", "No", "NO"):
            break

    for _ in range(randrange(50)):
        choice(computers).run()
    if show[1]:
        for i, c in enumerate(computers):
            print(f"{i}.({c.virus.id}, {c.tt})", end="\t")
    sleep(s)
    if len(virus_dict) >= 50:
        break

if input("save?: ") in ("y", "yes", "Y", "Yes", "YES"):
    with open("./virus.txt", "w+") as f:
        f.write(save(computers, virus_dict))
