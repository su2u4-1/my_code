from typing import Callable, NoReturn


def get_int(text: str, error_text: str, condition: Callable[[int], bool]) -> int | NoReturn:
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


#       ↓       →       ↑         ←
D4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
#      ⇘       ⇒       ⇗       ⇓       ⇑        ⇙       ⇐        ⇖
D8 = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))

D8_Opposite_side = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0}


def t0(t: list[int], ai_side: int, player_side: int) -> int:
    """p p p p *\n
    direction x 8"""
    for i in range(8):
        for j in t[i * 4 : i * 4 + 3]:
            if j != player_side:
                return 0
    return 10


def t1(t: list[int], ai_side: int, player_side: int) -> int:
    """a a a a *\n
    direction x 8"""
    for i in range(8):
        for j in t[i * 4 : i * 4 + 4]:
            if j != ai_side:
                return 0
    return 11


def t2(t: list[int], ai_side: int, player_side: int) -> int:
    """p p p * p\n
    direction x 8"""
    for i in range(8):
        j = t[i * 4 : i * 4 + 4]
        if j[:3] == [player_side] * 3:
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][0] == player_side:
                return 10
    return 0


def t3(t: list[int], ai_side: int, player_side: int) -> int:
    """a a a * a\n
    direction x 8"""
    for i in range(8):
        j = t[i * 4 : i * 4 + 4]
        if j[:3] == [ai_side] * 3:
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][0] == ai_side:
                return 11
    return 0


gomoku_ai_template: tuple[Callable[[list[int], int, int], int], ...] = (t0, t1, t2, t3)
