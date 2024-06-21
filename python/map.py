import pygame
from random import randrange as rr

pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

point: list[tuple[int, int, tuple[int, int, int]]] = []


def dist(x: int, y: int) -> tuple[int, int, int] | None:
    min_d = float("inf")
    color = None
    for i in point:
        d = (x - i[0]) ** 2 + (y - i[1]) ** 2
        if min_d > d:
            min_d = d
            color = i[2]
    return color


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
                point.append((rr(0, W), rr(0, H), (rr(0, 256), rr(0, 256), rr(0, 256))))

    for i in range(W):
        for j in range(H):
            color = dist(i, j)
            if color is None:
                screen.set_at((i, j), (0, 0, 0))
            else:
                screen.set_at((i, j), color)

    for i in point:
        pygame.draw.circle(screen, (0, 0, 0), (i[0], i[1]), 5, 2)

    pygame.display.update()
    clock.tick(10)
