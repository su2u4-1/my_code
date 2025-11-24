import pygame
from random import randint

pygame.init()
W, H = 400, 400
LENGTH = 50
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
# 0: empty, 1: wall, 2: target, 3: box, 4: box on target, 5: player
# matrix = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1],
#     [1, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]  # 12 x 8
matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 3, 1, 0, 1],
    [1, 2, 2, 3, 0, 3, 0, 1],
    [1, 1, 1, 2, 0, 3, 5, 1],
    [1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]  # 8 x 8
matrix_copy = [row.copy() for row in matrix]
count = 0
max_count = 4
win = False


def matrix_gen(w: int, h: int, length: int, box_count: int) -> list[list[int]]:
    cols = w // length
    rows = h // length
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                new_matrix[x][y] = 1  # wall
    for _ in range(box_count):
        placed = False
        while not placed:
            bx = randint(2, rows - 3)
            by = randint(2, cols - 3)
            if new_matrix[bx][by] == 0:
                new_matrix[bx][by] = 3  # box
                placed = True
        placed = False
        while not placed:
            tx = randint(1, rows - 2)
            ty = randint(1, cols - 2)
            if new_matrix[tx][ty] == 0:
                new_matrix[tx][ty] = 2  # target
                placed = True
    placed = False
    while not placed:
        px = randint(1, rows - 2)
        py = randint(1, cols - 2)
        if new_matrix[px][py] == 0:
            new_matrix[px][py] = 5  # player
            placed = True
    return new_matrix


def draw_matrix(matrix: list[list[int]]) -> None:
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            rect = pygame.Rect(y * LENGTH, x * LENGTH, LENGTH, LENGTH)
            if (x, y) == player:
                pygame.draw.rect(screen, (255, 0, 0), rect)  # player
            elif cell == 0:
                pygame.draw.rect(screen, (200, 200, 200), rect)  # empty
            elif cell == 1:
                pygame.draw.rect(screen, (100, 100, 100), rect)  # wall
            elif cell == 2:
                pygame.draw.rect(screen, (0, 0, 255), rect)  # target
            elif cell == 3:
                pygame.draw.rect(screen, (255, 165, 0), rect)  # box
            elif cell == 4:
                pygame.draw.rect(screen, (0, 255, 0), rect)  # box on target


def push_box(matrix: list[list[int]], dire: tuple[int, int], pos: tuple[int, int]) -> tuple[int, int]:
    global count
    nx, ny = pos[0] + dire[0], pos[1] + dire[1]
    if 0 <= nx < H // LENGTH and 0 <= ny < W // LENGTH:
        if matrix[nx][ny] == 0 or matrix[nx][ny] == 2:
            return (nx, ny)
        elif matrix[nx][ny] == 3 or matrix[nx][ny] == 4:
            nnx, nny = nx + dire[0], ny + dire[1]
            if 0 <= nnx < H // LENGTH and 0 <= nny < W // LENGTH:
                if matrix[nnx][nny] == 0 or matrix[nnx][nny] == 2:
                    if matrix[nnx][nny] == 0:
                        matrix[nnx][nny] = 3
                    else:
                        matrix[nnx][nny] = 4
                        count += 1
                    if matrix[nx][ny] == 4:
                        matrix[nx][ny] = 2
                        count -= 1
                    else:
                        matrix[nx][ny] = 0
                    return (nx, ny)
    return pos


def preprocess(matrix: list[list[int]]) -> tuple[int, int]:
    player_pos = (0, 0)
    for x, row in enumerate(matrix):
        for y, cell in enumerate(row):
            if cell == 5:
                player_pos = (x, y)
                matrix[x][y] = 0
    return player_pos


player = preprocess(matrix)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif (not win) and (event.key == pygame.K_UP or event.key == pygame.K_w):
                player = push_box(matrix, (-1, 0), player)
            elif (not win) and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                player = push_box(matrix, (1, 0), player)
            elif (not win) and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                player = push_box(matrix, (0, -1), player)
            elif (not win) and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                player = push_box(matrix, (0, 1), player)
            elif event.key == pygame.K_r:
                max_count = 4
                # matrix = matrix_gen(W, H, LENGTH, max_count)
                matrix = [row.copy() for row in matrix_copy]
                player = preprocess(matrix)
                count = 0
                win = False

    screen.fill((0, 0, 0))

    draw_matrix(matrix)
    if count == max_count:
        win = True
        font = pygame.font.Font(None, 74)
        text = font.render("You Win!", True, (255, 0, 0))
        screen.blit(text, (W // 2 - text.get_width() // 2, H // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
