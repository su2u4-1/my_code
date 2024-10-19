import pygame, sys, math, random, os


def generatemap(ax: int, ay: int, n: int):
    c = [[0 for _ in range(ay)] for _ in range(ax)]
    for i in range(n):
        while True:
            x = random.randint(0, xl - 1)
            y = random.randint(0, yl - 1)
            if c[x][y] == 0:
                c[x][y] = 9
                break
    for i in range(ax):
        for j in range(ay):
            if c[i][j] == 0:
                for d in range(-1, 2):
                    for e in range(-1, 2):
                        if 0 <= i + d < xl and 0 <= j + e < yl and c[i + d][j + e] == 9:
                            c[i][j] += 1
    return c


def openpart(x: int, y: int):
    for f in range(-1, 2):
        for g in range(-1, 2):
            if 0 <= x + f < xl and 0 <= y + g < yl:
                if showmap[x + f][y + g] == -1:
                    rightchick(x + f, y + g)


def openall():
    global flag
    flag = 1
    for x in range(xl):
        for y in range(yl):
            if map[x][y] == 9:
                showmap[x][y] = map[x][y]


def rightchick(x: int, y: int):
    if showmap[x][y] != 10:
        showmap[x][y] = map[x][y]
        if map[x][y] == 9:
            openall()
        if map[x][y] == 0:
            openpart(x, y)


def leftchick(x: int, y: int):
    if showmap[x][y] == 10:
        showmap[x][y] = -1
    elif showmap[x][y] == -1:
        showmap[x][y] = 10


def chickall():
    global flag
    n = 0
    for x in range(xl):
        for y in range(yl):
            if showmap[x][y] == 10 and map[x][y] != 9:
                return
            if showmap[x][y] == 10 or showmap[x][y] == -1:
                n += 1
    if n == g:
        flag = 2


mx = 0
my = 0
tmr = 0
flag = 0
pygame.init()
xl = math.floor(pygame.display.Info().current_w / 50)
yl = math.floor(pygame.display.Info().current_h / 50)
pygame.display.set_caption("踩地雷")
screen = pygame.display.set_mode((xl * 50, yl * 50), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font("C:\\Windows\\Fonts\\kaiu.ttf", 48)
g = round((xl * yl) / 5)
map = generatemap(xl, yl, g)
showmap = [[-1 for _ in range(yl)] for _ in range(xl)]
img: list[pygame.Surface] = []
for i in range(11):
    img.append(pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "\\踩地雷圖片\\" + str(i) + ".png"))

while True:
    tmr += 1
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and flag == 0:
            if mx == math.floor(mousex / 50) and my == math.floor(mousey / 50):
                rightchick(mx, my)
            else:
                mx = math.floor(mousex / 50)
                my = math.floor(mousey / 50)
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and flag == 0:
            if mx == math.floor(mousex / 50) and my == math.floor(mousey / 50):
                leftchick(mx, my)
    screen.fill((255, 255, 255))
    for i in range(xl):
        for j in range(yl):
            if showmap[i][j] == -1:
                pygame.draw.rect(screen, (0, 0, 0), (i * 50 + 1, j * 50 + 1, 48, 48))
            else:
                screen.blit(img[showmap[i][j]], [i * 50, j * 50])
    chickall()
    if flag == 1:
        txt = font.render("你輸了", True, (255, 0, 0), (0, 255, 0))
        screen.blit(txt, txt.get_rect(center=(pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2)))
    elif flag == 2:
        txt = font.render("你贏了", True, (255, 0, 0), (0, 255, 0))
        screen.blit(txt, txt.get_rect(center=(pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2)))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(mx * 50, my * 50, 50, 50), width=5)
    pygame.display.update()
    clock.tick(60)
