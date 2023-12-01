import pygame, sys, math, random

color = [
    (0, 255, 255),
    (0, 0, 0),
    (0, 0, 255),
    (255, 0, 255),
    (128, 128, 128),
    (0, 128, 0),
    (0, 255, 0),
    (128, 0, 0),
    (0, 0, 128),
    (128, 128, 0),
    (128, 0, 128),
    (255, 0, 0),
    (192, 192, 192),
    (0, 128, 128),
    (255, 255, 255),
    (255, 255, 0),
]
# 0青,1黑,2藍,3桃,4灰,5綠,6淺綠,7棕,8深藍,9土黃,10紫,11紅,12灰白,13藍綠,14白,15黃
rectcolor = []
for i in range(1600):
    rectcolor.append(random.choices(color, weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


def click(x, y):
    print(math.floor(x / 48), math.floor(y / 48))


def generatemaze(slx, sly):
    global px, py
    maze = []
    endx = slx - 2
    endy = sly - 2
    for x in range(slx):
        z = []
        for y in range(sly):
            if y == 0 or y == sly - 1 or x == 0 or x == slx - 1:
                z.append(1)
            else:
                z.append(0)
        maze.append(z)
    for x in range(0, slx, 2):
        for y in range(0, sly, 2):
            maze[x][y] = 1
    zx = [1, 0, -1, 0]
    zy = [0, 1, 0, -1]
    for x in range(2, slx - 1, 2):
        for y in range(2, sly - 1, 2):
            if y == 2:
                c = random.randint(0, 3)
            elif y != 2:
                c = random.randint(0, 2)
            maze[x + zx[c]][y + zy[c]] = 1
    maze[px][py] = 2
    maze[endx][endy] = 3
    return maze


def main():
    global px, py, screen, SCREEN_SIZE, map
    SCREEN_SIZE = (1200, 900)
    pygame.init()
    pygame.display.set_caption("遊戲5.0")
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 12)
    px = 1
    py = 1
    map = generatemaze(math.floor(screen.get_size()[0] / 48), math.floor(screen.get_size()[1] / 48))
    tmr = 0
    refresh()

    while True:
        tmr += 1
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                SCREEN_SIZE = event.size
                screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE, 32)
                pygame.display.set_caption("Window resized to " + str(event.size))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    py -= 1
                    refresh()
                    print("up", px, py)
                if event.key == pygame.K_DOWN:
                    py += 1
                    refresh()
                    print("down", px, py)
                if event.key == pygame.K_LEFT:
                    px -= 1
                    refresh()
                    print("left", px, py)
                if event.key == pygame.K_RIGHT:
                    px += 1
                    refresh()
                    print("right", px, py)
            if event.type == pygame.MOUSEBUTTONUP:
                click(mousex, mousey)
        txt = font.render(str(tmr), True, (0, 0, 0))
        pygame.display.update(screen.blit(txt, [0, 0]))
        clock.tick(10)


def refresh():
    global screen, SCREEN_SIZE, px, py, map
    screen.fill((0, 0, 0))
    for i in range(math.floor(SCREEN_SIZE[0] / 48)):
        for j in range(math.floor(SCREEN_SIZE[1] / 48)):
            if map[i][j] == 1:
                pygame.display.update(pygame.draw.rect(screen, (0, 0, 0), (i * 48 + 3, j * 48 + 3, 42, 42)))
            if map[i][j] == 0:
                pygame.display.update(pygame.draw.rect(screen, (255, 255, 255), (i * 48 + 3, j * 48 + 3, 42, 42)))
    pygame.display.update(
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            pygame.Rect(px * 48 - 1, py * 48 - 1, 50, 50),
            width=10,
        )
    )


if __name__ == "__main__":
    main()
