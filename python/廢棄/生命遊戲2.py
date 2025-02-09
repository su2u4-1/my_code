from typing import Optional
import time, random


def ri(a: int, b: int) -> int:
    random.seed()
    return random.randrange(a, b + 1)


def ra(a: Optional[int] = None) -> float:
    random.seed(a)
    return random.random()


def id(c1: int, c2: int) -> str:
    b = ""
    for _ in range(c1):
        for _ in range(c2):
            a = ri(0, 15)
            if a == 10:
                a = "A"
            elif a == 11:
                a = "B"
            elif a == 12:
                a = "C"
            elif a == 13:
                a = "D"
            elif a == 14:
                a = "E"
            elif a == 15:
                a = "F"
            else:
                a = str(a)
            b += a
        b += "-"
    return b[:-1]


def output():
    nt = time.localtime(time.time())
    path = f"C:\\Users\\User\\Desktop\\my_code\\data\\{nt.tm_year}-{nt.tm_mon}-{nt.tm_mday}-{nt.tm_hour}-{nt.tm_min}-{nt.tm_sec}"
    file = open(path + "(lca).txt", "w+")
    for i in lifel:
        file.write(str(i.__dict__))
        file.write("\n")
    file.close
    file = open(path + "(etl).txt", "w+")
    for i in list(ancl.items()):
        file.write(f"{i[1]}->{i[0]}\n")
    file.close
    file = open(path + "(etd).txt", "w+")
    file.write(str(ancl))
    file.close
    file = open(path + "(dl).txt", "w+")
    for i in die:
        file.write(str(i.__dict__))
        file.write("\n")
    file.close


class summonlife:
    def __init__(self, dna: str, anc: str, en: int, x: int, y: int):
        self.id = id(4, 4)
        idl.append(self.id)
        self.dna = dna
        dnal[self.id] = self.dna
        self.anc = anc
        ancl[self.id] = self.anc
        self.born = year
        self.die = None
        self.en = en
        self.age = 0
        self.xy = [x, y]
        self.att = int(dna.split("-")[0])
        self.de = int(dna.split("-")[1])
        self.agi = int(dna.split("-")[2])
        self.time = ra(int(dna.split("-")[3])) * 100
        self.repsp = ra(int(dna.split("-")[4]))
        self.gen = ra(int(dna.split("-")[5]))
        lifel.append(self)

    def next(self):
        self.age += 1
        a = 0
        for i in range(6):
            for j in range(10):
                a += int(self.dna.split("-")[i][j])
        if map[self.xy[0]][self.xy[1]] >= a / 81:
            self.en += a / 81
            map[self.xy[0]][self.xy[1]] -= a // 81
        else:
            self.en += map[self.xy[0]][self.xy[1]]
            map[self.xy[0]][self.xy[1]] = 0
            self.move
        if self.en >= ra() * 5 and int(self.dna[-1]) < 8:
            self.rep()
        self.examine

    def meet(self, k: "summonlife"):
        self.examine
        if self.dna == k.dna:
            self.rep()
        elif self.att > k.de * (ra() + 1) and self.agi > k.agi * (ra() + 1):
            self.eat(k)
        self.examine

    def eat(self, k: "summonlife"):
        if ri(1, 100) < (self.att / (self.att + k.de)) * 100:
            self.en += k.en * ra()
            k.en -= k.en * ra() * self.gen * 10

    def rep(self):
        if self.repsp > ra():
            self.en -= self.en / 3
            dna = self.dna
            d0 = dna.split("-")
            for _ in range(random.choices([0, 1, 2, 3, 4, 5], [5, 1, 1, 1, 1, 1])[0]):
                d1 = ri(0, 5)
                d2 = ri(0, 9)
                d = int(d0[d1][d2])
                if d <= 0:
                    d += ri(0, 1)
                elif d >= 9:
                    d -= ri(0, 1)
                else:
                    d += ri(-1, 1)
                d0[d1] = d0[d1][:d2] + str(d) + d0[d1][d2 + 1 :]
            summonlife(dna, self.id, int(self.en / 5), self.xy[0], self.xy[1])

    def examine(self):
        if self.age > self.time or self.en <= 0:
            self.die = year
            lifel.remove(self)
            die.append(self)
            del self

    def move(self):
        b = [[0, 1, 0, -1], [1, 0, -1, 0]]
        b1 = ri(0, 3)
        if self.xy[0] + b[0][b1] <= 99 and self.xy[0] + b[0][b1] >= 0 and self.xy[1] + b[1][b1] <= 99 and self.xy[1] + b[1][b1] >= 0:
            self.en -= ra() * self.gen * 10
            self.xy[0] += b[0][b1]
            self.xy[1] += b[1][b1]
        else:
            self.move()


idl: list[str] = []
dnal = {}
ancl: dict[str, str] = {}
die: list[summonlife] = []
map: list[list[int]] = []
for i in range(100):
    a: list[int] = []
    for j in range(100):
        a.append(ri(0, 100))
    map.append(a)
d = ""
for i in range(60):
    d += str(ri(0, 9))
    if (i + 1) % 10 == 0 and i != 59:
        d += "-"
year = 0
lifel: list[summonlife] = []
lifel.append(summonlife(d, "", ri(1, 10), ri(0, 99), ri(0, 99)))

while year <= 10000:
    print(year, len(lifel))
    year += 1
    for i in lifel:
        i.next()
    for i in lifel:
        for j in lifel:
            if i.xy == j.xy:
                i.meet(j)
    for i in range(100):
        for j in range(100):
            map[i][j] += int(ra())
output()
