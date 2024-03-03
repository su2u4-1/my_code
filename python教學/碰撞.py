import pygame
from math import sin, cos, pi
from random import randint as ri


class Ball:
    def __init__(self, x: int | float, y: int | float, color: list[int] | tuple[int], r: int = 5, direction: int | float = -1):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        if direction == -1:
            self.d = ri(0, 360)
        else:
            self.d = direction

    def move(self, speed):
        self.x += sin(self.d / 180 * pi) * speed
        self.y += cos(self.d / 180 * pi) * speed
        if self.x > W - self.r or self.x < 0 + self.r:
            self.d = 360 - self.d
        if self.y > H - self.r or self.y < 0 + self.r:
            self.d = 540 - self.d
            if self.d >= 360:
                self.d -= 360


pygame.init()
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
pygame.display.set_caption("碰撞")
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
SPEED = 5
ball = []
for _ in range(100):
    ball.append(Ball(ri(5, W - 5), ri(5, H - 5) , (ri(0, 255), ri(0, 255), ri(0, 255))))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    screen.fill((0, 0, 0))
    for i in ball:
        i.move(SPEED)
    for i in ball:
        pygame.draw.circle(screen, i.color, (round(i.x), round(i.y)), i.r)
    pygame.display.update()
    clock.tick(100)
