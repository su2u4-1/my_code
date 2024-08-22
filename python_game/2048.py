from os import system
from random import randrange, choices
from sys import stdin, stdout
from time import sleep
from typing import Callable

from keyboard import read_key

# from textgame import Game


# class Game2048(Game):
class Game2048:
    def __init__(self, r: int) -> None:
        self.init(r)

    def init(self, r: int) -> None:
        self.D = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.R = r
        self.m = [[0 for _ in range(r)] for _ in range(r)]
        self.add()

    def check(self) -> int:
        for i in self.m:
            if 0 in i:
                return 0
        for i in range(self.R):
            for j in range(self.R):
                for k in range(4):
                    if 0 <= i + self.D[k][0] < self.R and 0 <= j + self.D[k][1] < self.R:
                        if self.m[i][j] == self.m[i + self.D[k][0]][j + self.D[k][1]]:
                            return 1
        return 2

    def add(self) -> None:
        while True:
            x, y = randrange(self.R), randrange(self.R)
            if self.m[x][y] == 0:
                self.m[x][y] = choices((2, 4), (4, 1))[0]
                return

    def show(self) -> None:
        system("cls")
        str_m = [[str(j) for j in i] for i in self.m]
        long = 1
        for i in str_m:
            for j in range(self.R):
                long = max(long, len(i[j]))
        for i in self.m:
            for j in range(self.R):
                if i[j] == 0:
                    print(f"|{" "*long}|", end="")
                else:
                    print(f"|{i[j]:{long}}|", end="")
            print()

    def move(self, range1: range, range2: range, d: int) -> int:
        for i in range1:
            for j in range2:
                if self.m[i][j] == 0:
                    continue
                now_i, now_j = i, j
                while True:
                    if self.m[now_i + self.D[d][0]][now_j + self.D[d][1]] == 0:
                        self.m[now_i + self.D[d][0]][now_j + self.D[d][1]] = self.m[now_i][now_j]
                        self.m[now_i][now_j] = 0
                    elif self.m[now_i][now_j] == self.m[now_i + self.D[d][0]][now_j + self.D[d][1]]:
                        self.m[now_i][now_j] = 0
                        self.m[now_i + self.D[d][0]][now_j + self.D[d][1]] *= 2
                        break
                    now_i, now_j = now_i + self.D[d][0], now_j + self.D[d][1]
                    if now_i + self.D[d][0] < 0 or now_i + self.D[d][0] >= self.R or now_j + self.D[d][1] < 0 or now_j + self.D[d][1] >= self.R:
                        break
        return self.check()

    def main(self) -> None:
        d = ""
        t = 0
        while True:
            if d == "w" or d == "up":
                t = self.move(range(1, self.R), range(self.R), 0)
            elif d == "a" or d == "left":
                t = self.move(range(self.R), range(1, self.R), 1)
            elif d == "s" or d == "down":
                t = self.move(range(self.R - 2, -1, -1), range(self.R), 2)
            elif d == "d" or d == "right":
                t = self.move(range(self.R), range(self.R - 2, -1, -1), 3)
            if t == 2:
                print("game over")
                break
            elif t == 0:
                self.add()
            self.show()
            sleep(0.2)
            d = read_key()
        self.again()

    def again(self) -> None:
        stdin.flush()
        stdout.flush()
        o = input("again?[y/n]: ")
        if o in ("Y", "y", "Yes", "yes"):
            o = input("change size?[y/n]: ")
            if o in ("Y", "y", "Yes", "yes"):
                s = get_int("size: ", lambda x: x > 1)
            else:
                s = self.R
            self.init(s)
            self.main()


def get_int(text: str, condition: Callable[[int], bool]):
    while True:
        s = input(text)
        try:
            s = int(s)
            if condition(s):
                return s
            else:
                print("input error")
        except:
            print("input error")


if __name__ == "__main__":
    game = Game2048(get_int("size: ", lambda x: x > 1))
    game.main()
