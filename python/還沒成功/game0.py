from keyboard import read_key
from os import system
from time import sleep


class Button:
    def __init__(self, x: int, y: int, text: str, chinese: bool = True, do=None):
        self.x = x
        self.y = y
        if chinese:
            ntext = ""
            for i in range(len(text)):
                if 19968 <= int(ord(text[i])) <= 40959:
                    ntext += text[i] + "\u200B"
                else:
                    ntext += text[i]
            self.text = ntext
        else:
            self.text = text
        self.w = len(self.text)
        self.do = do


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

    def update(self, b: Button):
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
        system("cls")
        for y in range(self.h):
            for x in range(self.w):
                if self.s[y][x] == " " and self.f:
                    print(str(x)[-1], end="")
                else:
                    print(self.s[y][x], end="")
            print()
        sleep(0.2)


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


def newgame():
    s = Surface(W, H, "name")
    s.b.append(Button(round(W / 2), round(H / 2), "確認", True, "surface=main()"))
    return s


def main():
    s = Surface(W, H, "main")
    s.b.append(Button(round(W / 2), round(H / 2), "還沒做好", True, exit))
    return s


W, H = 120, 30
name = "player"
surface = Surface(W, H, "start")
surface.b.append(Button(round(W / 3) - 4, round(H / 3), "開新遊戲", True, "surface=newgame()"))
surface.b.append(Button(round(W / 3) - 4, round(H / 3 * 2) - 1, "讀取存檔", True))
surface.b.append(Button(round(W / 3 * 2) - 4, round(H / 3), "儲存遊戲", True))
surface.b.append(Button(round(W / 3 * 2) - 4, round(H / 3 * 2) - 1, "離開遊戲", True, exit))
surface.display()
while True:
    key = read_key()
    if surface.n == "name":
        surface.display()
        if key == "enter":
            name = surface.b[0].text[4:]
        elif key == "backspace":
            surface.b[0].text = surface.b[0].text[:-1]
            surface.b[0].w -= 1
        else:
            surface.b[0].text += key
            surface.b[0].w += 1
    if key == "w" or key == "a" or key == "s" or key == "d":
        surface.c = move(key, surface)
        surface.display()
    elif key == "enter":
        do = surface.b[surface.c].do
        if type(do) == str:
            exec(do)
        else:
            do()
        surface.display()
    elif key == "f":
        if surface.f:
            surface.f = False
        else:
            surface.f = True
        surface.display()
