import pygame
from random import randint as ri

# u上d下l左r右f前b後
rc = {}
for i in range(9):
    rc[f"u{i}"] = (255, 255, 255)  # w白
    rc[f"d{i}"] = (255, 255, 0)  # y黃
    rc[f"l{i}"] = (255, 128, 0)  # o橘
    rc[f"r{i}"] = (255, 0, 0)  # r紅
    rc[f"f{i}"] = (0, 255, 0)  # g綠
    rc[f"b{i}"] = (0, 0, 255)  # b藍


def r1(s):  # 順
    a = rc[f"{s}0"]
    rc[f"{s}0"] = rc[f"{s}6"]
    rc[f"{s}6"] = rc[f"{s}8"]
    rc[f"{s}8"] = rc[f"{s}2"]
    rc[f"{s}2"] = a
    a = rc[f"{s}1"]
    rc[f"{s}1"] = rc[f"{s}3"]
    rc[f"{s}3"] = rc[f"{s}7"]
    rc[f"{s}7"] = rc[f"{s}5"]
    rc[f"{s}5"] = a


def r2(s):  # 逆
    a = rc[f"{s}0"]
    rc[f"{s}0"] = rc[f"{s}2"]
    rc[f"{s}2"] = rc[f"{s}8"]
    rc[f"{s}8"] = rc[f"{s}6"]
    rc[f"{s}6"] = a
    a = rc[f"{s}1"]
    rc[f"{s}1"] = rc[f"{s}5"]
    rc[f"{s}5"] = rc[f"{s}7"]
    rc[f"{s}7"] = rc[f"{s}3"]
    rc[f"{s}3"] = a


def f1l():
    for i in range(3):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = a
    r1("u")


def f2l():
    for i in range(3, 6):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = a


def f3l():
    for i in range(6, 9):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = a
    r2("d")


def f1r():
    for i in range(3):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = a
    r2("u")


def f2r():
    for i in range(3, 6):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = a


def f3r():
    for i in range(6, 9):
        a = rc[f"f{i}"]
        rc[f"f{i}"] = rc[f"l{i}"]
        rc[f"l{i}"] = rc[f"b{i}"]
        rc[f"b{i}"] = rc[f"r{i}"]
        rc[f"r{i}"] = a
    r1("u")


def l1l():
    pass


def l2l():
    pass


def l3l():
    pass


def l1r():
    pass


def l2r():
    pass


def l3r():
    pass


def r1l():
    pass


def r2l():
    pass


def r3l():
    pass


def r1r():
    pass


def r2r():
    pass


def r3r():
    pass


def ran():
    match ri(1, 18):
        case 1:
            f1l()
        case 2:
            f2l()
        case 3:
            f3l()
        case 4:
            f1r()
        case 5:
            f2r()
        case 6:
            f3r()
        case 7:
            l1l()
        case 8:
            l2l()
        case 9:
            l3l()
        case 10:
            l1r()
        case 11:
            l2r()
        case 12:
            l3r()
        case 13:
            r1l()
        case 14:
            r2l()
        case 15:
            r3l()
        case 16:
            r1r()
        case 17:
            r2r()
        case 18:
            r3r()


l = 100
xs = 200
ys = 50
x = []
y = []
for i in [0, 0.5, 1, 1.5, 2, 2.5, 3]:
    x.append(xs + l * (i * 3**0.5))
for i in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]:
    y.append(ys + l * i)
p = [
    (x[3], y[0]),
    (x[2], y[1]),
    (x[4], y[1]),
    (x[1], y[2]),
    (x[3], y[2]),
    (x[5], y[2]),
    (x[0], y[3]),
    (x[2], y[3]),
    (x[4], y[3]),
    (x[6], y[3]),
    (x[1], y[4]),
    (x[3], y[4]),
    (x[5], y[4]),
    (x[2], y[5]),
    (x[4], y[5]),
    (x[3], y[6]),
    (x[0], y[5]),
    (x[1], y[6]),
    (x[2], y[7]),
    (x[3], y[8]),
    (x[4], y[7]),
    (x[5], y[6]),
    (x[6], y[5]),
    (x[0], y[7]),
    (x[1], y[8]),
    (x[2], y[9]),
    (x[3], y[10]),
    (x[4], y[9]),
    (x[5], y[8]),
    (x[6], y[7]),
    (x[0], y[9]),
    (x[1], y[10]),
    (x[2], y[11]),
    (x[3], y[12]),
    (x[4], y[11]),
    (x[5], y[10]),
    (x[6], y[9]),
]

pygame.init()
W_change = pygame.display.Info().current_w
H_change = pygame.display.Info().current_h
W, H = 1000, 700
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("遊戲8.0")
clock = pygame.time.Clock()
textlink = "C:\\Windows\\Fonts\\kaiu.ttf"
font = pygame.font.Font(textlink, 20)
fullscreen = 0
t = 0

while True:
    t += 1
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen += 1
                if fullscreen % 2 == 1:
                    W = W_change
                    H = H_change
                    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
                else:
                    W, H = 1000, 700
                    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

    if t % 10 == 0:
        ran()

    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, rc["u0"], [p[0], p[1], p[4], p[2]])
    pygame.draw.polygon(screen, rc["u1"], [p[2], p[4], p[8], p[5]])
    pygame.draw.polygon(screen, rc["u2"], [p[5], p[8], p[12], p[9]])
    pygame.draw.polygon(screen, rc["u3"], [p[1], p[3], p[7], p[4]])
    pygame.draw.polygon(screen, rc["u4"], [p[4], p[7], p[11], p[8]])
    pygame.draw.polygon(screen, rc["u5"], [p[8], p[11], p[14], p[12]])
    pygame.draw.polygon(screen, rc["u6"], [p[3], p[6], p[10], p[7]])
    pygame.draw.polygon(screen, rc["u7"], [p[7], p[10], p[13], p[11]])
    pygame.draw.polygon(screen, rc["u8"], [p[11], p[13], p[15], p[14]])

    pygame.draw.polygon(screen, rc["f0"], [p[6], p[16], p[17], p[10]])
    pygame.draw.polygon(screen, rc["f1"], [p[10], p[17], p[18], p[13]])
    pygame.draw.polygon(screen, rc["f2"], [p[13], p[18], p[19], p[15]])
    pygame.draw.polygon(screen, rc["f3"], [p[16], p[23], p[24], p[17]])
    pygame.draw.polygon(screen, rc["f4"], [p[17], p[24], p[25], p[18]])
    pygame.draw.polygon(screen, rc["f5"], [p[18], p[25], p[26], p[19]])
    pygame.draw.polygon(screen, rc["f6"], [p[23], p[30], p[31], p[24]])
    pygame.draw.polygon(screen, rc["f7"], [p[24], p[31], p[32], p[25]])
    pygame.draw.polygon(screen, rc["f8"], [p[25], p[32], p[33], p[26]])

    pygame.draw.polygon(screen, rc["r0"], [p[15], p[19], p[20], p[14]])
    pygame.draw.polygon(screen, rc["r1"], [p[14], p[20], p[21], p[12]])
    pygame.draw.polygon(screen, rc["r2"], [p[12], p[21], p[22], p[9]])
    pygame.draw.polygon(screen, rc["r3"], [p[19], p[26], p[27], p[20]])
    pygame.draw.polygon(screen, rc["r4"], [p[20], p[27], p[28], p[21]])
    pygame.draw.polygon(screen, rc["r5"], [p[21], p[28], p[29], p[22]])
    pygame.draw.polygon(screen, rc["r6"], [p[26], p[33], p[34], p[27]])
    pygame.draw.polygon(screen, rc["r7"], [p[27], p[34], p[35], p[28]])
    pygame.draw.polygon(screen, rc["r8"], [p[28], p[35], p[36], p[29]])

    pygame.display.update()
    clock.tick(100)
