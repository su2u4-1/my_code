import pygame
from random import choice, randint

W, H = 80, 60
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
d1 = [0, 1, 0, -1, 1, -1, 1, -1]
d2 = [1, 0, -1, 0, 1, -1, -1, 1]
seed = [choice(a), choice(a), choice(a), choice(a), choice(a), choice(a)]
seed = [17, 29, 5, 17, 29, 5]
mi, mx = 0, 0
print(seed)


def draw(d, name="windows"):
    pygame.init()
    pygame.display.set_caption(name)
    # font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W * 10, H * 10), pygame.RESIZABLE)
    m = 255 / (mx - mi)

    while True:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        for i in range(W):
            for j in range(H):
                pygame.draw.rect(screen, (m * (d[i][j] - mi), m * (d[i][j] - mi), m * (d[i][j] - mi)), (i * 10, j * 10, 10, 10))

        # text = font.render(f"{x},{y},{d[x // 10][y // 10]}", True, (0, 255, 0))
        # screen.blit(text, (0, 0))

        pygame.display.update()
        clock.tick()


def gb(x, y):
    global mx, mi
    a = 0
    a += hash((x // seed[0], y // seed[0], randint(-1, 1)))
    a += hash((x // seed[1], y // seed[1], randint(-1, 1)))
    a += hash((x // seed[2], y // seed[2], randint(-1, 1)))
    a += hash((x // seed[3], y // seed[3], randint(-1, 1)))
    a += hash((x // seed[4], y // seed[4], randint(-1, 1)))
    a += hash((x // seed[5], y // seed[5], randint(-1, 1)))
    a += hash((x, y, randint(-1, 1)))
    a = a
    if a > mx:
        mx = a
    if a < mi:
        mi = a
    return a


def kk(ori):
    global mx, mi
    mi, mx = 0, 0
    ne = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(W):
        for j in range(H):
            n = 0
            for d in range(8):
                if 0 <= i + d1[d] < W and 0 <= j + d2[d] < H:
                    for r in ori:
                        ne[i][j] += r[i + d1[d]][j + d2[d]]
                        n += 1
            # ne[i][j] /= n
            # ne[i][j] += gb(i, j) * len(ori)
            if ne[i][j] > mx:
                mx = ne[i][j]
            if ne[i][j] < mi:
                mi = ne[i][j]
    print(mx, mi)
    return ne


mc = [[gb(i, j) for j in range(H)] for i in range(W)]
print(mx, mi)
draw(mc, "c0")

mc1 = kk([mc])
draw(mc1, "c1")
mc2 = kk([mc, mc1])
draw(mc2, "c2")
mc3 = kk([mc, mc1, mc2])
draw(mc3, "c3")
mc4 = kk([mc, mc1, mc2, mc3])
draw(mc4, "c4")
mc5 = kk([mc, mc1, mc2, mc3, mc4])
draw(mc5, "c5")
mc6 = kk([mc, mc1, mc2, mc3, mc4, mc5])
draw(mc6, "c6")
mc7 = kk([mc, mc1, mc2, mc3, mc4, mc5, mc6])
draw(mc7, "c7")
mc8 = kk([mc, mc1, mc2, mc3, mc4, mc5, mc6, mc7])
draw(mc8, "c8")
mc9 = kk([mc, mc1, mc2, mc3, mc4, mc5, mc6, mc7, mc8])
draw(mc9, "c9")
mc10 = kk([mc, mc1, mc2, mc3, mc4, mc5, mc6, mc7, mc8, mc9])
draw(mc10, "c10")
