import keyboard, os


class Button:
    def __init__(self, x: int, y: int, text: str, chinese: bool):
        self.x = x
        self.y = y
        self.text = f"[ {text} ]"
        self.chinese = chinese
        if chinese:
            self.w = len(self.text) + len(text)
        else:
            self.w = len(self.text)


class Surface:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
        self.s = []
        for y in range(h):
            a = []
            for x in range(w):
                if x == 0 or x == w - 1 or y == 0 or y == h - 1:
                    a.append("=")
                else:
                    a.append(" ")
            self.s.append(a)
        self.b = []
        self.c = 0

    def update(self, b: Button):
        if b.chinese:
            self.s[b.y][b.x] = "["
            if b.x + b.w - 1 < self.w:
                self.s[b.y][b.x + b.w] = "]"
            for i in range(2, b.w - 1, 2):
                if b.x + i < self.w:
                    self.s[b.y][b.x + i] = b.text[int(i / 2) + 1]
                    self.s[b.y][b.x + i + 1] = ""
        else:
            for i in range(0, b.w):
                if b.x + i < self.w:
                    self.s[b.y][b.x + i] = b.text[i]
        if b == self.b[self.c]:
            self.s[b.y][b.x] = "{"
            if b.x + b.w - 1 < self.w:
                if b.chinese:
                    self.s[b.y][b.x + b.w] = "}"
                else:
                    self.s[b.y][b.x + b.w - 1] = "}"

    def display(self):
        for i in self.b:
            self.update(i)
        os.system("cls")
        for y in range(self.h):
            for x in range(self.w):
                print(self.s[y][x], end="")
            print()


def move(key: str, s: Surface):
    if key == "w":  # up
        d = 100
        o = s.b[s.c]
        for n in range(len(s.b)):
            i = s.b[n]
            if i == o:
                continue
            elif i.y < o.y:
                nd = ((i.x - o.x) ** 2 + (i.y - o.y) ** 2) ** 0.5
                if nd < d:
                    d = nd
        return n
    elif key == "s":  # down
        d = 100
        o = s.b[s.c]
        for n in range(len(s.b)):
            i = s.b[n]
            if i == o:
                continue
            elif i.y > o.y:
                nd = ((i.x - o.x) ** 2 + (i.y - o.y) ** 2) ** 0.5
                if nd < d:
                    d = nd
        return n
    elif key == "a":  # left
        d = 100
        o = s.b[s.c]
        for n in range(len(s.b)):
            i = s.b[n]
            if i == o:
                continue
            elif i.x < o.x:
                nd = ((i.x - o.x) ** 2 + (i.y - o.y) ** 2) ** 0.5
                if nd < d:
                    d = nd
        return n
    elif key == "d":  # right
        d = 100
        o = s.b[s.c]
        for n in range(len(s.b)):
            i = s.b[n]
            if i == o:
                continue
            elif i.x > o.x:
                nd = ((i.x - o.x) ** 2 + (i.y - o.y) ** 2) ** 0.5
                if nd < d:
                    d = nd
        return n
    return s.c


surface = Surface(120, 30)
surface.b.append(Button(5, 5, "按鈕", True))
surface.b.append(Button(5, 10, "button", False))
surface.b.append(Button(15, 5, "按鈕", True))
surface.b.append(Button(15, 10, "button", False))
surface.display()
while True:
    surface.c = move(keyboard.read_key(), surface)
    surface.display()
