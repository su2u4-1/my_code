from random import randint

from Game import clear_screen, get_int


class Game_guess_number:
    def __init__(self, a: int, b: int) -> None:
        self.init(a, b)

    def init(self, a: int, b: int) -> None:
        self.ans = randint(a, b)
        self.a = a
        self.b = b
        self.n = 0

    def main(self) -> None:
        while True:
            a = get_int("guess a number: ", "must be within range", lambda x: self.a <= x <= self.b)
            self.n += 1
            if a > self.ans:
                print("\033[31mtoo big\033[0m")
            elif a < self.ans:
                print("\033[34mtoo small\033[0m")
            else:
                print("\033[32myou win\033[0m")
                print("game over")
                print("round:", self.n)
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
            clear_screen()
            self.init(a, b)
            self.main()


if __name__ == "__main__":
    a = get_int("lower limit: ", "must be greater than or equal to 0", lambda x: x >= 0)
    b = get_int("upper limit: ", "must be greater than or equal to the lower limit", lambda x: x >= a)
    game = Game_guess_number(a, b)
    game.main()
