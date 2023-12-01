import pygame
from math import floor as fl
from random import randint as ri


def put_chess(x, y, p):
    print(x, y, p)
    file.write(str((x, y, p)) + "\n")
    board[x][y] = p
    n = []
    for j in range(4):
        if 0 <= x + A[j] < 19 and 0 <= y + B[j] < 19:
            for i in range(len(same_color_chess)):
                if (x + A[j], y + B[j]) in same_color_chess[i][1] and same_color_chess[i][2] == p:
                    same_color_chess[i][1].append((x, y))
                    n.append(same_color_chess[i])
    if len(n) == 0:
        same_color_chess.append([1, [(x, y)], p])
    elif len(n) != 1:
        c = []
        for i in n:
            c += i[1]
            while i in same_color_chess:
                same_color_chess.remove(i)
        for i in c:
            while c.count(i) > 1:
                c.remove(i)
        same_color_chess.append([1, c, p])
    check(x, y)


def check(x, y):
    for i in range(len(same_color_chess)):
        for j in range(len(same_color_chess)):
            if i != j and same_color_chess[i][2] == same_color_chess[j][2]:
                for k in same_color_chess[i][1]:
                    for l in same_color_chess[j][1]:
                        if k == l:
                            same_color_chess[i][1] += same_color_chess[j][1]
                            same_color_chess.remove(same_color_chess[j])
    for i in range(len(same_color_chess)):
        same_color_chess[i][0] = 0
        for j in same_color_chess[i][1]:
            for k in range(4):
                if 0 <= j[0] + A[k] < 19 and 0 <= j[1] + B[k] < 19:
                    if board[j[0] + A[k]][j[1] + B[k]] == 0:
                        same_color_chess[i][0] += 1
    for i in same_color_chess:
        if (x, y) != (-1, -1):
            if (x, y) not in i[1] and i[0] <= 0:
                for j in i[1]:
                    board[j[0]][j[1]] = 0
                same_color_chess.remove(i)
        if (x, y) == (-1, -1):
            if i[0] <= 0:
                for j in i[1]:
                    board[j[0]][j[1]] = 0
                same_color_chess.remove(i)
    if (x, y) != (-1, -1):
        check(-1, -1)


def main():
    pygame.init()
    pygame.display.set_caption("圍棋")
    screen = pygame.display.set_mode(((l - 1) * 44 + 54, (l - 1) * 44 + 54), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    font = pygame.font.Font("C:\\Windows\\Fonts\\kaiu.ttf", 48)

    for _ in range(l):
        a = []
        for _ in range(l):
            a.append(0)
        board.append(a)
    f = 1

    while True:
        mx, my = pygame.mouse.get_pos()
        mx = fl(mx / 44)
        my = fl(my / 44)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        screen.fill((238, 154, 73))
        for i in range(l):
            if i == 0 or i == l - 1:
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    [i * 44 + 27, 27],
                    [i * 44 + 27, (l - 1) * 44 + 27],
                    4,
                )
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    [27, i * 44 + 27],
                    [(l - 1) * 44 + 27, i * 44 + 27],
                    4,
                )
            else:
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    [i * 44 + 27, 27],
                    [i * 44 + 27, (l - 1) * 44 + 27],
                    2,
                )
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    [27, i * 44 + 27],
                    [(l - 1) * 44 + 27, i * 44 + 27],
                    2,
                )
        empty = []
        for i in range(l):
            for j in range(l):
                if board[i][j] == 1:
                    pygame.draw.circle(screen, (0, 0, 0), (i * 44 + 28, j * 44 + 28), 13)
                elif board[i][j] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (i * 44 + 28, j * 44 + 28), 13)
                else:
                    empty.append((i, j))
        if len(empty) < 10:
            pygame.quit()
            break
        i = empty[ri(0, len(empty) - 1)]
        if f == 1:
            put_chess(i[0], i[1], f)
            f = 2
            # pygame.draw.circle(screen,(0,0,0),(mx*44+28,my*44+28),15,width=3)
        elif f == 2:
            put_chess(i[0], i[1], f)
            f = 1
            # pygame.draw.circle(screen,(255,255,255),(mx*44+28,my*44+28),15,width=3)

        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    A = [0, 1, 0, -1]
    B = [1, 0, -1, 0]
    board = []
    same_color_chess = []
    l = 19
    file = open("圍棋.txt", "w+")
    main()
    file.close()
