import pygame, sys
from random import randint as ri
from math import floor

W, L = 1350, 750
w = 10

pygame.init()
screen = pygame.display.set_mode((W, L))
pygame.display.set_caption("雜訊")
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

map = []
for x in range(round(W / w)):
    a = []
    for y in range(round(L / w)):
        a.append([128, 128, 128])
    map.append(a)

a1 = [1, 0, -1, 0]
a2 = [0, 1, 0, -1]
tmr = 0
s = 1
h = 0

while True:
    tmr += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                h += 1
            elif event.key == pygame.K_0:
                s = 0
            elif event.key == pygame.K_1:
                s = 1
            elif event.key == pygame.K_2:
                s = 2
            elif event.key == pygame.K_3:
                s = 3
            elif event.key == pygame.K_4:
                s = 4
            elif event.key == pygame.K_5:
                s = 5
            elif event.key == pygame.K_6:
                s = 6
            elif event.key == pygame.K_7:
                s = 7
            elif event.key == pygame.K_8:
                s = 8
            elif event.key == pygame.K_9:
                s = 9

    for _ in range(ri(100, 300)):
        for i in range(3):
            x, y = ri(0, round(W / w) - 1), ri(0, round(L / w) - 1)
            map[x][y][i] += ri(-10, 10)
            map[x][y][i] = (0, map[x][y][i])[map[x][y][i] > 0]
            map[x][y][i] = (255, map[x][y][i])[map[x][y][i] < 255]
            map[x][y][i] = round(map[x][y][i])
    mx, my = pygame.mouse.get_pos()
    mx, my = floor(mx / w), floor(my / w)
    txt = font.render(f"x:{mx},y:{my},color:{map[mx][my]},time:{tmr},speed:{s}", True, (0, 0, 0))

    for x in range(round(W / w)):
        for y in range(round(L / w)):
            for i in range(3):
                if map[x][y][i] >= 230:
                    map[x][y][i] = 26
                if map[x][y][i] <= 25:
                    map[x][y][i] = 229

    screen.fill((255, 255, 255))
    for x in range(round(W / w)):
        for y in range(round(L / w)):
            pygame.draw.rect(
                screen,
                (map[x][y][0], map[x][y][1], map[x][y][2]),
                (x * w, y * w, w, w),
                0,
            )
    if h % 2 == 1:
        screen.blit(txt, [0, 0])
    pygame.display.update()
    clock.tick(10 * s)
