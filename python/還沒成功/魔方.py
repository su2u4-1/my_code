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


def r1(s:str):  # 順
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


def r2(s:str):  # 逆
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


def r3(s1:str,s2:str,s3:str,s4:str,n:list):
    for i in n:
        a = rc[f'{s1}{i}']
        rc[f'{s1}{i}'] = rc[f'{s2}{i}']
        rc[f'{s2}{i}'] = rc[f'{s3}{i}']
        rc[f'{s3}{i}'] = rc[f'{s4}{i}']
        rc[f'{s4}{i}'] = a


def f1l():
    r3('f','r','b','l',[0,1,2])
    r1("u")


def f2l():
    r3('f','r','b','l',[3,4,5])


def f3l():
    r3('f','r','b','l',[6,7,8])
    r2("d")


def f1r():
    r3('f','l','b','r',[0,1,2])
    r2("u")


def f2r():
    r3('f','l','b','r',[3,4,5])


def f3r():
    r3('f','l','b','r',[6,7,8])
    r1("u")


def l1u():
    r3('f','d','b','u',[2,5,8])
    r1('r')


def l2u():
    r3('f','d','b','u',[1,4,7])


def l3u():
    r3('f','d','b','u',[0,3,6])
    r2('l')


def l1d():
    r3('f','u','b','d',[2,5,8])
    r2('r')


def l2d():
    r3('f','u','b','d',[1,4,7])


def l3d():
    r3('f','u','b','d',[0,3,6])
    r1('l')


def r1u():
    r3('r','d','l','u',[0,3,6])
    r2('f')


def r2u():
    r3('r','d','l','u',[1,4,7])


def r3u():
    r3('r','d','l','u',[2,5,8])
    r1('b')


def r1d():
    r3('r','u','l','d',[0,3,6])
    r1('f')


def r2d():
    r3('r','u','l','d',[1,4,7])


def r3d():
    r3('r','u','l','d',[2,5,8])
    r2('b')


def ran():
    global i
    i += 1
    match i:
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
            l1u()
        case 8:
            l2u()
        case 9:
            l3u()
        case 10:
            l1d()
        case 11:
            l2d()
        case 12:
            l3d()
        case 13:
            r1u()
        case 14:
            r2u()
        case 15:
            r3u()
        case 16:
            r1d()
        case 17:
            r2d()
        case 18:
            r3d()


i = 0
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

    if t % 100 == 0:
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

    pygame.draw.line(screen,(0,0,0),p[0],p[6],3)
    pygame.draw.line(screen,(0,0,0),p[0],p[9],3)
    pygame.draw.line(screen,(0,0,0),p[1],p[12],3)
    pygame.draw.line(screen,(0,0,0),p[3],p[14],3)
    pygame.draw.line(screen,(0,0,0),p[2],p[10],3)
    pygame.draw.line(screen,(0,0,0),p[5],p[13],3)
    pygame.draw.line(screen,(0,0,0),p[6],p[15],3)
    pygame.draw.line(screen,(0,0,0),p[9],p[15],3)
    pygame.draw.line(screen,(0,0,0),p[6],p[30],3)
    pygame.draw.line(screen,(0,0,0),p[15],p[33],3)
    pygame.draw.line(screen,(0,0,0),p[9],p[36],3)
    pygame.draw.line(screen,(0,0,0),p[30],p[33],3)
    pygame.draw.line(screen,(0,0,0),p[33],p[36],3)
    pygame.draw.line(screen,(0,0,0),p[10],p[31],3)
    pygame.draw.line(screen,(0,0,0),p[13],p[32],3)
    pygame.draw.line(screen,(0,0,0),p[14],p[34],3)
    pygame.draw.line(screen,(0,0,0),p[12],p[35],3)
    pygame.draw.line(screen,(0,0,0),p[16],p[19],3)
    pygame.draw.line(screen,(0,0,0),p[23],p[26],3)
    pygame.draw.line(screen,(0,0,0),p[19],p[22],3)
    pygame.draw.line(screen,(0,0,0),p[26],p[29],3)

    pygame.display.update()
    clock.tick(100)
