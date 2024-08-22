from os import system
from random import randrange
from time import sleep

from keyboard import read_key

from textgame import get_int

DX = (0, 1, 0, -1)
DY = (1, 0, -1, 0)
CHANGE = {(0, 0): 4, (0, 1): 2, (0, 2): 1, (0, 3): 8, (1, 0): 1, (1, 1): 8, (1, 2): 4, (1, 3): 2}


class Game_maze:
    def __init__(self, w: int, h: int, start_point: tuple[int, int], end_point: tuple[int, int], symbol: tuple[str, str, str, str, str] = (" ", "▓", "S", "E", "P")):
        self.init(w, h, start_point, end_point, symbol)

    def init(self, w: int, h: int, start_point: tuple[int, int], end_point: tuple[int, int], symbol: tuple[str, str, str, str, str]):
        self.w = w
        self.h = h
        self.sp = start_point
        self.ep = end_point
        self.symbol = symbol
        self.pl = list(start_point)
        self.m = [[self.symbol[1] for _ in range(self.w * 2 + 1)] for _ in range(self.h * 2 + 1)]
        self.maze = [[0 for _ in range(w)] for _ in range(h)]
        self.build()
        self.update()

    def build(self) -> None:
        a: list[tuple[int, int]] = [self.sp]
        b: list[tuple[int, int, int, int, int, int]] = []
        for i in range(4):
            if 0 <= a[0][0] + DY[i] < self.h and 0 <= a[0][1] + DX[i] < self.w:
                b.append((a[0][0], a[0][1], DY[i], DX[i], CHANGE[(0, i)], CHANGE[(1, i)]))
        while True:
            if len(b) > 0:
                s = b.pop(randrange(len(b)))
                if (s[0] + s[2], s[1] + s[3]) not in a:
                    self.maze[s[0]][s[1]] += s[4]
                    self.maze[s[0] + s[2]][s[1] + s[3]] += s[5]
                    a.append((s[0] + s[2], s[1] + s[3]))
                    for i in range(4):
                        if 0 <= a[-1][0] + DY[i] < self.h and 0 <= a[-1][1] + DX[i] < self.w:
                            b.append((a[-1][0], a[-1][1], DY[i], DX[i], CHANGE[(0, i)], CHANGE[(1, i)]))
            else:
                break

    def update(self) -> None:
        self.m = [[self.symbol[1] for _ in range(self.w * 2 + 1)] for _ in range(self.h * 2 + 1)]
        for i in range(self.h):
            for j in range(self.w):
                t = self.maze[i][j]
                self.m[i * 2 + 1][j * 2 + 1] = self.symbol[0]
                if t >= 8:
                    t -= 8
                    self.m[i * 2 + 1][j * 2] = self.symbol[0]
                if t >= 4:
                    t -= 4
                if t >= 2:
                    t -= 2
                if t >= 1:
                    self.m[i * 2][j * 2 + 1] = self.symbol[0]
        self.m[self.sp[0] * 2 + 1][self.sp[1] * 2 + 1] = self.symbol[2]
        self.m[self.ep[0] * 2 + 1][self.ep[1] * 2 + 1] = self.symbol[3]
        self.m[self.pl[0] * 2 + 1][self.pl[1] * 2 + 1] = self.symbol[4]

    def show(self) -> None:
        self.update()
        system("cls")
        print("\n".join("".join(i) for i in self.m))

    def check(self) -> bool:
        return self.pl[0] == self.ep[0] and self.pl[1] == self.ep[1]

    def main(self) -> None:
        d = ""
        while True:
            if d == "w" or d == "up":
                if self.m[self.pl[0] * 2][self.pl[1] * 2 + 1] == self.symbol[0]:
                    self.pl[0] -= 1
            elif d == "a" or d == "left":
                if self.m[self.pl[0] * 2 + 1][self.pl[1] * 2] == self.symbol[0]:
                    self.pl[1] -= 1
            elif d == "s" or d == "down":
                if self.m[self.pl[0] * 2 + 2][self.pl[1] * 2 + 1] == self.symbol[0]:
                    self.pl[0] += 1
            elif d == "d" or d == "right":
                if self.m[self.pl[0] * 2 + 1][self.pl[1] * 2 + 2] == self.symbol[0]:
                    self.pl[1] += 1
            self.show()
            if self.check():
                print("gameover")
                break
            sleep(0.2)
            d = read_key()
        self.again()

    def again(self) -> None:
        o = input("again?[y/n]: ")
        if o in ("Y", "y", "Yes", "yes"):
            o = input("change size?[y/n]: ")
            if o in ("Y", "y", "Yes", "yes"):
                w = get_int("w: ", lambda x: x > 0)
                h = get_int("h: ", lambda x: x > 0)
            else:
                w, h = self.w, self.h
            self.init(w, h, (0, 0), (w - 1, h - 1), self.symbol)
            self.main()


if __name__ == "__main__":
    w = get_int("w: ", lambda x: x > 0)
    h = get_int("h: ", lambda x: x > 0)
    maze = Game_maze(w, h, (0, 0), (w - 1, h - 1), ("  ", "▓▓", "SP", "EP", "PL"))
    maze.main()
