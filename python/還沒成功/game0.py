import keyboard, os
from time import sleep


class Button:
    def __init__(self, x: int, y: int, text: str, chinese: bool, do = None):
        self.x = x
        self.y = y
        self.text = text
        self.chinese = chinese
        if chinese:
            self.w = len(text)*2
        else:
            self.w = len(text)
        self.do = do


class Surface:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
        self.b = []
        self.c = 0
        self.f = False
        self.refresh()

    def refresh(self):
        self.s = []
        for y in range(self.h):
            a = []
            for x in range(self.w):
                if x == 0 or x == self.w - 1 or y == 0 or y == self.h - 1:
                    a.append("=")
                else:
                    a.append(" ")
            self.s.append(a)

    def update(self, b: Button):
        if b.chinese:
            for i in range(0, b.w, 2):
                if b.x + i < self.w:
                    self.s[b.y][b.x + i] = b.text[int(i / 2)]
                    self.s[b.y][b.x + i + 1] = ""
        else:
            for i in range(0, b.w):
                if b.x + i < self.w:
                    self.s[b.y][b.x + i] = b.text[i]
        if b == self.b[self.c]:
            self.s[b.y][b.x - 1] += "\033[7m"
            if b.x + b.w - 1 < self.w:
                self.s[b.y][b.x + b.w - 1] += "\033[0m"

    def display(self):
        self.refresh()
        for i in self.b:
            self.update(i)
        os.system("cls")
        for y in range(self.h):
            for x in range(self.w):
                if self.s[y][x] == " " and self.f:
                    print(str(x)[-1], end="")
                else:
                    print(self.s[y][x], end="")
            print()
        sleep(0.1)


def move(key: str, s: Surface):
    if key == "w":
        condition = "i.y < o.y"
    elif key == "a":
        condition = "i.x < o.x"
    elif key == "s":
        condition = "i.y > o.y"
    elif key == "d":
        condition = "i.x > o.x"
    d = 100
    o = s.b[s.c]
    en = s.c
    for n in range(len(s.b)):
        i = s.b[n]
        if i == o:
            continue
        elif eval(condition):
            nd = ((i.x - o.x) ** 2 + (i.y - o.y) ** 2) ** 0.5
            if nd < d:
                d = nd
                en = n
    return en

W, H = 120 ,30
surface = Surface(W, H)
surface.b.append(Button(round(W/3)-4, round(H/3), "開新遊戲", True))
surface.b.append(Button(round(W/3)-4, round(H/3*2)-1, "讀取存檔", True))
surface.b.append(Button(round(W/3*2)-4, round(H/3), "儲存遊戲", True))
surface.b.append(Button(round(W/3*2)-4, round(H/3*2)-1, "離開遊戲", True, exit))
surface.display()
while True:
    key = keyboard.read_key()
    if key == "w" or key == "a" or key == "s" or key == "d":
        surface.c = move(key, surface)
        surface.display()
    elif key == "enter":
        do = surface.b[surface.c].do
        if type(do) == str:
            eval(do)
        else:
            do()
    elif key == "f":
        if surface.f:
            surface.f = False
        else:
            surface.f = True
        surface.display()
