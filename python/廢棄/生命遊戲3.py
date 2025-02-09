import pygame, sys, math, time, random


def output(path: str):
    file1 = open(path + "(e).txt", "w+")
    for i in evolution1:
        file1.write(i)
        file1.write("\n")
    file1.close()
    file2 = open(path + "(n).txt", "w+")
    for i in life_list:
        file2.write(f"{i.id}\n{i.color},{i.quantity},({i.x},{i.y})")
        file2.write("\n")
    file2.close()
    file3 = open(path + "(a).txt", "w+")
    for i in ancestor:
        file3.write(f"{i.id}\n{i.color},{i.quantity},({i.x},{i.y})")
        file3.write("\n")
    file3.close()


def ri(a: int, b: int):
    random.seed()
    return random.randint(a, b)


def generatemap(xl: int = 270, yl: int = 150):
    map: list[list[int]] = []
    for _ in range(xl):
        a: list[int] = []
        for _ in range(yl):
            a.append(ri(12, 15))
        map.append(a)
    return map


class summonlife:
    def __init__(self, color: tuple[int, int, int], id: str, x: int, y: int, quantity: int = 1):
        self.color = color
        self.quantity = quantity
        self.id = id
        self.x = x
        self.y = y
        self.year = 0
        random.seed(int(self.id))
        self.nu = random.random()
        id_list.append(id)

    def next(self):
        self.year += 1
        self.nu -= 0.01
        if self.nu <= 0:
            life_list.remove(self)
            del self
            return
        b1 = [1, 0, -1, 0]
        b2 = [0, 1, 0, -1]
        if map[self.x][self.y] >= self.nu * 2:
            map[self.x][self.y] -= int(self.nu * 2)
        if map[self.x][self.y] >= 10:
            self.quantity += self.nu
        elif map[self.x][self.y] < 5:
            self.quantity -= self.nu * 2
            while True:
                i = ri(0, 3)
                if self.x + b1[i] < xl and self.x + b1[i] > 0 and self.y + b2[i] < yl and self.y + b2[i] > 0:
                    self.x += b1[i]
                    self.y += b2[i]
                    break
        else:
            if ri(1, 100) <= 20:
                while True:
                    i = ri(0, 3)
                    if self.x + b1[i] < xl and self.x + b1[i] > 0 and self.y + b2[i] < yl and self.y + b2[i] > 0:
                        self.x += b1[i]
                        self.y += b2[i]
                        break
        while self.quantity >= 5:
            self.quantity -= 3
            k = 0
            while True:
                k += 1
                if ri(1, 100) <= 1:
                    c = [ri(0, 255), ri(0, 255), ri(0, 255)]
                    for j in range(3):
                        if self.color[j] > 235:
                            c[j] = ri(self.color[j] - 20, self.color[j])
                        elif self.color[j] < 20:
                            c[j] = ri(self.color[j], self.color[j] + 20)
                        elif self.color[j] <= 235 and self.color[j] >= 20:
                            c[j] = ri(self.color[j] - 20, self.color[j] + 20)
                    colorchange = (c[0], c[1], c[2])
                    newid = self.id + f"{ri(0,9)}{ri(0,9)}"
                    evolution[newid] = self.id
                    evolution1.append(f"{tmr}:{self.id}->{newid}")
                    print(f"{tmr}:{self.id}->{newid}")
                    life_list.append(summonlife(colorchange, newid, self.x, self.y, 3))
                else:
                    life_list.append(summonlife(self.color, self.id, self.x, self.y, 3))
                if k >= 4:
                    break

    def meet(self, enemy: "summonlife"):
        if self.id != enemy.id:
            if self.nu > enemy.nu:
                self.quantity += enemy.quantity / 2
                enemy.quantity = 0
            elif self.nu < enemy.nu:
                enemy.quantity += self.quantity / 2
                self.quantity = 0
            else:
                self.quantity -= enemy.nu
                enemy.quantity -= self.nu


tmr = 0
a, b = 0, 0
xl, yl = 270, 150
pygame.init()
pygame.display.set_caption("生命遊戲")
screen = pygame.display.set_mode((1350, 750), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)
map = generatemap(xl, yl)
id_list: list[str] = []
life_list: list[summonlife] = []
evolution = {"00": "None"}
evolution1: list[str] = []
ancestor: list[summonlife] = []
text = ""
f = 0
idl = 1
mx, my = 134, 74
zero = summonlife((255, 0, 0), "00", 134, 74, 10)
life_list.append(zero)
ancestor.append(zero)
while True:
    if f % 2 == 0:
        tmr += 1
    """if len(evolution)%100 == 0:
        if f%2 == 0:
            f = 1"""
    if tmr == 10000:
        pygame.quit()
        nt = time.localtime(time.time())
        output(f"C:\\Users\\User\\Desktop\\my_code\\data\\{nt.tm_year}-{nt.tm_mon}-{nt.tm_mday}-{nt.tm_hour}-{nt.tm_min}-{nt.tm_sec}")
        sys.exit()
    mx, my = pygame.mouse.get_pos()
    mx = math.floor(mx / 5)
    my = math.floor(my / 5)
    text = f"map:{map[mx][my]}  time:{tmr}  x,y:({mx},{my})"
    for i in life_list:
        if i.x == mx and i.y == my:
            text += f"color:{i.color}  quantity:{i.quantity}  nu:{i.nu}  onu:{i.nu+(i.year/100)}  year:{i.year}  id:{i.id}  "
            try:
                text += f"evolution:{evolution[i.id]}  "
            except:
                pass
            break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            nt = time.localtime(time.time())
            output(f"C:\\Users\\User\\Desktop\\my_code\\data\\{nt.tm_year}-{nt.tm_mon}-{nt.tm_mday}-{nt.tm_hour}-{nt.tm_min}-{nt.tm_sec}")
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                f += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if idl < 10:
                    z = summonlife((ri(0, 255), ri(0, 255), ri(0, 255)), f"0{idl}", mx, my, 10)
                    life_list.append(z)
                    ancestor.append(z)
                elif idl >= 10:
                    z = summonlife((ri(0, 255), ri(0, 255), ri(0, 255)), f"{idl}", mx, my, 10)
                    life_list.append(z)
                    ancestor.append(z)
                idl += 1
    screen.fill((0, 0, 0))
    for x in range(xl):
        for y in range(yl):
            c = (map[x][y] * -16) + 255
            pygame.draw.rect(screen, (c, c, c), pygame.Rect(x * 5, y * 5, 5, 5), width=0)
            if x == mx and y == my:
                pygame.draw.rect(
                    screen,
                    (255, 0, 0),
                    pygame.Rect(mx * 5 + 1, my * 5 + 1, 3, 3),
                    width=0,
                )
    for i in life_list:
        pygame.draw.rect(
            screen,
            i.color,
            pygame.Rect(i.x * 5, i.y * 5, 5, 5),
            width=round(i.quantity),
        )
        if f % 2 == 0:
            i.next()
            if i.quantity <= 0:
                life_list.remove(i)
    for i in life_list:
        for j in life_list:
            if i.x == j.x and i.y == j.y:
                i.meet(j)
                try:
                    if i.quantity <= 0:
                        life_list.remove(i)
                    if j.quantity <= 0:
                        life_list.remove(j)
                except:
                    pass
    if f % 2 == 0:
        for x in range(xl):
            for y in range(yl):
                if map[x][y] <= 14.8:
                    random.seed()
                    map[x][y] += int(random.random() / 5)
    txt = font.render(text, True, (255, 255, 255))
    screen.blit(txt, [0, 0])
    pygame.display.update()
    clock.tick(10)
