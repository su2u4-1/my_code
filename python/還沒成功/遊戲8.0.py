import pygame
from random import randint as ri
from math import floor as fl

pygame.init()
W_change = pygame.display.Info().current_w
H_change = pygame.display.Info().current_h
W, H = 1000, 700
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("遊戲8.0")
clock = pygame.time.Clock()
textlink = "C:\\Windows\\Fonts\\kaiu.ttf"
font = pygame.font.Font(textlink, 20)
b = [ri(0, 255), ri(0, 255), ri(0, 255)]
input_flag = False
fullscreen = 0
inputbox = False
do_something = None


class InputBox:
    def __init__(self, x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.range = (x, y, x + w, y + h)
        self.color = (0, 0, 100)
        self.text = text
        self.txt_surface = pygame.font.Font(textlink, 20).render(text, True, self.color)
        self.active = False

    def handle_mouse(self, x, y, sx, sy):
        if self.range[0] <= x - sx <= self.range[2] and self.range[1] <= y - sy <= self.range[3]:
            self.active = not self.active
        else:
            self.active = False
        if self.active:
            self.color = (0, 0, 200)
        else:
            self.color = (0, 0, 100)

    def handle_keydown(self, event):
        global input_text, input_flag
        if self.active:
            if event.key == pygame.K_RETURN:
                input_flag = True
                self.text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = pygame.font.Font(textlink, 20).render(self.text, True, self.color)
        input_text = self.text

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:
    def __init__(
        self,
        x,
        y,
        w,
        h,
        text,
        holddown,
        surface,
        do="print(f'button {self.text} is pressed')",
    ):
        self.original_x = x
        self.original_y = y
        self.original_w = w
        self.original_h = h
        self.x_ = self.original_x
        self.y_ = self.original_y
        self.w_ = self.original_w
        self.h_ = self.original_h
        self.text = text
        self.do_something = do
        self.scaling = 0.9
        self.text_color1 = (100, 100, 100)
        self.text_color2 = (200, 200, 200)
        self.button_color = (20, 20, 20)
        self.frame_color = (200, 200, 200)
        self.frame_ = False
        self.text_color_ = self.text_color1
        self.time = 0
        self.holddown = holddown
        self.text_size_original = 20
        self.text_size_ = self.text_size_original
        self.surface = surface

    def check(self, mx, my, start_x, start_y):
        global do_something
        if (
            start_x + self.x_ <= mx <= start_x + self.x_ + self.w_
            and start_y + self.y_ <= my <= start_y + self.y_ + self.h_
            and surface_dict[surface_list[-1]] == self.surface
        ):
            self.text_color_ = self.text_color2
            self.frame_ = True
            if pygame.mouse.get_pressed()[0] and self.time <= 10:
                self.x_ = self.original_x + self.original_w * 0.05
                self.y_ = self.original_y + self.original_h * 0.05
                self.w_ = self.original_w * 0.9
                self.h_ = self.original_h * 0.9
                self.text_size_ = 18
                if self.time <= 0:
                    if self.holddown:
                        print("直")
                        self.do(self.do_something)
                        self.time = 15
                    else:
                        do_something = (self, self.do_something)
                if not self.holddown:
                    self.time = 10
            else:
                self.x_ = self.original_x
                self.y_ = self.original_y
                self.w_ = self.original_w
                self.h_ = self.original_h
                self.text_size_ = self.text_size_original
        else:
            self.text_color_ = self.text_color1
            self.frame_ = False
            self.x_ = self.original_x
            self.y_ = self.original_y
            self.w_ = self.original_w
            self.h_ = self.original_h
            self.text_size_ = self.text_size_original

    def display(self):
        pygame.draw.rect(
            self.surface.surface,
            self.button_color,
            (self.x_, self.y_, self.w_, self.h_),
        )
        if self.frame_:
            pygame.draw.rect(
                self.surface.surface,
                self.frame_color,
                (self.x_, self.y_, self.w_, self.h_),
                5,
            )
        text = pygame.font.Font(textlink, self.text_size_).render(self.text, True, self.text_color_)
        self.surface.surface.blit(text, text.get_rect(center=(fl(self.x_ + self.w_ / 2), fl(self.y_ + self.h_ / 2))))
        if self.surface.name == "CreateCharacter":
            input_box.draw(self.surface.surface)

    def do(self, do_something):
        try:
            exec(do_something)
        except Exception as e:
            print(e)
            print(do_something)
            exit()


class Label:
    def __init__(self, x, y, w, h, text, v, surface):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.v = v
        self.surface = surface
        self.text_color = (200, 200, 200)
        self.label_color = (20, 20, 20)
        self.frame_color = (200, 200, 200)

    def display(self):
        pygame.draw.rect(self.surface.surface, self.label_color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(self.surface.surface, self.frame_color, (self.x, self.y, self.w, self.h), 5)
        text = pygame.font.Font(textlink, 20).render(self.text.format(eval(self.v)), True, self.text_color)
        self.surface.surface.blit(
            text,
            text.get_rect(center=(fl(self.x + self.w / 2), fl(self.y + self.h / 2))),
        )


class Surface:
    def __init__(self, name, w, h, object=[]):
        self.name = name
        self.w = w
        self.h = h
        self.object = object
        self.surface = pygame.Surface((w, h)).convert_alpha()

    def display(self):
        global sx, sy
        self.surface.fill((104, 104, 130, 200))
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.w, self.h), 5)
        sx, sy = W / 2 - self.w / 2, H / 2 - self.h / 2
        for i in self.object:
            if type(i) == Button:
                i.check(mx, my, sx, sy)
            i.display()
        screen.blit(self.surface, (sx, sy))


class Player:
    def __init__(self):
        self.name = "name"
        self.stamina = 0
        self.strength = 0
        self.wisdom = 0
        self.dexterity = 0
        self.vitality = 0
        self.luck = 0
        self.remaining_points = 30


def back_ground_color(w, h):
    back_ground = []
    for _ in range(fl(w / 10)):
        a = []
        for _ in range(fl(h / 10)):
            a.append((b[0], b[1], b[2]))
            b[ri(0, 2)] += ri(-1, 1)
            for i in range(3):
                b[i] = b[i] if b[i] < 255 else 255
                b[i] = b[i] if b[i] > 0 else 0
        back_ground.append(a)
    return back_ground


def add_surface(surface_name):
    f = True
    match surface_name:
        case "Start":
            surface = Surface(surface_name, 400, 240)
            surface.object.append(
                Button(
                    50,
                    50,
                    100,
                    40,
                    "開新遊戲",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')\nadd_surface('CreateCharacter')",
                )
            )
            surface.object.append(
                Button(
                    250,
                    50,
                    100,
                    40,
                    "開啟舊檔",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')",
                )
            )
            surface.object.append(
                Button(
                    50,
                    150,
                    100,
                    40,
                    "儲存遊戲",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')",
                )
            )
            surface.object.append(
                Button(
                    250,
                    150,
                    100,
                    40,
                    "離開遊戲",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')\nadd_surface('LeaveTheGameConfirmation')",
                )
            )
        case "LeaveTheGameConfirmation":
            surface = Surface(surface_name, 400, 140)
            surface.object.append(
                Button(
                    50,
                    50,
                    100,
                    40,
                    "確認",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')\npygame.quit()\nexit()",
                )
            )
            surface.object.append(
                Button(
                    250,
                    50,
                    100,
                    40,
                    "取消",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')\nremove_surface('LeaveTheGameConfirmation')",
                )
            )
        case "CreateCharacter":
            surface = Surface(surface_name, 400, 300)
            surface.object.append(
                Button(
                    50,
                    50,
                    100,
                    40,
                    "確認",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')\nplayer.name=input_text\nprint(player.name)\nadd_surface('InitialAttributes')\nremove_surface('CreateCharacter')\nremove_surface('Start')",
                )
            )
            surface.object.append(
                Button(
                    250,
                    50,
                    100,
                    40,
                    "取消",
                    False,
                    surface,
                    "print(f'button {self.text} is pressed')\nremove_surface('CreateCharacter')",
                )
            )
        case "InitialAttributes":
            surface = Surface(surface_name, 620, 440)
            surface.object.append(
                Button(
                    50,
                    50,
                    40,
                    40,
                    "-",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.stamina>0:\n\tplayer.stamina-=1\n\tplayer.remaining_points+=1",
                )
            )
            surface.object.append(
                Button(
                    240,
                    50,
                    40,
                    40,
                    "+",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.remaining_points>0:\n\tplayer.remaining_points-=1\n\tplayer.stamina+=1",
                )
            )
            surface.object.append(
                Button(
                    340,
                    50,
                    40,
                    40,
                    "-",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.strength>0:\n\tplayer.strength-=1\n\tplayer.remaining_points+=1",
                )
            )
            surface.object.append(
                Button(
                    530,
                    50,
                    40,
                    40,
                    "+",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.remaining_points>0:\n\tplayer.remaining_points-=1\n\tplayer.strength+=1",
                )
            )
            surface.object.append(
                Button(
                    50,
                    150,
                    40,
                    40,
                    "-",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.wisdom>0:\n\tplayer.wisdom-=1\n\tplayer.remaining_points+=1",
                )
            )
            surface.object.append(
                Button(
                    240,
                    150,
                    40,
                    40,
                    "+",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.remaining_points>0:\n\tplayer.remaining_points-=1\n\tplayer.wisdom+=1",
                )
            )
            surface.object.append(
                Button(
                    340,
                    150,
                    40,
                    40,
                    "-",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.dexterity>0:\n\tplayer.dexterity-=1\n\tplayer.remaining_points+=1",
                )
            )
            surface.object.append(
                Button(
                    530,
                    150,
                    40,
                    40,
                    "+",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.remaining_points>0:\n\tplayer.remaining_points-=1\n\tplayer.dexterity+=1",
                )
            )
            surface.object.append(
                Button(
                    50,
                    250,
                    40,
                    40,
                    "-",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.vitality>0:\n\tplayer.vitality-=1\n\tplayer.remaining_points+=1",
                )
            )
            surface.object.append(
                Button(
                    240,
                    250,
                    40,
                    40,
                    "+",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.remaining_points>0:\n\tplayer.remaining_points-=1\n\tplayer.vitality+=1",
                )
            )
            surface.object.append(
                Button(
                    340,
                    250,
                    40,
                    40,
                    "-",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.luck>0:\n\tplayer.luck-=1\n\tplayer.remaining_points+=1",
                )
            )
            surface.object.append(
                Button(
                    530,
                    250,
                    40,
                    40,
                    "+",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nif player.remaining_points>0:\n\tplayer.remaining_points-=1\n\tplayer.luck+=1",
                )
            )
            surface.object.append(
                Button(
                    260,
                    350,
                    100,
                    40,
                    "確認",
                    True,
                    surface,
                    "print(f'button {self.text} is pressed')\nadd_surface('Base')\nremove_surface('InitialAttributes')",
                )
            )
            surface.object.append(Label(90, 50, 150, 40, "體力:{0}", "player.stamina", surface))
            surface.object.append(Label(380, 50, 150, 40, "力量:{0}", "player.strength", surface))
            surface.object.append(Label(90, 150, 150, 40, "智慧:{0}", "player.wisdom", surface))
            surface.object.append(Label(380, 150, 150, 40, "敏捷:{0}", "player.dexterity", surface))
            surface.object.append(Label(90, 250, 150, 40, "血氣:{0}", "player.vitality", surface))
            surface.object.append(Label(380, 250, 150, 40, "運氣:{0}", "player.luck", surface))
            surface.object.append(Label(50, 350, 150, 40, "剩餘點數:{0}", "player.remaining_points", surface))
        case "Base":
            surface = Surface(surface_name, 680, 450)
            surface.object.append(
                Button(50, 50, 50, 50, "設定", False, surface, "print(f'button {self.text} is pressed')\nadd_surface('Settings')")
            )
            surface.object.append(
                Button(500, 50, 130, 50, "出門", False, surface, "print(f'button {self.text} is pressed')\nadd_surface('Map')")
            )
            surface.object.append(
                Button(500, 125, 130, 50, "角色", False, surface, "print(f'button {self.text} is pressed')\nadd_surface('Character')")
            )
            surface.object.append(
                Button(500, 200, 130, 50, "合成", False, surface, "print(f'button {self.text} is pressed')\nadd_surface('Synthesis')")
            )
            surface.object.append(
                Button(500, 275, 130, 50, "鍛造", False, surface, "print(f'button {self.text} is pressed')\nadd_surface('Forging')")
            )
            surface.object.append(
                Button(500, 350, 130, 50, "倉庫", False, surface, "print(f'button {self.text} is pressed')\nadd_surface('Warehouse')")
            )
        case "Settings":
            pass
        case _:
            print("這個功能尚未製作完成")
            f = False
    if f:
        surface_dict[surface_name] = surface
        surface_list.append(surface_name)


def remove_surface(surface_name):
    surface_list.remove(surface_name)
    del surface_dict[surface_name]


input_box = InputBox(50, 210, 300, 40, "請輸入名字")
back_ground = back_ground_color(W, H)
surface_dict = {}
surface_list = []
add_surface("Start")
player = Player()

while True:
    mx, my = pygame.mouse.get_pos()
    for j in surface_list:
        for i in surface_dict[j].object:
            if type(i) == Button and i.time > 0:
                i.time -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if inputbox:
                input_box.handle_keydown(event)
                inputbox = False
            if event.key == pygame.K_F11:
                fullscreen += 1
                if fullscreen % 2 == 1:
                    W = W_change
                    H = H_change
                    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
                    back_ground = back_ground_color(W, H)
                else:
                    W, H = 1000, 700
                    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
                    back_ground = back_ground_color(W, H)
        elif event.type == pygame.MOUSEBUTTONUP:
            if inputbox:
                input_box.handle_mouse(mx, my, sx, sy)
                inputbox = False
                sx, sy = 0, 0
            if do_something is not None:
                do_something[0].do(do_something[1])
                do_something = None

    screen.fill((0, 0, 0))
    for x in range(fl(W / 10)):
        for y in range(fl(H / 10)):
            pygame.draw.rect(screen, back_ground[x][y], (x * 10, y * 10, 10, 10), 0)
    screen.blit(font.render(f"{mx},{my}", True, (0, 0, 0)), [0, 0])

    for i in surface_list:
        surface_dict[i].display()
        if surface_list[-1] == "CreateCharacter":
            inputbox = True
            if input_flag:
                player.name = input_text
                print(player.name)
                add_surface("InitialAttributes")
                remove_surface("CreateCharacter")
                remove_surface("Start")
    pygame.display.update()
    clock.tick(100)
