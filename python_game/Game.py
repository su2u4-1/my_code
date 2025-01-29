from typing import Callable


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


D4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
D8 = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
