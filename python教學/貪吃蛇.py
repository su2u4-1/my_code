# 載入模組
import pygame
from random import randint as ri

# 設定pygame
pygame.init()
W = round(pygame.display.Info().current_w / 10) - 1
H = round(pygame.display.Info().current_h / 10) - 3
screen = pygame.display.set_mode((W * 10, H * 10), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# 設定變數
score = 0
snake = [(1, 1), (1, 2), (1, 3)]
tail = (1, 0)
dire = (0, 0)
apple: list[tuple[int, int]] = []

# 主迴圈
while True:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("score:", score)
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dire = (0, -1)
            elif event.key == pygame.K_a:
                dire = (-1, 0)
            elif event.key == pygame.K_s:
                dire = (0, 1)
            elif event.key == pygame.K_d:
                dire = (1, 0)
            elif event.key == pygame.K_SPACE:
                dire = (0, 0)

    # 更新內容
    if dire != (0, 0):
        head = snake[-1]
        snake.append((head[0] + dire[0], head[1] + dire[1]))
        tail = snake.pop(0)

    for i in apple:
        if i in snake:
            score += 1
            snake.insert(0, tail)
            apple.remove(i)
            break

    if snake[-1] in snake[:-1]:
        pygame.quit()
        print("GAMEOVER\nscore:", score)
        exit()
    if snake[-1][0] < 0 or snake[-1][0] >= W or snake[-1][1] < 0 or snake[-1][1] >= H:
        pygame.quit()
        print("GAMEOVER\nscore:", score)
        exit()

    if len(apple) < 50:
        a = (ri(0, W - 1), ri(0, H - 1))
        if a not in apple and a not in snake:
            apple.append(a)

    # 更新畫面
    screen.fill((0, 0, 0))
    for i in range(W):
        for j in range(H):
            pygame.draw.rect(screen, (50, 200, 0), (i * 10 + 1, j * 10 + 1, 8, 8))
    for i in apple:
        pygame.draw.rect(screen, (200, 0, 0), (i[0] * 10 + 1, i[1] * 10 + 1, 8, 8))
    for i in snake:
        if i == snake[-1]:
            pygame.draw.rect(screen, (0, 0, 0), (i[0] * 10 + 1, i[1] * 10 + 1, 8, 8))
        else:
            pygame.draw.rect(screen, (200, 200, 0), (i[0] * 10 + 1, i[1] * 10 + 1, 8, 8))

    pygame.display.update()
    clock.tick(10)
