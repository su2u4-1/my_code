import sys, time, random


def output(path):
    file1 = open(path + "(e).txt", "w+")
    for i in evolution:
        file1.write(i)
        file1.write("\n")
    file1.close()
    file2 = open(path + "(n).txt", "w+")
    for i in life_list:
        file2.write(f"{i.id}\n{i.quantity},{i.age},{i.att},{i.de},{i.agi},({i.x},{i.y})")
        file2.write("\n")
    file2.close()


def ri(a, b):
    random.seed()
    return random.randint(a, b)


def ra(a=None):
    random.seed(a)
    return random.random()


def generatemap(xl=270, yl=150):
    map = []
    for x in range(xl):
        a = []
        for y in range(yl):
            a.append(ra(x + y) * 15)
        map.append(a)
    return map


class summonlife:
    def __init__(self, id, x, y, quantity=1):
        self.quantity = quantity
        self.id = id
        self.x = x
        self.y = y
        self.age = 1
        j = 0
        self.de = 0
        for i in range(0, len(self.id), 2):
            j += int(f"{self.id[i]}{self.id[i+1]}")
            self.de += ra(int(f"{self.id[i]}{self.id[i+1]}"))
        k1, k2 = 0, 0
        for i in range(0, len(self.id), 2):
            k1 += int(self.id[i])
            k2 += int(self.id[i + 1])
        self.att = ra(j)
        self.agi = ra(k1 + k2)
        self.nu = ra(int(self.id))
        id_list.append(self.id)
        # print(f"{self.id},{self.att},{self.de},{self.agi},({self.x},{self.y})")

    def next(self):
        self.age += 1
        if self.age >= self.nu * 100:
            life_list.remove(self)
            del self
            return
        b1 = [1, 0, -1, 0]
        b2 = [0, 1, 0, -1]
        if map[self.x][self.y] >= 10:
            self.quantity += self.nu * ri(1, 10)
        elif map[self.x][self.y] < 5:
            self.quantity -= self.nu * ra()
            while True:
                c = map[self.x][self.y]
                cx = self.x
                cy = self.y
                for i in range(4):
                    if (
                        map[self.x + b1[i]][self.y + b2[i]] > c
                        and self.x + b1[i] < xl
                        and self.x + b1[i] > 0
                        and self.y + b2[i] < yl
                        and self.y + b2[i] > 0
                    ):
                        c = map[self.x + b1[i]][self.y + b2[i]]
                        cx = self.x + b1[i]
                        cy = self.y + b2[i]
                    if c != map[self.x][self.y]:
                        self.x = cx
                        self.y = cy
                        break
                if c == map[self.x][self.y]:
                    i = ri(0, 3)
                    if self.x + b1[i] < xl and self.x + b1[i] > 0 and self.y + b2[i] < yl and self.y + b2[i] > 0:
                        self.x += b1[i]
                        self.y += b2[i]
                        break
        else:
            while True:
                c = map[self.x][self.y]
                cx = self.x
                cy = self.y
                for i in range(4):
                    if (
                        map[self.x + b1[i]][self.y + b2[i]] > c
                        and self.x + b1[i] < xl
                        and self.x + b1[i] > 0
                        and self.y + b2[i] < yl
                        and self.y + b2[i] > 0
                    ):
                        c = map[self.x + b1[i]][self.y + b2[i]]
                        cx = self.x + b1[i]
                        cy = self.y + b2[i]
                    if c != map[self.x][self.y]:
                        self.x = cx
                        self.y = cy
                        break
                    elif c == map[self.x][self.y]:
                        break
                if c == map[self.x][self.y]:
                    break
        while self.quantity >= 5:
            self.quantity -= 3
            k = 0
            while True:
                k += 1
                if ri(1, 100) <= 5:
                    newid = self.id + f"{ri(0,9)}{ri(0,9)}"
                    evolution.append(f"{tmr}:{self.id}->{newid}")
                    life_list.append(summonlife(newid, self.x, self.y, 3))
                else:
                    life_list.append(summonlife(self.id, self.x, self.y, 3))
                if k >= 4:
                    break

    def meet(self, i):
        if self.att > i.de and self.agi > i.agi and self.id != i.id:
            self.quantity += i.quantity / 2
            try:
                life_list.remove(i)
            except:
                pass
        elif self.de < i.att and self.agi < i.agi and self.id != i.id:
            i.quantity += self.quantity / 2
            try:
                life_list.remove(self)
            except:
                pass
        else:
            z = (self.quantity + i.quantity) / 2
            self.quantity = z
            i.quantity = z


tmr = 0
a, b = 0, 0
xl, yl = 100, 100
map = generatemap(xl, yl)
id_list = []
life_list = []
evolution = []
life_list.append(summonlife("00", ri(25, 75), ri(25, 75), 10))
t = time.time()
while True:
    if tmr == 1000:
        nt = time.localtime(time.time())
        output(f"C:\\Users\\User\\Desktop\\程式\\data\\{nt.tm_year}-{nt.tm_mon}-{nt.tm_mday}-{nt.tm_hour}-{nt.tm_min}-{nt.tm_sec}")
        sys.exit()
    for i in life_list:
        i.next()
        if i.quantity <= 0:
            life_list.remove(i)
    for i in life_list:
        for j in life_list:
            if i.x == j.x and i.y == j.y:
                i.meet(j)
    tmr += 1
    print(f"{tmr}\t{len(life_list)}\t{round(time.time()-t,3)}")
    t = time.time()
