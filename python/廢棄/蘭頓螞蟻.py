import pygame, sys

pygame.init()
W, H = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("蘭頓螞蟻")
clock = pygame.time.Clock()
point: list[list[int]] = []
d = 0
ant = [960, 540]
mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]
for _ in range(1920):
    a: list[int] = []
    for _ in range(1080):
        a.append(0)
    point.append(a)


def update():
    global d, b
    if 0 <= ant[0] + mx[d] <= 1920 and 0 <= ant[1] + my[d] <= 1080:
        ant[0] += mx[d]
        ant[1] += my[d]
        if point[ant[0]][ant[1]] == 0:
            point[ant[0]][ant[1]] = 1
            if d < 3:
                d += 1
            elif d >= 3:
                d = 0
        elif point[ant[0]][ant[1]] == 1:
            point[ant[0]][ant[1]] = 0
            if d > 0:
                d -= 1
            elif d <= 0:
                d = 3
    else:
        if point[ant[0]][ant[1]] == 0:
            point[ant[0]][ant[1]] = 1
        elif point[ant[0]][ant[1]] == 1:
            point[ant[0]][ant[1]] = 0


def draw():
    for x in range(1920):
        for y in range(1080):
            if point[x][y] == 0:
                screen.set_at((x, y), (255, 255, 255))
            elif point[x][y] == 1:
                screen.set_at((x, y), (0, 0, 0))
    screen.set_at((ant[0], ant[1]), (255, 0, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delete = []
    update()
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    clock.tick(100000000000000000000000000000000000000000)
