import pygame
from random import randrange as rr

pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

point: list[tuple[int, int, tuple[int, int, int]]] = []
screen.fill((0, 0, 0))


def draw() -> None:
    screen.fill((0, 0, 0))
    for x in range(W):
        for y in range(H):
            min_d = W * H
            color = (0, 0, 0)
            for p in point:
                d = (x - p[0]) ** 2 + (y - p[1]) ** 2
                if d < min_d:
                    min_d = d
                    color = p[2]
            screen.set_at((x, y), color)


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
                draw()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                point.append((mx, my, (rr(0, 256), rr(0, 256), rr(0, 256))))
                draw()

    for i in point:
        pygame.draw.circle(screen, (0, 0, 0), (i[0], i[1]), 5, 2)

    pygame.display.update()
    clock.tick(10)
