from os import system
from random import randint

from textgame import get_int


class Game_guess_number:
    def __init__(self, a: int, b: int) -> None:
        self.init(a, b)

    def init(self, a: int, b: int) -> None:
        self.ans = randint(a, b)
        self.a = a
        self.b = b

    def main(self) -> None:
        while True:
            a = get_int("guess a number: ", "must be within range", lambda x: self.a <= x <= self.b)
            if a > self.ans:
                print("too big")
            elif a < self.ans:
                print("too small")
            else:
                print("you win")
                print("game over")
                break
        self.again()

    def again(self) -> None:
        o = input("again?[y/n]: ")
        if o in ("Y", "y", "Yes", "yes"):
            o = input("change size?[y/n]: ")
            if o in ("Y", "y", "Yes", "yes"):
                a = get_int("lower limit: ", "must be greater than or equal to 0", lambda x: x >= 0)
                b = get_int("upper limit: ", "must be greater than or equal to the lower limit", lambda x: x >= a)
            else:
                a, b = self.a, self.b
            system("cls")
            self.init(a, b)
            self.main()


a = get_int("lower limit: ", "must be greater than or equal to 0", lambda x: x >= 0)
b = get_int("upper limit: ", "must be greater than or equal to the lower limit", lambda x: x >= a)
game = Game_guess_number(a, b)
game.main()
