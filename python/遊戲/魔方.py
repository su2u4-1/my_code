from typing import Callable
import pygame
from random import randint as ri


class Button:
    def __init__(self, x: int, y: int, w: int, h: int, do: Callable[..., None], text: str = ""):
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
        self.text = text
        self.text_size = 20
        self.text_color = (20, 20, 20)

    def check1(self, mx: int, my: int):
        if self.x - self.w / 2 <= mx <= self.x + self.w / 2 and self.y - self.h / 2 <= my <= self.y + self.h / 2:
            self.color = self.color2
        else:
            self.x = self.ox
            self.y = self.oy
            self.w = self.ow
            self.h = self.oh
            self.color = self.color1

    def check2(self, mx: int, my: int, mouse: int):
        if self.x - self.w / 2 <= mx <= self.x + self.w / 2 and self.y - self.h / 2 <= my <= self.y + self.h / 2 and mouse:
            self.x = self.ox + self.ow * 0.05
            self.y = self.oy + self.oh * 0.05
            self.w = self.ow * 0.9
            self.h = self.oh * 0.9
            self.do()
        else:
            self.x = self.ox
            self.y = self.oy
            self.w = self.ow
            self.h = self.oh

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x - self.w / 2, self.y - self.h / 2, self.w, self.h), 0)
        text = pygame.font.Font(textlink, self.text_size).render(self.text, True, self.text_color)
        screen.blit(text, text.get_rect(center=(self.x, self.y)))


# u上d下l左r右f前b後
rc: dict[str, tuple[int, int, int]] = {}
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


def ro(n: int, f: bool = True) -> None:
    match n:
        case 1:
            if f:
                step.append(4)
            f1r()
        case 2:
            if f:
                step.append(5)
            f2r()
        case 3:
            if f:
                step.append(6)
            f3r()
        case 4:
            if f:
                step.append(1)
            f1l()
        case 5:
            if f:
                step.append(2)
            f2l()
        case 6:
            if f:
                step.append(3)
            f3l()
        case 7:
            if f:
                step.append(10)
            l1d()
        case 8:
            if f:
                step.append(11)
            l2d()
        case 9:
            if f:
                step.append(12)
            l3d()
        case 10:
            if f:
                step.append(7)
            l1u()
        case 11:
            if f:
                step.append(8)
            l2u()
        case 12:
            if f:
                step.append(9)
            l3u()
        case 13:
            if f:
                step.append(16)
            r1d()
        case 14:
            if f:
                step.append(17)
            r2d()
        case 15:
            if f:
                step.append(18)
            r3d()
        case 16:
            if f:
                step.append(13)
            r1u()
        case 17:
            if f:
                step.append(14)
            r2u()
        case 18:
            if f:
                step.append(15)
            r3u()
        case _:
            print("error: unknow key", n)


l = 100
xs = 200
ys = 50
x = [int(xs + l * i * 3**0.5) for i in (0, 0.5, 1, 1.5, 2, 2.5, 3, -0.25, 3.25)]
y = [int(ys + l * i) for i in (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6)]
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
step: list[int] = []
button_list: list[Button] = []


def f1() -> None:
    for _ in range(10):
        ro(ri(1, 18))


def ros(*code: int) -> None:
    for i in code:
        ro(i)


button_list.append(Button(x[7], y[4], 30, 20, lambda: ro(4)))
button_list.append(Button(x[7], y[6], 30, 20, lambda: ro(5)))
button_list.append(Button(x[7], y[8], 30, 20, lambda: ro(6)))
button_list.append(Button(x[8], y[4], 30, 20, lambda: ro(1)))
button_list.append(Button(x[8], y[6], 30, 20, lambda: ro(2)))
button_list.append(Button(x[8], y[8], 30, 20, lambda: ro(3)))
button_list.append(Button(x[6], y[2], 30, 20, lambda: ro(10)))
button_list.append(Button(x[5], y[1], 30, 20, lambda: ro(11)))
button_list.append(Button(x[4], y[0], 30, 20, lambda: ro(12)))
button_list.append(Button(x[2], y[12], 30, 20, lambda: ro(7)))
button_list.append(Button(x[1], y[11], 30, 20, lambda: ro(8)))
button_list.append(Button(x[0], y[10], 30, 20, lambda: ro(9)))
button_list.append(Button(x[0], y[2], 30, 20, lambda: ro(16)))
button_list.append(Button(x[1], y[1], 30, 20, lambda: ro(17)))
button_list.append(Button(x[2], y[0], 30, 20, lambda: ro(18)))
button_list.append(Button(x[4], y[12], 30, 20, lambda: ro(13)))
button_list.append(Button(x[5], y[11], 30, 20, lambda: ro(14)))
button_list.append(Button(x[6], y[10], 30, 20, lambda: ro(15)))

button_list.append(Button(150, 75, 100, 40, lambda: ro(step.pop(), False) if len(step) > 0 else None, "回上一步"))
button_list.append(Button(75, 150, 60, 40, f1, "轉亂"))

button_list.append(Button(x[7] - 35, y[6], 30, 20, (lambda: ros(4, 5, 6))))
button_list.append(Button(x[8] + 35, y[6], 30, 20, (lambda: ros(1, 2, 3))))
button_list.append(Button(x[5] + 35, y[1] - 25, 30, 20, (lambda: ros(10, 11, 12))))
button_list.append(Button(x[1] - 35, y[11] + 25, 30, 20, (lambda: ros(7, 8, 9))))
button_list.append(Button(x[1] - 35, y[1] - 25, 30, 20, (lambda: ros(16, 17, 18))))
button_list.append(Button(x[5] + 35, y[11] + 25, 30, 20, (lambda: ros(13, 14, 15))))

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
                    screen = pygame.display.set_mode((W_change, H_change), pygame.FULLSCREEN)
                else:
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
    text = font.render(f"({mx},{my}){step}", True, (255, 255, 255))
    screen.blit(text, [0, 0])
    for i in button_list:
        i.display()
    pygame.display.update()
    clock.tick(100)
