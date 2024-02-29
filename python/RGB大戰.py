import pygame, os
from random import randint as ri


class Point:
    def __init__(self, mode: int, value: int, x: int = -1, y: int = -1):
        self.m = mode
        self.v = value
        if x == -1:
            self.x = ri(0, W - 1)
        else:
            self.x = x
        if y == -1:
            self.y = ri(0, H - 1)
        else:
            self.y = y
        self.color = [0, 0, 0]
        self.color[self.m] = self.v

    def move(self):
        self.x += ri(-R, R)
        self.y += ri(-R, R)
        if self.x >= W:
            self.x = W - 1
        elif self.x < 0:
            self.x = 0
        if self.y >= H:
            self.y = H - 1
        elif self.y < 0:
            self.y = 0

    def trans(self, tMode: int):
        self.m = tMode
        self.color = [0, 0, 0]
        self.color[self.m] = self.v


def functionName(x1, y1, x2, y2, r):
    return x1 - r <= x2 <= x1 + r and y1 - r <= y2 <= y1 + r


R = 5
pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
W, H = 500, 500
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.Font("C:\\Windows\\Fonts\\kaiu.ttf", 20)
f = True
c = [0, 0, 0]
pointList = []
csum = 0
for i in range(3):
    for r in range(0, 256, 3):
        c[i] += 1
        csum += 1
        pointList.append(Point(i, r))

while True:
    if f:
        os.system("cls")
        print(f"r {c[0]:3}/{csum} {c[0] / (csum) * 100:.3}%")
        print(f"g {c[1]:3}/{csum} {c[1] / (csum) * 100:.3}%")
        print(f"b {c[2]:3}/{csum} {c[2] / (csum) * 100:.3}%")
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                f = not f
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    screen.fill((0, 0, 0))
    if f:
        for p in pointList:
            p.move()
        for i in pointList:
            for j in pointList:
                if i == j or i.m == j.m:
                    continue
                if functionName(i.x, i.y, j.x, j.y, R):
                    if i.v < j.v and (i.m + 1 == j.m or i.m - 2 == j.m):
                        c[i.m] -= 1
                        c[j.m] += 1
                        i.trans(j.m)
                    elif i.v > j.v and (j.m + 1 == i.m or j.m - 2 == i.m):
                        c[j.m] -= 1
                        c[i.m] += 1
                        j.trans(i.m)
    txt = ""
    for p in pointList:
        color = [0, 0, 0]
        color[p.m] = 255
        pygame.draw.circle(screen, color, (p.x, p.y), R)
        pygame.draw.circle(screen, p.color, (p.x, p.y), R - 1)
        if functionName(p.x, p.y, mx, my, R):
            txt = f"{p.color}, ({p.x},{p.y})"
    screen.blit(font.render(txt, True, (255, 255, 255)), [0, 0])
    pygame.display.update()
    clock.tick(100)
