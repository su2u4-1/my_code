from random import randint as ri
from random import choice as rc
import pygame
from math import sqrt, cos, sin, pi


class Point:
    def __init__(self, x: float, y: float, m: float = 1.0, vx: float = 0.0, vy: float = 0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = (ri(100, 255), ri(100, 255), ri(100, 255))
        self.m = m
        self.is_dead = False

    def evaluate(self, others: list["Point"], g_constant: float):
        if self.is_dead:
            return
        ax, ay = 0.0, 0.0
        softening = 100.0

        for other in others:
            if other is self or other.is_dead:
                continue

            dx = other.x - self.x
            dy = other.y - self.y
            dist_sq = dx**2 + dy**2

            # 修正後的碰撞合併邏輯：如果距離小於兩者半徑之和（簡化處理）
            # 這裡使用質量作為距離判定，若太近則發生質量轉移
            if dist_sq < (self.m + other.m) * 2:
                if self.m >= other.m:
                    transfer = other.m * 0.1
                    self.m += transfer
                    other.m -= transfer
                    # 吸收動量
                    self.vx = (self.vx * self.m + other.vx * transfer) / (self.m + transfer)
                    self.vy = (self.vy * self.m + other.vy * transfer) / (self.m + transfer)
                continue

            dist_sq += softening
            dist = sqrt(dist_sq)
            # a = G * m_other / r^2
            force = g_constant * other.m / dist_sq

            ax += dx / dist * force
            ay += dy / dist * force

        self.vx += ax
        self.vy += ay

    def move(self, W: int, H: int):
        self.x += self.vx
        self.y += self.vy

        # 邊界反彈並損失動能
        if self.x < 0 or self.x > W:
            self.vx *= -0.5
            self.x = max(0, min(W, self.x))
        if self.y < 0 or self.y > H:
            self.vy *= -0.5
            self.y = max(0, min(H, self.y))


pygame.init()
W, H = 1366, 768
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("二維重力模擬 - 質量演化")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

points: list[Point] = [Point(ri(50, W - 50), ri(50, H - 50), ri(1, 3)) for _ in range(100)]
g_speed = 1.0
run = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_SPACE:
                run = not run
            elif event.key == pygame.K_UP:
                g_speed += 0.5
            elif event.key == pygame.K_DOWN:
                g_speed = max(0, g_speed - 0.5)
            elif event.key == pygame.K_r:
                for p in points:
                    p.x = ri(50, W - 50)
                    p.y = ri(50, H - 50)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(Point(*event.pos, m=5.0))

    screen.fill((10, 10, 20))

    if run:
        for p in points:
            p.evaluate(points, g_speed)
        for p in points:
            p.move(W, H)

    next_points: list[Point] = []
    for p in points:
        if p.m < 0.01 * ri(1, 5) and len(next_points) > 0:  # 質量太小則消失
            rc(next_points).m += p.m  # 將微小質量轉移給隨機一個點，模擬物質散佈
            continue

        # 分裂邏輯：給予子代相反的初速度噴射，防止立即合併
        if p.m > ri(15, 20):
            p.m /= 2
            angle = ri(0, 360) * pi / 180
            push_force = 2.0
            # 新增一個點，並賦予反向速度
            new_point = Point(p.x + cos(angle) * 10, p.y + sin(angle) * 10, p.m, p.vx + cos(angle + pi) * push_force, p.vy + sin(angle + pi) * push_force)
            next_points.append(new_point)
            p.vx += cos(angle) * push_force
            p.vy += sin(angle) * push_force

        next_points.append(p)

    points = next_points

    for p in points:
        # 繪製半徑與質量開根號成正比
        radius = sqrt(p.m) * 4
        pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), radius)

    status = f"N: {len(points)}, G: {g_speed}, {'RUN' if run else 'STOP'}"
    screen.blit(font.render(status, True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
    clock.tick(60)
