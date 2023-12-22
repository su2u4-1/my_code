import pygame


class Button:
    def __init__(self, x, y, w, h, do):
        self.ox = x
        self.oy = y
        self.ow = w
        self.oh = h
        self.x = self.ox
        self.y = self.oy
        self.w = self.ow
        self.h = self.oh
        self.do = do
        self.scaling = 0.9
        self.color1 = (100, 100, 100)
        self.color2 = (200, 200, 200)
        self.color = self.color1

    def check1(self, mx, my):
        if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
            self.color = self.color2
        else:
            self.x = self.ox
            self.y = self.oy
            self.w = self.ow
            self.h = self.oh
            self.color = self.color1

    def check2(self, mx, my, mouse):
        if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h and mouse:
            self.x = self.ox + self.ow * 0.05
            self.y = self.oy + self.oh * 0.05
            self.w = self.ow * 0.9
            self.h = self.oh * 0.9
            self.do_something()
        else:
            self.x = self.ox
            self.y = self.oy
            self.w = self.ow
            self.h = self.oh

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 0)

    def do_something(self):
        try:
            exec(self.do)
        except Exception as e:
            print(e)
            print(self.do)
            exit()


# u上d下l左r右f前b後
rc = {}
for i in range(9):
    rc[f"u{i}"] = (255, 255, 255)  # w白
    rc[f"d{i}"] = (255, 255, 0)  # y黃
    rc[f"l{i}"] = (255, 128, 0)  # o橘
    rc[f"r{i}"] = (255, 0, 0)  # r紅
    rc[f"f{i}"] = (0, 255, 0)  # g綠
    rc[f"b{i}"] = (0, 0, 255)  # b藍


def r1(s: str):  # 順
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


def r2(s: str):  # 逆
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


def r3(s1: str, s2: str, s3: str, s4: str, n1: int, n2: int, n3: int, n4: int):
    a = rc[f"{s1}{n1}"]
    rc[f"{s1}{n1}"] = rc[f"{s2}{n2}"]
    rc[f"{s2}{n2}"] = rc[f"{s3}{n3}"]
    rc[f"{s3}{n3}"] = rc[f"{s4}{n4}"]
    rc[f"{s4}{n4}"] = a


def f1l():
    for i in range(3):
        r3("f", "r", "b", "l", i, i, i, i)
    r1("u")


def f2l():
    for i in range(3, 6):
        r3("f", "r", "b", "l", i, i, i, i)


def f3l():
    for i in range(6, 9):
        r3("f", "r", "b", "l", i, i, i, i)
    r2("d")


def f1r():
    for i in range(3):
        r3("f", "l", "b", "r", i, i, i, i)
    r2("u")


def f2r():
    for i in range(3, 6):
        r3("f", "l", "b", "r", i, i, i, i)


def f3r():
    for i in range(6, 9):
        r3("f", "l", "b", "r", i, i, i, i)
    r1("d")


def l1u():
    r3("f", "d", "b", "u", 2, 2, 6, 2)
    r3("f", "d", "b", "u", 5, 5, 3, 5)
    r3("f", "d", "b", "u", 8, 8, 0, 8)
    r1("r")


def l2u():
    r3("f", "d", "b", "u", 1, 1, 7, 1)
    r3("f", "d", "b", "u", 4, 4, 4, 4)
    r3("f", "d", "b", "u", 7, 7, 1, 7)


def l3u():
    r3("f", "d", "b", "u", 0, 0, 8, 0)
    r3("f", "d", "b", "u", 3, 3, 5, 3)
    r3("f", "d", "b", "u", 6, 6, 2, 6)
    r2("l")


def l1d():
    r3("f", "u", "b", "d", 2, 2, 6, 2)
    r3("f", "u", "b", "d", 5, 5, 3, 5)
    r3("f", "u", "b", "d", 8, 8, 0, 8)
    r2("r")


def l2d():
    r3("f", "u", "b", "d", 1, 1, 7, 1)
    r3("f", "u", "b", "d", 4, 4, 4, 4)
    r3("f", "u", "b", "d", 7, 7, 1, 7)


def l3d():
    r3("f", "u", "b", "d", 0, 0, 8, 0)
    r3("f", "u", "b", "d", 3, 3, 5, 3)
    r3("f", "u", "b", "d", 6, 6, 2, 6)
    r1("l")


def r1u():
    r3("r", "d", "l", "u", 0, 2, 8, 6)
    r3("r", "d", "l", "u", 3, 1, 5, 7)
    r3("r", "d", "l", "u", 6, 0, 2, 8)
    r2("f")


def r2u():
    r3("r", "d", "l", "u", 1, 5, 7, 3)
    r3("r", "d", "l", "u", 4, 4, 4, 4)
    r3("r", "d", "l", "u", 7, 3, 1, 5)


def r3u():
    r3("r", "d", "l", "u", 2, 8, 6, 0)
    r3("r", "d", "l", "u", 5, 7, 3, 1)
    r3("r", "d", "l", "u", 8, 6, 0, 2)
    r1("b")


def r1d():
    r3("r", "u", "l", "d", 0, 6, 8, 2)
    r3("r", "u", "l", "d", 3, 7, 5, 1)
    r3("r", "u", "l", "d", 6, 8, 2, 0)
    r1("f")


def r2d():
    r3("r", "u", "l", "d", 1, 3, 7, 5)
    r3("r", "u", "l", "d", 4, 4, 4, 4)
    r3("r", "u", "l", "d", 7, 5, 1, 3)


def r3d():
    r3("r", "u", "l", "d", 2, 0, 6, 8)
    r3("r", "u", "l", "d", 5, 1, 3, 7)
    r3("r", "u", "l", "d", 8, 2, 0, 6)
    r2("b")


def rollback(a):
    match a:
        case "f1l":
            f1r()
        case "f2l":
            f2r()
        case "f3l":
            f3r()
        case "f1r":
            f1l()
        case "f2r":
            f2l()
        case "f3r":
            f3l()
        case "l1u":
            l1d()
        case "l2u":
            l2d()
        case "l3u":
            l3d()
        case "l1d":
            l1u()
        case "l2d":
            l2u()
        case "l3d":
            l3u()
        case "r1u":
            r1d()
        case "r2u":
            r2d()
        case "r3u":
            r3d()
        case "r1d":
            r1u()
        case "r2d":
            r2u()
        case "r3d":
            r3u()


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
step = []
button_list = []
button_list.append(Button(160, 240, 30, 20, "step.append('f1l')\nf1l()"))
button_list.append(Button(160, 340, 30, 20, "step.append('f2l')\nf2l()"))
button_list.append(Button(160, 440, 30, 20, "step.append('f3l')\nf3l()"))
button_list.append(Button(750, 240, 30, 20, "step.append('f1r')\nf1r()"))
button_list.append(Button(750, 340, 30, 20, "step.append('f2r')\nf2r()"))
button_list.append(Button(750, 440, 30, 20, "step.append('f3r')\nf3r()"))
button_list.append(Button(700, 150, 30, 20, "step.append('l1u')\nl1u()"))
button_list.append(Button(610, 90, 30, 20, "step.append('l2u')\nl2u()"))
button_list.append(Button(530, 50, 30, 20, "step.append('l3u')\nl3u()"))
button_list.append(Button(400, 650, 30, 20, "step.append('l1d')\nl1d()"))
button_list.append(Button(310, 600, 30, 20, "step.append('l2d')\nl2d()"))
button_list.append(Button(220, 560, 30, 20, "step.append('l3d')\nl3d()"))
button_list.append(Button(220, 140, 30, 20, "step.append('r1u')\nr1u()"))
button_list.append(Button(290, 90, 30, 20, "step.append('r2u')\nr2u()"))
button_list.append(Button(390, 50, 30, 20, "step.append('r3u')\nr3u()"))
button_list.append(Button(520, 650, 30, 20, "step.append('r1d')\nr1d()"))
button_list.append(Button(600, 600, 30, 20, "step.append('r2d')\nr2d()"))
button_list.append(Button(690, 550, 30, 20, "step.append('r3d')\nr3d()"))
button_list.append(Button(100, 100, 30, 20, "if len(step)>0:\n\trollback(step.pop())"))

while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(step)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in button_list:
                i.check2(mx, my, True)
    for i in button_list:
        i.check1(mx, my)
    if not pygame.mouse.get_pressed()[0]:
        for i in button_list:
            i.check2(mx, my, False)
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
    pygame.draw.line(screen, (0, 0, 0), p[0], p[6], 3)
    pygame.draw.line(screen, (0, 0, 0), p[0], p[9], 3)
    pygame.draw.line(screen, (0, 0, 0), p[1], p[12], 3)
    pygame.draw.line(screen, (0, 0, 0), p[3], p[14], 3)
    pygame.draw.line(screen, (0, 0, 0), p[2], p[10], 3)
    pygame.draw.line(screen, (0, 0, 0), p[5], p[13], 3)
    pygame.draw.line(screen, (0, 0, 0), p[6], p[15], 3)
    pygame.draw.line(screen, (0, 0, 0), p[9], p[15], 3)
    pygame.draw.line(screen, (0, 0, 0), p[6], p[30], 3)
    pygame.draw.line(screen, (0, 0, 0), p[15], p[33], 3)
    pygame.draw.line(screen, (0, 0, 0), p[9], p[36], 3)
    pygame.draw.line(screen, (0, 0, 0), p[30], p[33], 3)
    pygame.draw.line(screen, (0, 0, 0), p[33], p[36], 3)
    pygame.draw.line(screen, (0, 0, 0), p[10], p[31], 3)
    pygame.draw.line(screen, (0, 0, 0), p[13], p[32], 3)
    pygame.draw.line(screen, (0, 0, 0), p[14], p[34], 3)
    pygame.draw.line(screen, (0, 0, 0), p[12], p[35], 3)
    pygame.draw.line(screen, (0, 0, 0), p[16], p[19], 3)
    pygame.draw.line(screen, (0, 0, 0), p[23], p[26], 3)
    pygame.draw.line(screen, (0, 0, 0), p[19], p[22], 3)
    pygame.draw.line(screen, (0, 0, 0), p[26], p[29], 3)
    text = font.render(f"({mx},{my})", True, (255, 255, 255))
    screen.blit(text, [0, 0])
    for i in button_list:
        i.display()
    pygame.display.update()
    clock.tick(100)
