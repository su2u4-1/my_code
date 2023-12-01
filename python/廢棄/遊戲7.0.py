from random import randint as ri
from math import floor
import pygame, sys, time


def back_ground_color(w, h):
    global back_ground
    back_ground = []
    for _ in range(floor(w / 10)):
        a = []
        for _ in range(floor(h / 10)):
            a.append((b[0], b[1], b[2]))
            b[ri(0, 2)] += ri(-1, 1)
            for i in range(3):
                b[i] = (255, b[i])[b[i] < 255]
                b[i] = (0, b[i])[b[i] > 0]
        back_ground.append(a)


input_text = ""
input_flag = False
textlink = "C:\\Windows\\Fonts\\kaiu.ttf"


class InputBox:
    def __init__(self, x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.range = (x, y, x + w, y + h)
        self.color = (0, 0, 100)
        self.text = text
        self.txt_surface = pygame.font.Font(textlink, 20).render(text, True, self.color)
        self.active = False

    def handle_mouse(self, x, y, sx, sy):
        # If the user clicked on the input_box rect.
        if self.range[0] <= x - sx <= self.range[2] and self.range[1] <= y - sy <= self.range[3]:
            # Toggle the active variable.
            self.active = not self.active
        else:
            self.active = False
        # Change the current color of the input box.
        self.color = (0, 0, 200) if self.active else (0, 0, 100)

    def handle_keydown(self, event):
        global input_text, input_flag
        if self.active:
            if event.key == pygame.K_RETURN:
                input_text = self.text
                input_flag = True
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            # Re-render the text.
            self.txt_surface = pygame.font.Font(textlink, 20).render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


def set_():
    global button_size_original, button_size_change, text_color_original, text_color_change, text_size_original, text_size_change, text_center, button_color, frame_color, txt_content, Button_range, label_frame_color, label_color, label_size, label_text_center, label_text_size, Sl
    button_size_original = [
        (50, 50, 100, 40),
        (250, 50, 100, 40),
        (50, 150, 100, 40),
        (250, 150, 100, 40),
        (50, 50, 100, 40),
        (250, 50, 100, 40),
        (50, 50, 100, 40),
        (250, 50, 100, 40),
        (50, 50, 40, 40),
        (240, 50, 40, 40),
        (340, 50, 40, 40),
        (530, 50, 40, 40),
        (50, 150, 40, 40),
        (240, 150, 40, 40),
        (340, 150, 40, 40),
        (530, 150, 40, 40),
        (50, 250, 40, 40),
        (240, 250, 40, 40),
        (340, 250, 40, 40),
        (530, 250, 40, 40),
        (260, 350, 100, 40),
        (50, 50, 50, 50),
        (500, 50, 130, 50),
        (500, 125, 130, 50),
        (500, 200, 130, 50),
        (500, 275, 130, 50),
        (500, 350, 130, 50),
    ]
    button_size_change = [
        (55, 52, 90, 36),
        (255, 52, 90, 36),
        (55, 152, 90, 36),
        (255, 152, 90, 36),
        (55, 52, 90, 36),
        (255, 52, 90, 36),
        (55, 52, 90, 36),
        (255, 52, 90, 36),
        (52, 52, 36, 36),
        (242, 52, 36, 36),
        (342, 52, 36, 36),
        (532, 52, 36, 36),
        (52, 152, 36, 36),
        (242, 152, 36, 36),
        (342, 152, 36, 36),
        (532, 152, 36, 36),
        (52, 252, 36, 36),
        (242, 252, 36, 36),
        (342, 252, 36, 36),
        (532, 252, 36, 36),
        (265, 352, 90, 36),
        (53, 53, 45, 45),
        (507, 53, 117, 45),
        (507, 123, 117, 45),
        (507, 203, 117, 45),
        (507, 273, 117, 45),
        (507, 353, 117, 45),
    ]
    text_color_original = (100, 100, 100)
    text_color_change = (200, 200, 200)
    text_size_original = 20
    text_size_change = 18
    text_center = [
        (95, 68),
        (295, 68),
        (96, 168),
        (301, 168),
        (95, 68),
        (295, 68),
        (95, 68),
        (295, 68),
        (68, 68),
        (258, 68),
        (358, 68),
        (548, 68),
        (68, 168),
        (258, 168),
        (358, 168),
        (548, 168),
        (68, 268),
        (258, 268),
        (358, 268),
        (548, 268),
        (305, 368),
        (75, 75),
        (559, 73),
        (559, 148),
        (559, 223),
        (559, 293),
        (559, 373),
    ]
    button_color = (20, 20, 20)
    frame_color = (200, 200, 200)
    txt_content = [
        "開新遊戲",
        "開啟舊檔",
        "儲存遊戲",
        "離開遊戲",
        "確認",
        "取消",
        "確認",
        "取消",
        "-",
        "+",
        "-",
        "+",
        "-",
        "+",
        "-",
        "+",
        "-",
        "+",
        "-",
        "+",
        "確認",
        "設定",
        "出門",
        "角色",
        "合成",
        "鍛造",
        "倉庫",
    ]
    Button_range = [
        [-150, -50, -70, -30],
        [50, 150, -70, -30],
        [-150, -50, 30, 70],
        [50, 150, 30, 70],
        [-150, -50, -20, 20],
        [50, 150, -20, 20],
        [-150, -50, -100, -60],
        [50, 150, -100, -60],
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
    label_text_size = 20
    Sl = ["Start"]


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
input_box = InputBox(50, 210, 300, 40, "請輸入名字")
b = [ri(0, 255), ri(0, 255), ri(0, 255)]
back_ground_color(W, H)


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
        if (W / 2) + Button_range[i][0] <= mx <= (W / 2) + Button_range[i][1] and (H / 2) + Button_range[i][2] <= my <= (
            H / 2
        ) + Button_range[i][3]:
            text_color = text_color_change
            if pygame.mouse.get_pressed()[0]:
                if Sl[-1] == "Start":
                    button_size = button_size_change[i]
                    text_size = text_size_change
                    if i == 0:
                        Sl.append("CreateCharacter")
                    elif i == 1:
                        pass
                    elif i == 2:
                        pass
                    elif i == 3:
                        Sl.append("LeaveTheGameConfirmation")
                elif Sl[-1] == "LeaveTheGameConfirmation":
                    button_size = button_size_change[i]
                    text_size = text_size_change
                    if i == 4:
                        pygame.quit()
                        sys.exit()
                    elif i == 5:
                        Sl.remove("LeaveTheGameConfirmation")
                        return
                elif Sl[-1] == "CreateCharacter":
                    button_size = button_size_change[i]
                    text_size = text_size_change
                    if i == 6:
                        player = Player(input_text)
                        Sl.remove("CreateCharacter")
                        Sl.append("InitialAttributes")
                        Sl.remove("Start")
                        return
                    elif i == 7:
                        Sl.remove("CreateCharacter")
                        return
                elif Sl[-1] == "InitialAttributes":
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
        if Sl[-1] == "CreateCharacter":
            if input_flag:
                player = Player(input_text)
                Sl.remove("CreateCharacter")
                Sl.remove("Start")
                Sl.append("InitialAttributes")
                input_flag = False
                return
            input_box.draw(Surface)
        txt = pygame.font.Font(textlink, text_size).render(txt_content[i], True, text_color)
        Surface.blit(txt, txt.get_rect(center=text_center[i]))
    if Sl[-1] == "InitialAttributes":
        for i in range(other[0], other[1] + 1):
            pygame.draw.rect(Surface, label_color, label_size[i], 0)
            pygame.draw.rect(Surface, label_frame_color, label_size[i], 3)
            txt = pygame.font.Font(textlink, label_text_size).render(label_text[i], True, label_frame_color)
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
        elif i == "Start":
            start = pygame.Surface((400, 240))
            CreateSurface(start, (400, 240), (0, 3), None)
        elif i == "LeaveTheGameConfirmation":
            leavethegameconfirmation = pygame.Surface((400, 140))
            CreateSurface(leavethegameconfirmation, (400, 140), (4, 5), None)
        elif i == "CreateCharacter":
            createcharacter = pygame.Surface((400, 300))
            CreateSurface(createcharacter, (400, 300), (6, 7), None)
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

"""
遮罩:Mask
開始:Start
建角色:CreateCharacter
初始屬性:InitialAttributes
基地:Base
倉庫:Warehouse
合成:Synthesis
角色:Character
地圖:Map
設定:Settings
背包:Inventory
訓練:Training
屬性:Attributes
技能:Skills
裝備介面:EquipmentInterface
物品介面:ItemInterface
合成介面:SynthesisInterface
怪物:Monsters
資源:Resources
強化:Enhancement
附魔:Enchantment
鑲嵌:Socketing
鍛造:Forging
離開遊戲確認:LeaveTheGameConfirmation
"""
