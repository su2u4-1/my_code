import pygame
from random import randint as ri


class Point:
    def __init__(self, color: tuple[int, int, int] = (128, 128, 128)):
        self.x = ri(0, W - 1)
        self.y = ri(0, H - 1)
        self.xy = (self.x, self.y)
        self.color = color
        self.son: list[Point] = []


pygame.init()
# W = pygame.display.Info().current_w
# H = pygame.display.Info().current_h
W, H = 800, 600
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)
point = [Point() for _ in range(500)]
p = [Point((255, 0, 0)), Point((0, 255, 0)), Point((0, 0, 255))]
line = []
flag_0 = False
flag_1 = False

line: list[tuple[tuple[int, int, int], tuple[int, int], tuple[int, int]]] = []


def f1():
    line.clear()
    for i in p:
        i.son = []
    for i in point:
        t = min(p, key=lambda a: (a.x - i.x) ** 2 + (a.y - i.y) ** 2)
        i.color = t.color
        t.son.append(i)
        line.append((t.color, i.xy, t.xy))
    for i in p:
        tx: list[int] = []
        ty: list[int] = []
        for j in i.son:
            tx.append(j.x)
            ty.append(j.y)
        if len(tx) == 0:
            i.x = ri(0, W - 1)
        else:
            i.x = sum(tx) // len(tx)
        if len(ty) == 0:
            i.y = ri(0, H - 1)
        else:
            i.y = sum(ty) // len(ty)
        i.xy = (i.x, i.y)


def f2():
    t: list[tuple[int, int]] = []
    for i in point:
        mi = (10000, -1, -1)
        for j in point:
            if i.xy == j.xy:
                continue
            dx, dy = j.x - i.x, j.y - i.y
            r2 = dx**2 + dy**2
            if r2 < mi[0]:
                mi = (r2**0.5, dx, dy)
        t.append((mi[1] // mi[0] * 10, mi[2] // mi[0] * 10))
    for i, e in zip(point, t):
        i.x += e[0]
        i.y += e[1]
        if i.x < 0 or i.x >= W:
            i.x = ri(0, W - 1)
            i.color = (128, 128, 128)
        if i.y < 0 or i.y >= H:
            i.y = ri(0, H - 1)
            i.color = (128, 128, 128)
        i.xy = (i.x, i.y)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_SPACE:
                if flag_0 or flag_1:
                    flag_0 = False
                    flag_1 = False
                else:
                    flag_0 = True
                    flag_1 = True
            elif event.key == pygame.K_h:
                f1()
            elif event.key == pygame.K_g:
                f2()
            elif event.key == pygame.K_r:
                point = [Point() for _ in range(500)]
                p = [Point((255, 0, 0)), Point((0, 255, 0)), Point((0, 0, 255))] + [Point((ri(0, 255), ri(0, 255), ri(0, 255))) for _ in range(len(p) - 3)]
                line = []
            elif event.key == pygame.K_e:
                line = []
                for i in p:
                    i.son = []
                for i in point:
                    i.color = (128, 128, 128)
            elif event.key == pygame.K_f:
                flag_0 = not flag_0
            elif event.key == pygame.K_d:
                flag_1 = not flag_1
            elif event.key == pygame.K_j:
                p.append(Point((ri(0, 255), ri(0, 255), ri(0, 255))))
            elif event.key == pygame.K_k:
                p.pop()

    if flag_0:
        f1()
    if flag_1:
        f2()

    screen.fill((0, 0, 0))
    text = font.render(str(len(p)), True, (255, 255, 255))
    screen.blit(text, (0, 0))
    for i in point:
        pygame.draw.circle(screen, i.color, i.xy, 5, 3)
    for i in p:
        pygame.draw.circle(screen, i.color, i.xy, 5)
    for i in line:
        pygame.draw.line(screen, i[0], i[1], i[2])
    pygame.display.update()
    clock.tick(10)
