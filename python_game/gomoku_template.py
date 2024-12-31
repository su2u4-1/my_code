from random import choice, randint
from typing import Callable

from gamelib import D8, D8_Opposite_side

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

    a p p p *
    p = 8

    a a a * a
    p = 11

    a a a *
    p = 7

    p a a a *
    p = 5
t2:
    p p * p p
    p = 10

    p p * p
    p = 9

    a p p * p
    p = 8

    p p * p a
    p = 8

    p p *
    p = 6

    a a * a a
    p = 11

    a a * a
    p = 7

    a a * a p
    p = 6

    p a a * a
    p = 6

    a a *
    p = 5
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
            if j[3] == ai_side:
                return 9
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][0] == player_side:
                return 10
            else:
                return 8
        elif j[:3] == [ai_side] * 3:
            if j[3] == player_side:
                return 5
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][0] == ai_side:
                return 11
            else:
                return 7
    return 0


def t2(t: list[int], ai_side: int, player_side: int) -> int:
    for i in range(4):
        j = t[i * 4 : i * 4 + 4]
        if j[:2] == [player_side] * 2:
            if j[2] == ai_side:
                return 8
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][:2] == [player_side] * 2:
                return 10
            elif t[i * 4 : i * 4 + 4][0] == player_side:
                if t[i * 4 : i * 4 + 4][1] == 0:
                    return 9
                else:
                    return 8
            else:
                return 6
        elif j[:2] == [ai_side] * 2:
            if j[2] == player_side:
                return 6
            i = D8_Opposite_side[i]
            if t[i * 4 : i * 4 + 4][:2] == [ai_side] * 2:
                return 11
            elif t[i * 4 : i * 4 + 4][0] == ai_side:
                if t[i * 4 : i * 4 + 4][1] == 0:
                    return 7
                else:
                    return 6
            else:
                return 5
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


def gomoku_ai(chessBoard: list[list[int]], ai_side: int, player_side: int) -> tuple[int, int]:
    template: tuple[Callable[[list[int], int, int], int], ...] = (t0, t1, t2, t3, t4)
    priority_positions: list[tuple[int, list[tuple[int, int]]]] = []
    size = len(chessBoard)
    for x in range(size):
        for y in range(size):
            if chessBoard[x][y] == 0:
                t: list[int] = []
                for i in range(8):
                    for j in range(1, 5):
                        nx, ny = x + D8[i][0] * j, y + D8[i][1] * j
                        if 0 <= nx < size and 0 <= ny < size:
                            t.append(chessBoard[nx][ny])
                        else:
                            t.append(-1)
                p = max(c(t, ai_side, player_side) for c in template)
                for i in priority_positions:
                    if i[0] == p:
                        i[1].append((x, y))
                        break
                else:
                    priority_positions.append((p, [(x, y)]))

    priority_positions.sort(key=lambda x: x[0], reverse=True)
    for _, v in priority_positions:
        if len(v) > 0:
            mx, my = choice(v)
            if chessBoard[mx][my] == 0:
                return mx, my
    while True:
        mx, my = randint(0, size - 1), randint(0, size - 1)
        if chessBoard[mx][my] == 0:
            return mx, my
