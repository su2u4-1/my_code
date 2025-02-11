from typing import Sequence
from math import sin, cos, pi
from random import randint as ri

import pygame


# 球
class Ball:
    # 初始化球,主要是設定球的各項屬性
    def __init__(self, x: int, y: int, color: Sequence[int], direction: int = -1):
        self.x = x
        self.y = y
        self.color = color
        if direction == -1:
            self.d = ri(0, 360)
        else:
            self.d = direction

    # 讓球移動,同時偵測碰撞並改變方向
    def move(self, speed: int):
        self.x += sin(self.d / 180 * pi) * speed
        self.y += cos(self.d / 180 * pi) * speed
        if self.x > W - Rr or self.x < 0 + Rr:
            self.d = 360 - self.d
        if self.y > H - Rr or self.y < 0 + Rr:
            self.d = 540 - self.d
            if self.d >= 360:
                self.d -= 360


# 設定pygame
pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
pygame.display.set_caption("碰撞")
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
# 設定球與移動速度
Speed = 5
Rr = 10
balls: list[Ball] = []
for _ in range(50):
    balls.append(Ball(ri(5, W - 5), ri(5, H - 5), (ri(0, 255), ri(0, 255), ri(0, 255))))

while True:
    # 如果視窗被關閉或esc被按下就關閉pygame且離開程式
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_SPACE:
                mx, my = pygame.mouse.get_pos()
                balls.append(Ball(mx, my, (ri(0, 255), ri(0, 255), ri(0, 255))))
            elif event.key == pygame.K_w:
                Speed += 1
            elif event.key == pygame.K_s:
                Speed -= 1
                if Speed < 0:
                    Speed = 0
            elif event.key == pygame.K_a:
                Rr -= 1
                if Rr < 1:
                    Rr = 1
            elif event.key == pygame.K_d:
                Rr += 1

    # 清空畫面
    screen.fill((0, 0, 0))
    # 讓球移動
    for i in balls:
        i.move(Speed)
        # 繪製新的球
        pygame.draw.circle(screen, i.color, (round(i.x), round(i.y)), Rr)
    for i in range(len(balls)):
        for j in range(i, len(balls)):
            if i != j:
                if (balls[i].x - balls[j].x) ** 2 + (balls[i].y - balls[j].y) ** 2 <= Rr * 2:
                    balls[i].d, balls[j].d = balls[j].d, balls[i].d
    # 更新畫面
    pygame.display.update()
    clock.tick()
