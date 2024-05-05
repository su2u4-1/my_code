import pygame
from random import choice
import matplotlib.pyplot as plt
from noise import pnoise2

a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
     139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
     283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
     457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599]
W, H = 800, 600
seed = [choice(a[72:]), choice(a[36:72]), choice(a[:36])]
print(seed)


def drawplot(p):
    t = [i for i in range(len(p))]
    plt.plot(t, p, color=(0, 0, 0))
    plt.xlim(0, len(t))
    plt.ylim(min(p), max(p))
    plt.legend()
    plt.show()


def draw(d, name="windows"):
    pygame.init()
    pygame.display.set_caption(name)
    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

    while True:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        m = 255 / (mx - mi)

        screen.fill((0, 0, 0))
        for i in range(W):
            for j in range(H):
                # pygame.draw.rect(screen, (m * (d[i][j] - mi), m * (d[i][j] - mi), m * (d[i][j] - mi)), (i * 10, j * 10, 10, 10))
                screen.set_at((i, j), (m * (d[i][j] - mi), m * (d[i][j] - mi), m * (d[i][j] - mi)))
                # screen.set_at((i, j), (255 * d[i][j], 255 * d[i][j], 255 * d[i][j]))

        text = font.render(f"{x},{y},{d[x][y]}", True, (0, 255, 0))
        screen.blit(text, (0, 0))

        pygame.display.update()
        clock.tick()


cop = [[0 for _ in range(H)] for _ in range(W)]

t = []
for x in range(W):
    for y in range(H):
        cop[x][y] = pnoise2(x / seed[0], y / seed[0], base=seed[0])
    t.extend(cop[x])
print(max(t), min(t))
mx, mi = max(t), min(t)
draw(cop)

t = []
for x in range(W):
    for y in range(H):
        cop[x][y] += pnoise2(x / seed[1], y / seed[1], base=seed[1]) / 2
    t.extend(cop[x])
print(max(t), min(t))
mx, mi = max(t), min(t)
draw(cop)

t = []
for x in range(W):
    for y in range(H):
        cop[x][y] += pnoise2(x / seed[2], y / seed[2], base=seed[2]) / 4
    t.extend(cop[x])
print(max(t), min(t))
mx, mi = max(t), min(t)
draw(cop)
