import pygame, os
import matplotlib.pyplot as plt
from random import randint as ri


def drawplot(t, p):
    mi, mx = [], []
    for i in range(CL):
        plt.plot(t, p[i], color=(COLOR[i][0], COLOR[i][1], COLOR[i][2]), label=i)
        mx.append(max(p[i]))
        mi.append(min(p[i]))
    plt.xlim(0, len(t))
    plt.ylim(min(mi), max(mx))
    plt.legend()
    plt.show()


class Point:
    def __init__(self, mode: int, x: int = -1, y: int = -1):
        self.m = mode
        if x == -1:
            self.x = ri(0, W - 1)
        else:
            self.x = x
        if y == -1:
            self.y = ri(0, H - 1)
        else:
            self.y = y
        self.color = [COLOR[mode][0] * 255, COLOR[mode][1] * 255, COLOR[mode][2] * 255]

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
        self.color = [COLOR[tMode][0] * 255, COLOR[tMode][1] * 255, COLOR[tMode][2] * 255]


def functionName(x1, y1, x2, y2, r):
    return x1 - r <= x2 <= x1 + r and y1 - r <= y2 <= y1 + r


pygame.init()
R = 5
SAMP = [10, 1000]
COLOR = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 0)]
CL = len(COLOR)
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
W, H = 500, 500

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.Font("C:\\Windows\\Fonts\\kaiu.ttf", 20)

f = True
c = []
pointList = []
csum = 0
t = 0
time, poi = [], []

for i in range(CL):
    poi.append([])
    c.append(0)
    for _ in range(0, 256, CL):
        c[i] += 1
        csum += 1
        pointList.append(Point(i))

while True:
    t += 1
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
                    if i.m + 1 == j.m or i.m - CL + 1 == j.m:
                        c[i.m] -= 1
                        c[j.m] += 1
                        i.trans(j.m)
                    elif j.m + 1 == i.m or j.m - CL + 1 == i.m:
                        c[j.m] -= 1
                        c[i.m] += 1
                        j.trans(i.m)
    for p in pointList:
        pygame.draw.circle(screen, p.color, (p.x, p.y), R)
    if t % SAMP[0] == 0:
        time.append(t / SAMP[0])
        for i in range(CL):
            poi[i].append(c[i])
        os.system("cls")
        print(f"{(t*100)/(SAMP[0]*SAMP[1])}%")
    if t == SAMP[0] * SAMP[1]:
        pygame.quit()
        drawplot(time, poi)
        exit()
    pygame.display.update()
    clock.tick(10000)
