from typing import Callable
import pygame
from random import randint as ri


class Button:
    def __init__(self, x: int, y: int, w: int, h: int, do: Callable[..., None], args: tuple[int, ...], text: str = ""):
        self.ox = x
        self.oy = y
        self.ow = w
        self.oh = h
        self.x = self.ox
        self.y = self.oy
        self.w = self.ow
        self.h = self.oh
        self.do = do
        self.args = args
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
            self.do(*self.args)
        else:
            self.x = self.ox
            self.y = self.oy
            self.w = self.ow
            self.h = self.oh

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x - self.w / 2, self.y - self.h / 2, self.w, self.h), 0)
        text = pygame.font.Font(textlink, self.text_size).render(self.text, True, self.text_color)
        screen.blit(text, text.get_rect(center=(self.x, self.y)))


class RubiksCube:
    def __init__(
        self, rc: dict[str, tuple[int, int, int]], display_order: tuple[str, ...], l: int = 100, xs: int = 200, ys: int = 50
    ) -> None:
        self.x = [int(xs + l * i * 3**0.5) for i in (0, 0.5, 1, 1.5, 2, 2.5, 3, -0.25, 3.25)]
        self.y = [int(ys + l * i) for i in (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6)]
        self.p = (
            (self.x[3], self.y[0]),
            (self.x[2], self.y[1]),
            (self.x[4], self.y[1]),
            (self.x[1], self.y[2]),
            (self.x[3], self.y[2]),
            (self.x[5], self.y[2]),
            (self.x[0], self.y[3]),
            (self.x[2], self.y[3]),
            (self.x[4], self.y[3]),
            (self.x[6], self.y[3]),
            (self.x[1], self.y[4]),
            (self.x[3], self.y[4]),
            (self.x[5], self.y[4]),
            (self.x[2], self.y[5]),
            (self.x[4], self.y[5]),
            (self.x[3], self.y[6]),
            (self.x[0], self.y[5]),
            (self.x[1], self.y[6]),
            (self.x[2], self.y[7]),
            (self.x[3], self.y[8]),
            (self.x[4], self.y[7]),
            (self.x[5], self.y[6]),
            (self.x[6], self.y[5]),
            (self.x[0], self.y[7]),
            (self.x[1], self.y[8]),
            (self.x[2], self.y[9]),
            (self.x[3], self.y[10]),
            (self.x[4], self.y[9]),
            (self.x[5], self.y[8]),
            (self.x[6], self.y[7]),
            (self.x[0], self.y[9]),
            (self.x[1], self.y[10]),
            (self.x[2], self.y[11]),
            (self.x[3], self.y[12]),
            (self.x[4], self.y[11]),
            (self.x[5], self.y[10]),
            (self.x[6], self.y[9]),
        )
        self.display_order = display_order
        self.rc = rc
        self.rect: dict[str, tuple[int, int, int, int]] = {}
        self.rect["u0"] = (0, 1, 4, 2)
        self.rect["u1"] = (2, 4, 8, 5)
        self.rect["u2"] = (5, 8, 12, 9)
        self.rect["u3"] = (1, 3, 7, 4)
        self.rect["u4"] = (4, 7, 11, 8)
        self.rect["u5"] = (8, 11, 14, 12)
        self.rect["u6"] = (3, 6, 10, 7)
        self.rect["u7"] = (7, 10, 13, 11)
        self.rect["u8"] = (11, 13, 15, 14)
        self.rect["l0"] = (6, 16, 17, 10)
        self.rect["l1"] = (10, 17, 18, 13)
        self.rect["l2"] = (13, 18, 19, 15)
        self.rect["l3"] = (16, 23, 24, 17)
        self.rect["l4"] = (17, 24, 25, 18)
        self.rect["l5"] = (18, 25, 26, 19)
        self.rect["l6"] = (23, 30, 31, 24)
        self.rect["l7"] = (24, 31, 32, 25)
        self.rect["l8"] = (25, 32, 33, 26)
        self.rect["r0"] = (15, 19, 20, 14)
        self.rect["r1"] = (14, 20, 21, 12)
        self.rect["r2"] = (12, 21, 22, 9)
        self.rect["r3"] = (19, 26, 27, 20)
        self.rect["r4"] = (20, 27, 28, 21)
        self.rect["r5"] = (21, 28, 29, 22)
        self.rect["r6"] = (26, 33, 34, 27)
        self.rect["r7"] = (27, 34, 35, 28)
        self.rect["r8"] = (28, 35, 36, 29)
        self.rect_name_list = [
            "u0",
            "u1",
            "u2",
            "u3",
            "u4",
            "u5",
            "u6",
            "u7",
            "u8",
            "l0",
            "l1",
            "l2",
            "l3",
            "l4",
            "l5",
            "l6",
            "l7",
            "l8",
            "r0",
            "r1",
            "r2",
            "r3",
            "r4",
            "r5",
            "r6",
            "r7",
            "r8",
        ]

    def desplay(self, screen: pygame.Surface) -> None:
        for i in range(27):
            pygame.draw.polygon(screen, self.rc[self.display_order[i]], tuple(self.p[i] for i in self.rect[self.rect_name_list[i]]))
            screen.blit(
                font.render(self.rect_name_list[i], True, (0, 0, 0)), tuple(self.p[i] for i in self.rect[self.rect_name_list[i]][:2])
            )
        for i, j in (
            (0, 6),
            (0, 9),
            (1, 12),
            (3, 14),
            (2, 10),
            (5, 13),
            (6, 15),
            (9, 15),
            (6, 30),
            (15, 33),
            (9, 36),
            (30, 33),
            (33, 36),
            (10, 31),
            (13, 32),
            (14, 34),
            (12, 35),
            (16, 19),
            (23, 26),
            (19, 22),
            (26, 29),
        ):
            pygame.draw.line(screen, (0, 0, 0), self.p[i], self.p[j], 3)

    def register_button(self, button_list: list[Button]) -> None:
        p = (
            (8, 4),
            (8, 6),
            (8, 8),
            (7, 4),
            (7, 6),
            (7, 8),
            (2, 12),
            (1, 11),
            (0, 10),
            (6, 2),
            (5, 1),
            (4, 0),
            (4, 12),
            (5, 11),
            (6, 10),
            (0, 2),
            (1, 1),
            (2, 0),
        )
        for i in range(18):
            button_list.append(Button(self.x[p[i][0]], self.y[p[i][1]], 30, 20, ro, (i + 1,), str(i + 1)))
        button_list.append(Button(self.x[7] - 35, self.y[6], 30, 20, ros, (4, 5, 6)))
        button_list.append(Button(self.x[8] + 35, self.y[6], 30, 20, ros, (1, 2, 3)))
        button_list.append(Button(self.x[5] + 35, self.y[1] - 25, 30, 20, ros, (10, 11, 12)))
        button_list.append(Button(self.x[1] - 35, self.y[11] + 25, 30, 20, ros, (7, 8, 9)))
        button_list.append(Button(self.x[1] - 35, self.y[1] - 25, 30, 20, ros, (16, 17, 18)))
        button_list.append(Button(self.x[5] + 35, self.y[11] + 25, 30, 20, ros, (13, 14, 15)))


# u上d下l左r右f前b後
rc: dict[str, tuple[int, int, int]] = {}
for i in range(9):
    rc[f"u{i}"] = (255, 255, 255)  # w白
    rc[f"d{i}"] = (255, 248, 121)  # y黃
    rc[f"l{i}"] = (255, 128, 0)  # o橘
    rc[f"r{i}"] = (191, 65, 65)  # r紅
    rc[f"f{i}"] = (134, 194, 108)  # g綠
    rc[f"b{i}"] = (89, 72, 191)  # b藍


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


def mouse_turn_rc(start_pos: str, end_pos: str) -> None:
    match (start_pos, end_pos):
        case ("u0", "u2"):
            ro(15)
        case ("u2", "u0"):
            ro(18)
        case ("u3", "u5"):
            ro(14)
        case ("u5", "u3"):
            ro(17)
        case ("u6", "u8"):
            ro(13)
        case ("u8", "u6"):
            ro(16)
        case ("u0", "u6"):
            ro(9)
        case ("u6", "u0"):
            ro(12)
        case ("u1", "u7"):
            ro(8)
        case ("u7", "u1"):
            ro(11)
        case ("u2", "u8"):
            ro(7)
        case ("u8", "u2"):
            ro(10)
        case ("l0", "l2"):
            ro(1)
        case ("l2", "l0"):
            ro(4)
        case ("l3", "l5"):
            ro(2)
        case ("l5", "l3"):
            ro(5)
        case ("l6", "l8"):
            ro(3)
        case ("l8", "l6"):
            ro(6)
        case ("l0", "l6"):
            ro(9)
        case ("l6", "l0"):
            ro(12)
        case ("l1", "l7"):
            ro(8)
        case ("l7", "l1"):
            ro(11)
        case ("l2", "l8"):
            ro(7)
        case ("l8", "l2"):
            ro(10)
        case ("r0", "r2"):
            ro(1)
        case ("r2", "r0"):
            ro(4)
        case ("r3", "r5"):
            ro(2)
        case ("r5", "r3"):
            ro(5)
        case ("r6", "r8"):
            ro(3)
        case ("r8", "r6"):
            ro(6)
        case ("r0", "r6"):
            ro(13)
        case ("r6", "r0"):
            ro(16)
        case ("r1", "r7"):
            ro(14)
        case ("r7", "r1"):
            ro(17)
        case ("r2", "r8"):
            ro(15)
        case ("r8", "r2"):
            ro(18)
        case _:
            print("error: unknow key", start_pos, end_pos)


def f1() -> None:
    for _ in range(10):
        ro(ri(1, 18))


def ros(*code: int) -> None:
    for i in code:
        ro(i)


def check_mouse_pos(rects: dict[str, tuple[tuple[int, int], ...]]) -> str:
    for i in rects:
        pos = pygame.mouse.get_pos()
        A, B, C, D = rects[i]
        cp1 = (B[0] - A[0]) * (pos[1] - A[1]) - (pos[0] - A[0]) * (B[1] - A[1])
        cp2 = (C[0] - B[0]) * (pos[1] - B[1]) - (pos[0] - B[0]) * (C[1] - B[1])
        cp3 = (D[0] - C[0]) * (pos[1] - C[1]) - (pos[0] - C[0]) * (D[1] - C[1])
        cp4 = (A[0] - D[0]) * (pos[1] - D[1]) - (pos[0] - D[0]) * (A[1] - D[1])
        if (cp1 >= 0 and cp2 >= 0 and cp3 >= 0 and cp4 >= 0) or (cp1 <= 0 and cp2 <= 0 and cp3 <= 0 and cp4 <= 0):
            return i
    else:
        return ""


pygame.init()
W_change = pygame.display.Info().current_w
H_change = pygame.display.Info().current_h
W, H = 1500, 700
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("魔方")
clock = pygame.time.Clock()
textlink = "C:\\Windows\\Fonts\\kaiu.ttf"
font = pygame.font.Font(textlink, 20)
fullscreen = 0
step: list[int] = []
start_pos, end_pos = "", ""
button_list: list[Button] = []
button_list.append(Button(150, 75, 100, 40, lambda: ro(step.pop(), False) if len(step) > 0 else None, (), "回上一步"))
button_list.append(Button(75, 150, 60, 40, f1, (), "轉亂"))
rc1 = RubiksCube(
    rc,
    (
        "u0",
        "u1",
        "u2",
        "u3",
        "u4",
        "u5",
        "u6",
        "u7",
        "u8",
        "f0",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "r0",
        "r1",
        "r2",
        "r3",
        "r4",
        "r5",
        "r6",
        "r7",
        "r8",
    ),
    75,
    200,
    50,
)
rc2 = RubiksCube(
    rc,
    (
        "u8",
        "u7",
        "u6",
        "u5",
        "u4",
        "u3",
        "u2",
        "u1",
        "u0",
        "b0",
        "b1",
        "b2",
        "b3",
        "b4",
        "b5",
        "b6",
        "b7",
        "b8",
        "l0",
        "l1",
        "l2",
        "l3",
        "l4",
        "l5",
        "l6",
        "l7",
        "l8",
    ),
    75,
    800,
    50,
)
rc1.register_button(button_list)
rects: dict[str, tuple[tuple[int, int], ...]] = {}
for i in rc1.rect:
    rects[i] = tuple(rc1.p[j] for j in rc1.rect[i])


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
            start_pos = check_mouse_pos(rects)
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = check_mouse_pos(rects)
            if start_pos != "" and end_pos != "":
                mouse_turn_rc(start_pos, end_pos)
    for i in button_list:
        i.check1(mx, my)
    if not pygame.mouse.get_pressed()[0]:
        for i in button_list:
            i.check2(mx, my, False)
    screen.fill((0, 0, 0))
    rc1.desplay(screen)
    rc2.desplay(screen)
    text = font.render(f"({mx},{my}){step}", True, (255, 255, 255))
    screen.blit(text, [0, 0])
    for i in button_list:
        i.display()
    pygame.display.update()
    clock.tick(100)
