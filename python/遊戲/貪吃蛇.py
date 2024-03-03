import pygame
from random import randint as ri

pygame.init()
pygame.display.set_caption("貪吃蛇")
W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
W = round(W / 10) - 1
H = round(H / 10) - 3
screen = pygame.display.set_mode((W * 10, H * 10), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)
f = True

score = 0
snake = [[1, 1], [1, 2], [1, 3]]
tail = [1, 0]
dire = (0, 0)
color = []
apple = []
for i in range(W):
    a = []
    for j in range(H):
        a.append(ri(150, 200))
    color.append(a)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("score:", score)
            exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w | pygame.K_UP:
                    dire = (0, -1)
                case pygame.K_a | pygame.K_LEFT:
                    dire = (-1, 0)
                case pygame.K_s | pygame.K_DOWN:
                    dire = (0, 1)
                case pygame.K_d | pygame.K_RIGHT:
                    dire = (1, 0)
                case pygame.K_b:
                    dire = (0, 0)
                case pygame.K_ESCAPE:
                    pygame.quit()
                    print("score:", score)
                    exit()

    if dire != (0, 0) and f:
        head = snake[-1].copy()
        head[0] += dire[0]
        head[1] += dire[1]
        snake.append(head)
        tail = snake.pop(0)

    for i in apple:
        if i in snake and f:
            score += 1
            snake = [tail] + snake
            apple.remove(i)
            break

    if len(apple) <= (W * H / 500) - (len(snake) / 10) and f:
        a = [ri(0, W - 1), ri(0, H - 1)]
        if a not in snake and (a[0] > 15 or a[1] > 1):
            apple.append(a)

    if snake[-1] in snake[:-1]:
        f = False
    if snake[-1][0] < 0 or snake[-1][0] >= W or snake[-1][1] < 0 or snake[-1][0] >= H:
        f = False

    screen.fill((0, 0, 0))
    for i in range(W):
        for j in range(H):
            pygame.draw.rect(screen, (50, color[i][j], 0), (i * 10 + 1, j * 10 + 1, 8, 8))
    for i in apple:
        pygame.draw.rect(screen, (200, 0, 0), (i[0] * 10 + 1, i[1] * 10 + 1, 8, 8))
    for i in snake:
        if i == snake[-1]:
            pygame.draw.rect(screen, (0, 0, 0), (i[0] * 10 + 1, i[1] * 10 + 1, 8, 8))
        else:
            pygame.draw.rect(screen, (color[i[0]][i[1]], color[i[0]][i[1]], 0), (i[0] * 10 + 1, i[1] * 10 + 1, 8, 8))
    screen.blit(font.render(f"score:{score},apple:{len(apple)}", True, (255, 255, 255), (0, 0, 0)), (0, 0))
    if not f:
        screen.blit(font.render("GAMEOVER", True, (255, 0, 0), (255, 255, 255)), (W / 2 * 10 - 40, H / 2 * 10 - 40))
        screen.blit(font.render(f"score:{score}", True, (255, 0, 0), (255, 255, 255)), (W / 2 * 10 - 40, H / 2 * 10 - 20))

    pygame.display.update()
    clock.tick(10)
