from keyboard import read_key
from os import system
from time import sleep


class Button:
    def __init__(self, x: int, y: int, text: str, chinese: bool = True, do=None):
        self.x = x
        self.y = y
        if chinese:
            self.retext(text)
        else:
            self.text = text
            self.w = len(self.text)
        self.do = do

    def retext(self, text: str):
        ntext = ""
        for i in range(len(text)):
            if 19968 <= int(ord(text[i])) <= 40959:
                ntext += text[i] + "\u0000"
            else:
                ntext += text[i]
        self.text = ntext
        self.w = len(self.text)


class Surface:
    def __init__(self, w: int, h: int, name: str = "surface"):
        self.w = w
        self.h = h
        self.b = []
        self.c = 0
        self.f = False
        self.n = name
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
        for b in self.b:
            for i in range(0, b.w):
                if b.x + i < self.w:
                    self.s[b.y][b.x + i] = b.text[i]
            if b == self.b[self.c]:
                self.s[b.y][b.x - 1] += "\033[7m"
                if b.x + b.w - 1 < self.w:
                    self.s[b.y][b.x + b.w - 1] += "\033[0m"

    def update(self, readkey: bool = True):
        self.refresh()
        system("cls")
        for y in range(self.h):
            for x in range(self.w):
                if self.s[y][x] == " " and self.f:
                    print(str(x)[-1], end="")
                elif y == 0 and self.f and x < len(self.n):
                    print(self.n[x], end="")
                else:
                    print(self.s[y][x], end="")
            print()
        if readkey:
            sleep(0.3)
            return read_key(True)


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


def main():
    s = Surface(W, H, "main")
    s.b.append(Button(round(W / 2), round(H / 2), f"還沒做好", True, "print(name)\nexit()"))
    return s


def start():
    s = Surface(W, H, "start")
    s.b.append(Button(round(W / 3) - 4, round(H / 3), "開新遊戲", True, "system('cls')\nname=input('請輸入名字:')\nsurface=main()"))
    s.b.append(Button(round(W / 3) - 4, round(H / 3 * 2) - 1, "讀取存檔", True))
    s.b.append(Button(round(W / 3 * 2) - 4, round(H / 3), "儲存遊戲", True))
    s.b.append(Button(round(W / 3 * 2) - 4, round(H / 3 * 2) - 1, "離開遊戲", True, "exit()"))
    return s


W, H = 120, 30
name = "player"
surface = start()
key = surface.update()
while True:
    if key == "w" or key == "a" or key == "s" or key == "d":
        surface.c = move(key, surface)
        key = surface.update()
    elif key == "enter":
        do = surface.b[surface.c].do
        exec(do)
        key = surface.update()
    elif key == "f":
        if surface.f:
            surface.f = False
        else:
            surface.f = True
        key = surface.update()
