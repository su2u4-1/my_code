import pygame as pg
from math import cos, sin, pi, floor
from time import sleep
import os

pg.init()

# 設定視窗
width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("game")

# 建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))
on_off = pg.image.load(os.path.join("./", "on-off.png"))
bg.blit(on_off, (295, 215))


# 繪製幾何圖形
def draw(size):
    long = size
    five = [
        (320, 240 + long),
        (320 + (long * cos(pi / 10)), 240 + (long * sin(pi / 10))),
        (320 + (long * cos(3 * pi / 10)), 240 + (-long * sin(3 * pi / 10))),
        (320 + (-long * cos(3 * pi / 10)), 240 + (-long * sin(3 * pi / 10))),
        (320 + (-long * cos(pi / 10)), 240 + (long * sin(pi / 10))),
    ]  # 五邊形座標
    pg.draw.polygon(bg, (0, 0, 0), five, floor(size / 30))
    pg.draw.circle(bg, (255, 255, 0), five[0], floor(size / 3), 0)  # 黃
    pg.draw.circle(bg, (255, 0, 0), five[1], floor(size / 3), 0)  # 紅
    pg.draw.circle(bg, (0, 255, 0), five[2], floor(size / 3), 0)  # 綠
    pg.draw.circle(bg, (0, 0, 0), five[3], floor(size / 3), 0)  # 黑
    pg.draw.circle(bg, (255, 255, 255), five[4], floor(size / 3), 0)  # 白
    # 黑框
    pg.draw.circle(bg, (0, 0, 0), five[0], floor(size / 3), floor(size / 75))
    pg.draw.circle(bg, (0, 0, 0), five[1], floor(size / 3), floor(size / 75))
    pg.draw.circle(bg, (0, 0, 0), five[2], floor(size / 3), floor(size / 75))
    pg.draw.circle(bg, (0, 0, 0), five[4], floor(size / 3), floor(size / 75))
    # 顯示
    screen.blit(bg, (0, 0))
    pg.display.update()


draw(150)
running = True
buttons = pg.mouse.get_pressed()
if buttons[0]:
    xy = pg.mouse.get_pos()
    x = xy[0]
    y = xy[1]
    if 275 < x < 320 and 190 < y < 240:
        draw(100)
    else:
        draw(150)
    print(xy)

# 關閉程式的程式碼
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()
