from typing import Callable

"""
from time import sleep

from keyboard import read_key

class Game:
    def __init__(self, ...) -> None:
        self.init(...)

    def init(self, ...) -> None:
        ...

    def show(self) -> None:
        ...

    def check(self) -> ...:
        ...

    def main(self) -> None:
        d = ""
        while True:
            if d == "...":
                ...
            elif d == "...":
                ...
            ...
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
                ...
            else:
                ...
            self.init(...)
            self.main()
"""


def get_int(text: str, error_text: str, condition: Callable[[int], bool]):
    while True:
        s = input(text)
        try:
            s = int(s)
            if condition(s):
                return s
            else:
                print("input error:", error_text)
        except:
            print("input error: must be an integer")
