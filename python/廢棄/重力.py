from random import randint as ri
import pygame, sys


class create:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (ri(0, 255), ri(0, 255), ri(0, 255))
        self.move = []


n = int(input("數量:"))
point = []
for _ in range(n):
    point.append(create(ri(0, 1366), ri(0, 768)))
t = 1

pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
pygame.display.set_caption("重力")
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in point:
                    del i
                point = []
                for _ in range(n):
                    point.append(create(ri(0, 1366), ri(0, 768)))
            elif event.key == pygame.K_1:
                t = 1
            elif event.key == pygame.K_2:
                t = 2
            elif event.key == pygame.K_3:
                t = 4
            elif event.key == pygame.K_4:
                t = 8
            elif event.key == pygame.K_5:
                t = 16
            elif event.key == pygame.K_6:
                t = 32
            elif event.key == pygame.K_7:
                t = 64
            elif event.key == pygame.K_8:
                t = 128
            elif event.key == pygame.K_9:
                t = 256
    if pygame.mouse.get_pressed()[0]:
        f = -1
    elif pygame.mouse.get_pressed()[2]:
        f = 0
    else:
        f = 1
    for i in point:
        for j in point:
            if j.x - 1 <= i.x <= j.x + 1 and j.y - 1 <= i.y <= j.y + 1:
                continue
            else:
                dx = j.x - i.x
                dy = j.y - i.y
                if -250 < dx < 250 and -250 < dy < 250:
                    r = dx**2 + dy**2
                    cr = 10 / r
                    cx = dx * cr * t
                    cy = dy * cr * t
                    if cx >= 0:
                        if cx > dx:
                            cx = dx
                    else:
                        if cx < dx:
                            cx = dx
                    if cy >= 0:
                        if cy > dy:
                            cy = dy
                    else:
                        if cy < dy:
                            cy = dy
                    i.move.append([cx, cy])
    for i in point:
        for j in i.move:
            i.x += j[0] * f
            i.y += j[1] * f
            if i.x >= W:
                i.x = W
            elif i.x <= 0:
                i.x = 0
            if i.y >= H:
                i.y = H
            elif i.y <= 0:
                i.y = 0
        i.move = []
    screen.fill((0, 0, 0))
    for i in point:
        screen.set_at((round(i.x), round(i.y)), i.color)
    pygame.display.update()
    clock.tick(100)
