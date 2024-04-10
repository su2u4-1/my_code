import pygame
from random import choice, randint
from math import floor
import matplotlib.pyplot as plt


# Perlin 最初提出的数组
SEQ = [
  151,160,137,91,90,15,
  131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
  190,6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
  88,237,149,56,87,174,20,125,136,171,168,68,175,74,165,71,134,139,48,27,166,
  77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
  102,143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,196,
  135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,250,124,123,
  5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
  223,183,170,213,119,248,152,2,44,154,163,70,221,153,101,155,167,43,172,9,
  129,22,39,253,19,98,108,110,79,113,224,232,178,185,112,104,218,246,97,228,
  251,34,242,193,238,210,144,12,191,179,162,241,81,51,145,235,249,14,239,107,
  49,192,214,31,181,199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,
  138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
W, H = 800, 600


def drawplot(p):
    t = [i for i in range(len(p))]
    plt.plot(t, p, color=(0, 0, 0))
    plt.xlim(0, len(t))
    plt.ylim(min(p), max(p))
    plt.legend()
    plt.show()


def draw(d, name="windows"):
    pygame.init()
    pygame.display.set_caption(name)
    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

    while True:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        m = 255 / (mx - mi)

        screen.fill((0, 0, 0))
        for i in range(W):
            for j in range(H):
                #pygame.draw.rect(screen, (m * (d[i][j] - mi), m * (d[i][j] - mi), m * (d[i][j] - mi)), (i * 10, j * 10, 10, 10))
                screen.set_at((i, j), (m * (d[i][j] - mi), m * (d[i][j] - mi), m * (d[i][j] - mi)))

        text = font.render(f"{x},{y},{d[x // 10][y // 10]}", True, (0, 255, 0))
        screen.blit(text, (0, 0))

        pygame.display.update()
        clock.tick()


# 插值函数
def _blending(t):
    return t ** 3 * (10 + t * (6 * t - 15))  # 6t^5 -15t^4 + 10t^3


def noise(pos):
    if pos % 1 == 0:                                     #对于整数点，直接从数列中取得数值即可。
        return SEQ[int(pos % 255)]
    else:                                                #对于非整数的点，由左右的整数进行插值运算得出数值。
        x0, x1 = floor(pos) % 255, floor(pos + 1) % 255  #取得非整数点旁的两个整数。
        c0, c1 = SEQ[x0], SEQ[x1]                        #从数列中取得两个整数点的数值。
        t = pos % 255 - x0                               #计算非整数点离左边整数点的距离。
        return c0 * _blending(1 - t) + c1 * _blending(t) #使用插值函数计算非整数点的数值并输出。


mc = [[noise(i / 131) + noise(j / 131) for j in range(H)] for i in range(W)]
t1 = [max(i) for i in mc]
t2 = [min(i) for i in mc]
mx = max(t1)
mi = min(t2)
draw(mc, "c1")

#p = [noise(i / 73) for i in range(800)]
#drawplot(p)