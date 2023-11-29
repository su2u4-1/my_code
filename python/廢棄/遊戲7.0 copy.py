from random import randint as ri
from math import floor
import pygame, sys, time


def set_():
    global button_size_original, button_size_change, text_color_original, text_color_change, text_size_original, text_size_change, text_center, button_color, frame_color, txt_content, Button_range, label_frame_color, label_color, label_size, label_text_center, label_text_size, Sl
    button_size_original = [
        (50, 50, 50, 50),
        (500, 50, 130, 50),
        (500, 125, 130, 50),
        (500, 200, 130, 50),
        (500, 275, 130, 50),
        (500, 350, 130, 50),
    ]
    txt_content = [
        "設定",
        "出門",
        "角色",
        "合成",
        "鍛造",
        "倉庫",
    ]
    Button_range = [
        [-260, -220, -170, -130],
        [-70, -30, -170, -130],
        [30, 70, -170, -130],
        [220, 260, -170, -130],
        [-260, -220, -70, -30],
        [-70, -30, -70, -30],
        [30, 70, -70, -30],
        [220, 260, -70, -30],
        [-260, -220, 30, 70],
        [-70, -30, 30, 70],
        [30, 70, 30, 70],
        [220, 260, 30, 70],
        [-50, 50, 130, 170],
        [-290, -240, -175, -125],
        [160, 290, -175, -125],
        [160, 290, -100, -50],
        [160, 290, -25, 25],
        [160, 290, 50, 100],
        [160, 290, 125, 175],
    ]
    label_frame_color = (200, 200, 200)
    label_color = (20, 20, 20)
    label_size = [
        (90, 50, 150, 40),
        (380, 50, 150, 40),
        (90, 150, 150, 40),
        (380, 150, 150, 40),
        (90, 250, 150, 40),
        (380, 250, 150, 40),
        (50, 350, 150, 40),
    ]
    label_text_center = [
        (165, 70),
        (455, 70),
        (165, 170),
        (455, 170),
        (165, 270),
        (455, 270),
        (125, 370),
    ]


set_()
pygame.init()
W_change = pygame.display.Info().current_w
H_change = pygame.display.Info().current_h
W, H = 1000, 700
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("name")
clock = pygame.time.Clock()
f1, f2 = 0, 0
f0 = True
inputbox = False
remainingpoints = 30
b = [ri(0, 255), ri(0, 255), ri(0, 255)]


class Player:
    def __init__(self, name):
        self.name = name
        self.physicalstrength = 0
        self.power = 0
        self.wisdom = 0
        self.agility = 0
        self.vitality = 0
        self.luck = 0


def CreateSurface(Surface, Size, ButtonRange, other):
    global sx, sy, player, inputbox, f0, input_flag, remainingpoints
    if Sl[-1] == "CreateCharacter":
        sx, sy = W / 2 - Size[0] / 2, H / 2 - Size[1] / 2
        inputbox = True
    elif Sl[-1] == "InitialAttributes":
        label_text = [
            f"體力:{player.physicalstrength}",
            f"力量{player.power}",
            f"智慧:{player.wisdom}",
            f"敏捷:{player.agility}",
            f"血氣:{player.vitality}",
            f"運氣:{player.luck}",
            f"剩餘點數:{remainingpoints}",
        ]
    Surface = Surface.convert_alpha()
    Surface.fill((104, 104, 130, 200))
    pygame.draw.rect(Surface, (0, 0, 0), (0, 0, Size[0], Size[1]), 5)
    for i in range(ButtonRange[0], ButtonRange[1] + 1):
        if f0:
            button_size = button_size_original[i]
            text_size = text_size_original
            f0 = False
        if (W / 2) + Button_range[i][0] <= mx <= (W / 2) + Button_range[i][1] and (
            H / 2
        ) + Button_range[i][2] <= my <= (H / 2) + Button_range[i][3]:
            text_color = text_color_change
            if pygame.mouse.get_pressed()[0]:
                if Sl[-1] == "InitialAttributes":
                    button_size = button_size_change[i]
                    text_size = text_size_change
                    if i == 8:
                        if player.physicalstrength > 0:
                            player.physicalstrength -= 1
                            remainingpoints += 1
                    elif i == 9:
                        if remainingpoints > 0:
                            remainingpoints -= 1
                            player.physicalstrength += 1
                    elif i == 10:
                        if player.power > 0:
                            player.power -= 1
                            remainingpoints += 1
                    elif i == 11:
                        if remainingpoints > 0:
                            remainingpoints -= 1
                            player.power += 1
                    elif i == 12:
                        if player.wisdom > 0:
                            player.wisdom -= 1
                            remainingpoints += 1
                    elif i == 13:
                        if remainingpoints > 0:
                            remainingpoints -= 1
                            player.wisdom += 1
                    elif i == 14:
                        if player.agility > 0:
                            player.agility -= 1
                            remainingpoints += 1
                    elif i == 15:
                        if remainingpoints > 0:
                            remainingpoints -= 1
                            player.agility += 1
                    elif i == 16:
                        if player.vitality > 0:
                            player.vitality -= 1
                            remainingpoints += 1
                    elif i == 17:
                        if remainingpoints > 0:
                            remainingpoints -= 1
                            player.vitality += 1
                    elif i == 18:
                        if player.luck > 0:
                            player.luck -= 1
                            remainingpoints += 1
                    elif i == 19:
                        if remainingpoints > 0:
                            remainingpoints -= 1
                            player.luck += 1
                    elif i == 20:
                        Sl.remove("InitialAttributes")
                        Sl.append("Base")
                        return
                elif Sl[-1] == "Base":
                    button_size = button_size_change[i]
                    text_size = text_size_change
                    if i == 21:
                        pass
                    elif i == 22:
                        pass
                    elif i == 23:
                        pass
                    elif i == 24:
                        pass
                    elif i == 25:
                        pass
                    elif i == 26:
                        pass
                else:
                    button_size = button_size_original[i]
                    text_size = text_size_original
            else:
                button_size = button_size_original[i]
                text_size = text_size_original
            pygame.draw.rect(Surface, button_color, button_size, 0)
            pygame.draw.rect(Surface, frame_color, button_size, 3)
        else:
            text_color = text_color_original
            button_size = button_size_original[i]
            text_size = text_size_original
            pygame.draw.rect(Surface, button_color, button_size, 0)
        txt = pygame.font.Font(textlink, text_size).render(
            txt_content[i], True, text_color
        )
        Surface.blit(txt, txt.get_rect(center=text_center[i]))
    if Sl[-1] == "InitialAttributes":
        for i in range(other[0], other[1] + 1):
            pygame.draw.rect(Surface, label_color, label_size[i], 0)
            pygame.draw.rect(Surface, label_frame_color, label_size[i], 3)
            txt = pygame.font.Font(textlink, label_text_size).render(
                label_text[i], True, label_frame_color
            )
            Surface.blit(txt, txt.get_rect(center=label_text_center[i]))
    screen.blit(Surface, (W / 2 - Size[0] / 2, H / 2 - Size[1] / 2))


while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if inputbox:
                input_box.handle_keydown(event)
                inputbox = False
            if event.key == pygame.K_F11:
                f1 += 1
                if f1 % 2 == 1:
                    W = W_change
                    H = H_change
                    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
                    back_ground_color(W, H)
                else:
                    W, H = 1000, 700
                    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
                    back_ground_color(W, H)
            elif event.key == pygame.K_SPACE:
                f2 += 1
                if f2 % 2 == 1:
                    Sl.append("Mask")
                else:
                    Sl.remove("Mask")
        elif event.type == pygame.MOUSEBUTTONUP:
            if inputbox:
                input_box.handle_mouse(mx, my, sx, sy)
                inputbox = False
                sx, sy = 0, 0

    t = time.localtime(time.time())
    screen.fill((0, 0, 0))
    for x in range(floor(W / 10)):
        for y in range(floor(H / 10)):
            pygame.draw.rect(screen, back_ground[x][y], (x * 10, y * 10, 10, 10), 0)

    for i in Sl:
        if i == "Mask":
            mask = pygame.Surface(screen.get_size())
            mask = mask.convert_alpha()
            mask.fill((0, 0, 0, 100))
            screen.blit(mask, (0, 0))
        elif i == "InitialAttributes":
            initialattributes = pygame.Surface((620, 440))
            CreateSurface(initialattributes, (620, 440), (8, 20), (0, 6))
        elif i == "Base":
            base = pygame.Surface((680, 450))
            CreateSurface(base, (680, 450), (21, 26), None)

    txt_time = pygame.font.Font(textlink, 22).render(
        f"時間:{t.tm_year}/{t.tm_mon}/{t.tm_mday} {t.tm_hour}:{t.tm_min}:{t.tm_sec},滑鼠xy:{mx},{my}",
        True,
        (255, 0, 0),
    )
    screen.blit(txt_time, [0, 0])
    pygame.display.update()
    clock.tick(10)
