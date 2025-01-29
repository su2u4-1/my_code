from math import floor
from random import randint as ri
from random import choice as rc
import pygame


def glp(x0: int, y0: int, x1: int, y1: int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    x, y = x0, y0
    pixels: list[tuple[int, int]] = []
    err = dx - dy
    while True:
        pixels.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err = err - dy
            x = x + sx
        if e2 < dx:
            err = err + dx
            y = y + sy
    return pixels


def show(d: int):
    pygame.init()
    pygame.display.set_caption("遊戲4.0")
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 16)
    tmr = 0
    pygame.display.update(screen.fill((255, 255, 255)))
    while True:
        tmr += 1
        mx, my = pygame.mouse.get_pos()
        mx = floor(mx / 7)
        my = floor(my / 7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for i in range(w):
            for j in range(h):
                if map[i][j][1]:
                    a = (0, 0, 255)
                elif map[i][j][0] == 0:
                    a = (0, 0, 255)
                else:
                    a = (
                        floor(map[i][j][0] * (255 / d)),
                        floor(map[i][j][0] * (255 / d)),
                        floor(map[i][j][0] * (255 / d)),
                    )
                pygame.draw.rect(screen, a, (i * 7, j * 7, 7, 7))
        txt = font.render(
            f"t:{tmr},x/y:{mx}/{my},h:{map[mx][my][0]},w:{map[mx][my][1]}",
            True,
            (255, 255, 255),
        )
        screen.blit(txt, [0, 0])
        pygame.display.update()
        clock.tick(10)


# 地圖
w, h = 100, 100
e = 1000
map: list[list[tuple[int, bool]]] = []
for i in range(w):
    a: list[tuple[int, bool]] = []
    for j in range(h):
        # 高度,水流
        a.append((0, False))
    map.append(a)
# 山脈
line: list[list[tuple[int, int]]] = []
for _ in range(ri(1, 10)):
    x1, y1, x2, y2 = ri(0, 99), ri(0, 99), ri(0, 99), ri(0, 99)
    line.append(glp(x1, y1, x2, y2))
# 水源
water: list[tuple[int, int]] = []
for i in line:
    for j in i:
        map[j[0]][j[1]] = (ri(int(0.9 * e), e), map[j[0]][j[1]][1])
        x = j[0] + ri(-3, 3)
        y = j[1] + ri(-3, 3)
        if x >= 0 and x < w and y >= 0 and y < h and ri(1, 10) == 1:
            if map[x][y][0] == 0:
                water.append((x, y))
                map[x][y] = (map[x][y][0], True)
# 山
b1 = [1, 0, -1, 0]
b2 = [0, 1, 0, -1]
while True:
    n1 = 0
    for i in range(w):
        for j in range(h):
            for n in range(4):
                if i + b1[n] >= 0 and j + b2[n] >= 0 and i + b1[n] < w and j + b2[n] < h:
                    if map[i][j][0] >= map[i + b1[n]][j + b2[n]][0] + 10:
                        k = ri(1, ri(1, ri(1, 10)))
                        map[i][j] = (map[i][j][0] - k, map[i][j][1])
                        map[i + b1[n]][j + b2[n]] = (map[i + b1[n]][j + b2[n]][0] + k, map[i + b1[n]][j + b2[n]][1])
                        n1 += 1
    if n1 == 0:
        break
# 河
b1 = [1, 0, -1, 0]
b2 = [0, 1, 0, -1]
river: list[list[tuple[int, int]]] = []
for b in water:
    x, y = b[0], b[1]
    river.append([(x, y)])
    while True:
        flag = False
        c = [0, 1, 2, 3]
        for _ in range(4):
            n = rc(c)
            if x + b1[n] >= 0 and y + b2[n] >= 0 and x + b1[n] < w and y + b2[n] < h:
                if map[x][y][0] + ri(0, 5) > map[x + b1[n]][y + b2[n]][0]:
                    map[x + b1[n]][y + b2[n]] = (map[x + b1[n]][y + b2[n]][0], True)
                    x, y = x + b1[n], y + b2[n]
                    river[len(river) - 1].append((x, y))
                    break
            c.remove(n)
        else:
            break
# 顯示
d = 0
for i in range(w):
    for j in range(h):
        if map[i][j][0] > d:
            d = map[i][j][0]
show(d)
