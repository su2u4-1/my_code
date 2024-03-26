import pygame
from math import sin, cos, pi
from random import randint as ri


# 球
class Ball:
    # 初始化球,主要是設定球的各項屬性
    def __init__(self, x: int | float, y: int | float, color: list[int] | tuple[int], r: int = 5, direction: int | float = -1):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        if direction == -1:
            self.d = ri(0, 360)
        else:
            self.d = direction

    # 讓球移動,同時偵測碰撞並改變方向
    def move(self, speed):
        self.x += sin(self.d / 180 * pi) * speed
        self.y += cos(self.d / 180 * pi) * speed
        if self.x > W - self.r or self.x < 0 + self.r:
            self.d = 360 - self.d
        if self.y > H - self.r or self.y < 0 + self.r:
            self.d = 540 - self.d
            if self.d >= 360:
                self.d -= 360


# 設定pygame
pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
pygame.display.set_caption("碰撞")
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
# 設定球與移動速度
SPEED = 10
ball_1 = Ball(ri(5, W - 5), ri(5, H - 5), (ri(0, 255), ri(0, 255), ri(0, 255)))
ball_2 = Ball(ri(5, W - 5), ri(5, H - 5), (ri(0, 255), ri(0, 255), ri(0, 255)))

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

    # 清空畫面
    screen.fill((0, 0, 0))
    # 讓球移動
    ball_1.move(SPEED)
    ball_2.move(SPEED)
    # 繪製新的球
    pygame.draw.circle(screen, ball_1.color, (round(ball_1.x), round(ball_1.y)), ball_1.r)
    pygame.draw.circle(screen, ball_2.color, (round(ball_2.x), round(ball_1.y)), ball_2.r)
    # 更新畫面
    pygame.display.update()
    clock.tick(100)
