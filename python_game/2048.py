from random import randrange, choices
from time import sleep

from keyboard import read_key

from Game import get_int, clear_screen, D4


class Game_2048:
    def __init__(self, r: int) -> None:
        self.init(r)

    def init(self, r: int) -> None:
        self.R = r
        self.m = [[0 for _ in range(r)] for _ in range(r)]
        self.add()
        self.add()

    def check(self) -> int:
        for i in range(self.R):
            for j in range(self.R):
                for k in range(4):
                    if 0 <= i + D4[k][0] < self.R and 0 <= j + D4[k][1] < self.R:
                        if self.m[i][j] == self.m[i + D4[k][0]][j + D4[k][1]]:
                            return True
        return False

    def add(self) -> None:
        while True:
            x, y = randrange(self.R), randrange(self.R)
            if self.m[x][y] == 0:
                self.m[x][y] = choices((2, 4), (4, 1))[0]
                return

    def show(self) -> None:
        clear_screen()
        str_m = [[str(j) for j in i] for i in self.m]
        long = max(max(len(j) for j in i) for i in str_m)
        for i in self.m:
            for j in range(self.R):
                if i[j] == 0:
                    print(f"|{" "*long}|", end="")
                else:
                    print(f"|{i[j]:{long}}|", end="")
            print()

    def move(self, range1: range, range2: range, d: int) -> int:
        f = False
        for i in range1:
            for j in range2:
                if self.m[i][j] == 0:
                    continue
                now_i, now_j = i, j
                while True:
                    if self.m[now_i + D4[d][0]][now_j + D4[d][1]] == 0:
                        self.m[now_i + D4[d][0]][now_j + D4[d][1]] = self.m[now_i][now_j]
                        self.m[now_i][now_j] = 0
                        f = True
                    elif self.m[now_i][now_j] == self.m[now_i + D4[d][0]][now_j + D4[d][1]]:
                        self.m[now_i][now_j] = 0
                        self.m[now_i + D4[d][0]][now_j + D4[d][1]] *= 2
                        f = True
                        break
                    else:
                        break
                    now_i, now_j = now_i + D4[d][0], now_j + D4[d][1]
                    if now_i + D4[d][0] < 0 or now_i + D4[d][0] >= self.R or now_j + D4[d][1] < 0 or now_j + D4[d][1] >= self.R:
                        break
        if f:
            return 0
        elif self.check():
            return 1
        else:
            return 2

    def main(self) -> None:
        d = ""
        while True:
            if d == "w" or d == "up":
                t = self.move(range(1, self.R), range(self.R), 3)
            elif d == "a" or d == "left":
                t = self.move(range(self.R), range(1, self.R), 2)
            elif d == "s" or d == "down":
                t = self.move(range(self.R - 2, -1, -1), range(self.R), 1)
            elif d == "d" or d == "right":
                t = self.move(range(self.R), range(self.R - 2, -1, -1), 0)
            else:
                t = 1
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
        o = input("again?[y/n]: ")
        if o in ("Y", "y", "Yes", "yes"):
            o = input("change size?[y/n]: ")
            if o in ("Y", "y", "Yes", "yes"):
                s = get_int("size: ", "must be great than 1", lambda x: x > 1)
            else:
                s = self.R
            self.init(s)
            self.main()


if __name__ == "__main__":
    game = Game_2048(get_int("size: ", "must be great than 1", lambda x: x > 1))
    game.main()
