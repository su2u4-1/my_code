from random import randint as ri
import pygame, sys


class Create:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.color = (ri(0, 255), ri(0, 255), ri(0, 255))
        self.move: list[tuple[float, float]] = []


n = int(input("數量:"))
point: list[Create] = []
for _ in range(n):
    point.append(Create(ri(0, 1366), ri(0, 768)))
t = 1

pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("重力")
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_SPACE:
                for i in point:
                    del i
                point = []
                for _ in range(n):
                    point.append(Create(ri(0, 1366), ri(0, 768)))
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
            if i.x == j.x and i.y == j.y:
                continue
            dx = j.x - i.x
            dy = j.y - i.y
            if dx == 0:
                dx = 1
            if dy == 0:
                dy = 1
            if 5 < abs(dx) and 5 < abs(dy):
                r = dx**2 + dy**2
                cr = 1 / r
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
                i.move.append((cx, cy))
            else:
                i.move.append((-(10000 / dx), -(10000 / dy)))
    for i in point:
        for j in i.move:
            i.x += j[0] * f
            i.y += j[1] * f
        if i.x >= W or i.x < 0:
            i.x = ri(0, W - 1)
            i.y = ri(0, H - 1)
        if i.y >= H or i.y < 0:
            i.x = ri(0, W - 1)
            i.y = ri(0, H - 1)
        i.move = []
    screen.fill((0, 0, 0))
    for i in point:
        pygame.draw.circle(screen, i.color, (i.x, i.y), 5)
    pygame.display.update()
    clock.tick(100)
