from dataclasses import dataclass
from typing import Literal
from math import floor as fl

import pygame


@dataclass
class data:
    number: int
    xy_list: list[tuple[int, int]]
    side: Literal[1, 2]


def put_chess(x: int, y: int, p: Literal[1, 2]) -> Literal[1, 2]:
    board[x][y] = p
    n: list[data] = []
    for j in range(4):
        if 0 <= x + DX[j] < 19 and 0 <= y + DY[j] < 19:
            for i in range(len(same_color_chess)):
                if (x + DX[j], y + DY[j]) in same_color_chess[i].xy_list and same_color_chess[i].side == p:
                    same_color_chess[i].xy_list.append((x, y))
                    n.append(same_color_chess[i])
    if len(n) == 0:
        same_color_chess.append(data(1, [(x, y)], p))
    elif len(n) != 1:
        c: list[tuple[int, int]] = []
        for i in n:
            c += i.xy_list
            while i in same_color_chess:
                same_color_chess.remove(i)
        for i in c:
            while c.count(i) > 1:
                c.remove(i)
        same_color_chess.append(data(1, c, p))
    check(x, y)
    return 2 if p == 1 else 1


def check(x: int, y: int):
    for i in range(len(same_color_chess)):
        for j in range(len(same_color_chess)):
            if i != j and same_color_chess[i].side == same_color_chess[j].side:
                for k in same_color_chess[i].xy_list:
                    for l in same_color_chess[j].xy_list:
                        if k == l:
                            same_color_chess[i].xy_list += same_color_chess[j].xy_list
                            same_color_chess.remove(same_color_chess[j])
    for i in range(len(same_color_chess)):
        same_color_chess[i].number = 0
        for j in same_color_chess[i].xy_list:
            for k in range(4):
                if 0 <= j[0] + DX[k] < 19 and 0 <= j[1] + DY[k] < 19:
                    if board[j[0] + DX[k]][j[1] + DY[k]] == 0:
                        same_color_chess[i].number += 1
    for i in same_color_chess:
        if (x, y) != (-1, -1):
            if (x, y) not in i.xy_list and i.number <= 0:
                for j in i.xy_list:
                    board[j[0]][j[1]] = 0
                same_color_chess.remove(i)
        if (x, y) == (-1, -1):
            if i.number <= 0:
                for j in i.xy_list:
                    board[j[0]][j[1]] = 0
                same_color_chess.remove(i)
    if (x, y) != (-1, -1):
        check(-1, -1)


def main():
    pygame.init()
    pygame.display.set_caption("圍棋")
    screen = pygame.display.set_mode(((L - 1) * 44 + 54, (L - 1) * 44 + 54), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    f: Literal[1, 2] = 1

    while True:
        mx, my = pygame.mouse.get_pos()
        mx = fl(mx / 44)
        my = fl(my / 44)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    try:
                        if board[mx][my] == 0:
                            f = put_chess(mx, my, f)
                    except:
                        pass

        screen.fill((238, 154, 73))
        for i in range(L):
            if i == 0 or i == L - 1:
                pygame.draw.line(screen, (0, 0, 0), [i * 44 + 27, 27], [i * 44 + 27, (L - 1) * 44 + 27], 4)
                pygame.draw.line(screen, (0, 0, 0), [27, i * 44 + 27], [(L - 1) * 44 + 27, i * 44 + 27], 4)
            else:
                pygame.draw.line(screen, (0, 0, 0), [i * 44 + 27, 27], [i * 44 + 27, (L - 1) * 44 + 27], 2)
                pygame.draw.line(screen, (0, 0, 0), [27, i * 44 + 27], [(L - 1) * 44 + 27, i * 44 + 27], 2)
        for i in range(L):
            for j in range(L):
                if board[i][j] == 1:
                    pygame.draw.circle(screen, (0, 0, 0), (i * 44 + 28, j * 44 + 28), 13)
                elif board[i][j] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (i * 44 + 28, j * 44 + 28), 13)
        if f == 1:
            pygame.draw.circle(screen, (0, 0, 0), (mx * 44 + 28, my * 44 + 28), 15, width=3)
        else:
            pygame.draw.circle(screen, (255, 255, 255), (mx * 44 + 28, my * 44 + 28), 15, width=3)

        pygame.display.update()
        clock.tick(100)


if __name__ == "__main__":
    DX = [0, 1, 0, -1]
    DY = [1, 0, -1, 0]
    L = 19
    board = [[0 for _ in range(L)] for _ in range(L)]
    same_color_chess: list[data] = []
    main()
