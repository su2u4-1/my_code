from typing import Callable
from gamelib import D8_Opposite_side

"""
a = ai
p = player
* = current position
0 = empty
p = priority

t0:
    a a a a *
    p = 10

    p p p p *
    p = 11
t1:
    p p p * p
    p = 10

    p p p *
    p = 9

    a a a * a
    p = 11

    a a a *
    p = 8
t2:
    p p * p p
    p = 10

    p p * p
    p = 9

    p p *
    p = 7

    a a * a a
    p = 11

    a a * a
    p = 8

    a a *
    p = 6
t3:
    p *
    p = 2

    a *
    p = 1
t4:
    0   0   0
      0 0 0
    0 0 * 0 0
      0 0 0
    0   0   0
    p = -1
"""


def t0(t: list[int], ai_side: int, player_side: int) -> int:
    for i in range(8):
        for j in t[i * 4 : i * 4 + 4]:
            if j != ai_side:
                break
        else:
            return 11
        for j in t[i * 4 : i * 4 + 4]:
            if j != player_side:
                break
        else:
            return 10
    return 0


def t1(t: list[int], ai_side: int, player_side: int) -> int:
    for i in range(8):
        j = t[i * 4 : i * 4 + 4]
        if j[:3] == [player_side] * 3:
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][0] == player_side:
                return 10
            else:
                return 9
        elif j[:3] == [ai_side] * 3:
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][0] == ai_side:
                return 11
            else:
                return 8
    return 0


def t2(t: list[int], ai_side: int, player_side: int) -> int:
    for i in range(4):
        j = t[i * 4 : i * 4 + 4]
        if j[:2] == [player_side] * 2:
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][:2] == [player_side] * 2:
                return 10
            elif t[i * 4 : i * 4 + 4][0] == player_side:
                return 9
            else:
                return 7
        elif j[:2] == [ai_side] * 2:
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][:2] == [ai_side] * 2:
                return 11
            elif t[i * 4 : i * 4 + 4][0] == ai_side:
                return 8
            else:
                return 6
    return 0


def t3(t: list[int], ai_side: int, player_side: int) -> int:
    for i in range(8):
        if t[i * 4 : i * 4 + 4][0] == player_side:
            return 2
        elif t[i * 4 : i * 4 + 4][0] == ai_side:
            return 1
    return 0


def t4(t: list[int], ai_side: int, player_side: int) -> int:
    for i in range(8):
        for j in t[i * 4 : i * 4 + 4][:2]:
            if j == 1 or j == 2:
                return 0
    return -1


gomoku_ai_template: tuple[Callable[[list[int], int, int], int], ...] = (t0, t1, t2, t3, t4)
