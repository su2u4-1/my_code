import pygame, os
from math import floor as fl


def update1(x: int, y: int, state: str = "No"):
    global data
    if x not in data:
        return
    elif y not in data[x]:
        return
    a1 = [0, 1, 0, -1]
    a2 = [-1, 0, 1, 0]
    if state != "No":
        data[x][y][2] = state
    if data[x][y][0] == "button":
        for i in range(4):
            update1(x + a1[i], y + a2[i], data[x][y][2])
    elif data[x][y][0] == "line":
        if data[x][y][1] == "up":
            update1(x, y - 1, data[x][y][2])
        elif data[x][y][1] == "down":
            update1(x, y + 1, data[x][y][2])
        elif data[x][y][1] == "left":
            update1(x - 1, y, data[x][y][2])
        elif data[x][y][1] == "right":
            update1(x + 1, y, data[x][y][2])
    elif data[x][y][0] == "not" or data[x][y][0] == "turn":
        if data[x][y][1] == "up":
            d = 2
        elif data[x][y][1] == "down":
            d = 0
        elif data[x][y][1] == "left":
            d = 1
        elif data[x][y][1] == "right":
            d = 3
        else:
            d = -1
        for i in range(4):
            if data[x][y][0] == "not":
                if data[x][y][2] == "unpower" and i != d:
                    update1(x + a1[i], y + a2[i], "power")
                elif data[x][y][2] == "power" and i != d:
                    update1(x + a1[i], y + a2[i], "unpower")
            elif data[x][y][0] == "turn" and i != d:
                update1(x + a1[i], y + a2[i], data[x][y][2])


def update2(x: int, y: int):
    global data
    if x in data and y in data[x]:
        if data[x][y][0] == "line":
            n = 0
            if x + 1 in data and y in data[x + 1] and data[x][y][1] != "right":
                if data[x + 1][y][2] == "power":
                    if data[x + 1][y][0] == "button":
                        n += 1
                    elif data[x + 1][y][0] == "line" and data[x + 1][y][1] == "left":
                        n += 1
                elif data[x + 1][y][0] == "not" and data[x + 1][y][1] != "right":
                    n += 1
            if x - 1 in data and y in data[x - 1] and data[x][y][1] != "left":
                if data[x - 1][y][2] == "power":
                    if data[x - 1][y][0] == "button":
                        n += 1
                    elif data[x - 1][y][0] == "line" and data[x - 1][y][1] == "right":
                        n += 1
                elif data[x - 1][y][0] == "not" and data[x - 1][y][1] != "left":
                    n += 1
            if y + 1 in data[x] and data[x][y][1] != "dowm":
                if data[x][y + 1][2] == "power":
                    if data[x][y + 1][0] == "button":
                        n += 1
                    elif data[x][y + 1][0] == "line" and data[x][y + 1][1] == "up":
                        n += 1
                elif data[x][y + 1][0] == "not" and data[x][y + 1][1] != "down":
                    n += 1
            if y - 1 in data[x] and data[x][y][1] != "up":
                if data[x][y - 1][2] == "power":
                    if data[x][y - 1][0] == "button":
                        n += 1
                    elif data[x][y - 1][0] == "line" and data[x][y - 1][1] == "down":
                        n += 1
                elif data[x][y - 1][0] == "not" and data[x][y - 1][1] != "up":
                    n += 1
            if n > 0:
                data[x][y][2] = "power"
            else:
                data[x][y][2] = "unpower"
        if data[x][y][0] == "not":
            n = 0
            if x + 1 in data and y in data[x + 1] and data[x][y][1] == "left":
                if data[x + 1][y][2] == "power":
                    if data[x + 1][y][0] == "button":
                        n += 1
                    elif data[x + 1][y][0] == "line" and data[x + 1][y][1] == "left":
                        n += 1
                elif data[x + 1][y][0] == "not" and data[x + 1][y][1] != "right":
                    n += 1
            if x - 1 in data and y in data[x - 1] and data[x][y][1] == "right":
                if data[x - 1][y][2] == "power":
                    if data[x - 1][y][0] == "button":
                        n += 1
                    elif data[x - 1][y][0] == "line" and data[x - 1][y][1] == "right":
                        n += 1
                elif data[x - 1][y][0] == "not" and data[x - 1][y][1] != "left":
                    n += 1
            if y + 1 in data[x] and data[x][y][1] == "up":
                if data[x][y + 1][2] == "power":
                    if data[x][y + 1][0] == "button":
                        n += 1
                    elif data[x][y + 1][0] == "line" and data[x][y + 1][1] == "up":
                        n += 1
                elif data[x][y + 1][0] == "not" and data[x][y + 1][1] != "down":
                    n += 1
            if y - 1 in data[x] and data[x][y][1] == "down":
                if data[x][y - 1][2] == "power":
                    if data[x][y - 1][0] == "button":
                        n += 1
                    elif data[x][y - 1][0] == "line" and data[x][y - 1][1] == "down":
                        n += 1
                elif data[x][y - 1][0] == "not" and data[x][y - 1][1] != "up":
                    n += 1
            if n > 0:
                data[x][y][2] = "power"
            else:
                data[x][y][2] = "unpower"
        if data[x][y][0] == "light":
            n = 0
            if x + 1 in data and y in data[x + 1]:
                if data[x + 1][y][2] == "power":
                    if data[x + 1][y][0] == "button":
                        n += 1
                    elif data[x + 1][y][0] == "line" and data[x + 1][y][1] == "left":
                        n += 1
                elif data[x + 1][y][0] == "not" and data[x + 1][y][1] != "right":
                    n += 1
            if x - 1 in data and y in data[x - 1]:
                if data[x - 1][y][2] == "power":
                    if data[x - 1][y][0] == "button":
                        n += 1
                    elif data[x - 1][y][0] == "line" and data[x - 1][y][1] == "right":
                        n += 1
                elif data[x - 1][y][0] == "not" and data[x - 1][y][1] != "left":
                    n += 1
            if y + 1 in data[x]:
                if data[x][y + 1][2] == "power":
                    if data[x][y + 1][0] == "button":
                        n += 1
                    elif data[x][y + 1][0] == "line" and data[x][y + 1][1] == "up":
                        n += 1
                elif data[x][y + 1][0] == "not" and data[x][y + 1][1] != "down":
                    n += 1
            if y - 1 in data[x]:
                if data[x][y - 1][2] == "power":
                    if data[x][y - 1][0] == "button":
                        n += 1
                    elif data[x][y - 1][0] == "line" and data[x][y - 1][1] == "down":
                        n += 1
                elif data[x][y - 1][0] == "not" and data[x][y - 1][1] != "up":
                    n += 1
            if n > 0:
                data[x][y][2] = "power"
            else:
                data[x][y][2] = "unpower"


pygame.init()
W_change = pygame.display.Info().current_w
H_change = pygame.display.Info().current_h
w, h = 1000, 700
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("模擬電路")
clock = pygame.time.Clock()
full = False
start_coordinate = 0, 0
data: dict[int, dict[int, list[str]]] = {}
# {x:{y:[type,direction,state]}}
image_link = os.path.dirname(os.path.realpath(__file__)) + "\\模擬電路圖片\\"
choose = (-1, -1)
put = False
director = "up"
next_put = "No"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(data)
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if full:
                    w, h = W_change, H_change
                    screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    full = False
                else:
                    w, h = 1000, 700
                    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
                    full = True
            elif event.key == pygame.K_UP:
                director = "up"
            elif event.key == pygame.K_RIGHT:
                director = "right"
            elif event.key == pygame.K_DOWN:
                director = "down"
            elif event.key == pygame.K_LEFT:
                director = "left"
            elif event.key == pygame.K_SPACE:
                choose = (-1, -1)
            elif event.key == pygame.K_1 and put:
                next_put = ["button", "No", "unpower"]
            elif event.key == pygame.K_2 and put:
                next_put = ["line", director, "unpower"]
            elif event.key == pygame.K_3 and put:
                next_put = ["not", director, "unpower"]
            elif event.key == pygame.K_4 and put:
                next_put = ["light", "No", "unpower"]
            elif event.key == pygame.K_5 and put:
                next_put = ["turn", director, "unpower"]
            elif event.key == pygame.K_d:
                data = {}
            else:
                next_put = "No"
            if next_put != "No" and next_put[1] != "No":
                next_put[1] = director
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            mx, my = fl(mx / 10), fl(my / 10)
            if pygame.mouse.get_pressed()[0]:
                try:
                    if data[mx][my][0] == "button":
                        if data[mx][my][2] == "unpower":
                            data[mx][my][2] = "power"
                        else:
                            data[mx][my][2] = "unpower"
                except:
                    pass
                if next_put != "No":
                    if choose[0] in data:
                        data[choose[0]][choose[1]] = next_put
                    else:
                        data[choose[0]] = {}
                        data[choose[0]][choose[1]] = next_put
                    next_put = "No"
                choose = (mx, my)
                put = True
            elif pygame.mouse.get_pressed()[2]:
                put = False
                next_put = "No"

    button: list[tuple[int, int]] = []
    for i in range(fl(w / 10)):
        for j in range(fl(h / 10)):
            if i in data and j in data[i]:
                if data[i][j][0] == "button":
                    button.append((i, j))
    for i in button:
        # update1(i[0],i[1])
        update2(i[0], i[1])

    screen.fill((0, 0, 0))
    for i in range(fl(w / 10)):
        for j in range(fl(h / 10)):
            if i in data and j in data[i]:
                if data[i][j][1] == "No":
                    screen.blit(
                        pygame.image.load(image_link + f"{data[i][j][0]}_{data[i][j][2]}.png"),
                        [i * 10, j * 10],
                    )
                else:
                    screen.blit(
                        pygame.image.load(image_link + f"{data[i][j][0]}_{data[i][j][1]}_{data[i][j][2]}.png"),
                        [i * 10, j * 10],
                    )
    if choose != (-1, -1):
        if next_put != "No":
            if next_put[1] == "No":
                screen.blit(
                    pygame.image.load(image_link + f"{next_put[0]}_{next_put[2]}.png"),
                    [choose[0] * 10, choose[1] * 10],
                )
            else:
                screen.blit(
                    pygame.image.load(image_link + f"{next_put[0]}_{next_put[1]}_{next_put[2]}.png"),
                    [choose[0] * 10, choose[1] * 10],
                )
        pygame.draw.rect(screen, (0, 0, 255), (choose[0] * 10, choose[1] * 10, 10, 10), 1)
    pygame.display.update()
    clock.tick(10)
