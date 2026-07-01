import pygame
from math import floor
from typing import Optional


def checking(board: list[list[int]]) -> Optional[tuple[tuple[int, int], tuple[int, int], int]]:
    dire = ((1, -1), (1, 0), (1, 1), (0, 1))
    empty_count = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == 0:
                empty_count += 1
                continue
            for i in range(4):
                end_x = x
                end_y = y
                for _ in range(4):
                    if not (0 <= end_x + dire[i][0] < BOARD_SIZE) or not (0 <= end_y + dire[i][1] < BOARD_SIZE):
                        break
                    if board[end_x + dire[i][0]][end_y + dire[i][1]] != board[x][y]:
                        break
                    end_x += dire[i][0]
                    end_y += dire[i][1]
                else:
                    if board[x][y] == 1:
                        winner = 1
                        print("\n黑方獲勝")
                    else:
                        winner = 2
                        print("\n白方獲勝")
                    print(f"({x},{y})-({end_x},{end_y})")
                    return (x * 44 + 28, y * 44 + 28), (end_x * 44 + 28, end_y * 44 + 28), winner
    if empty_count == 0:
        print("\n平手")
        return (-1, -1), (-1, -1), 0


def main() -> None:
    # init
    pygame.init()
    pygame.display.set_caption("五子棋")
    # if board_size < 7, board_x = 318, board_y = 348
    board_x, board_y = max(318, 44 * (BOARD_SIZE - 1) + 54), max(348, 44 * (BOARD_SIZE - 1) + 84)
    screen = pygame.display.set_mode((board_x, board_y), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    message = ""
    mouse_x, mouse_y = 0, 0
    move_count = 0
    is_game_active = True
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    result_line = None

    # main loop
    while True:
        # get mouse pos
        mousex, mousey = pygame.mouse.get_pos()
        mouse_x = floor(mousex / 44)
        mouse_y = floor(mousey / 44)
        for event in pygame.event.get():
            # close window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if is_game_active:
                    try:
                        if board[mouse_x][mouse_y] == 0:
                            move_count += 1
                            board[mouse_x][mouse_y] = 1 if move_count % 2 else 2
                    except:
                        pass
                # button click
                if 60 < mousex < 120 and mousey > board_x:
                    print("\nexit game")
                    exit()
                if mousex < 60 and mousey > board_x:
                    print("\nreset game")
                    main()

        # draw board
        screen.fill((238, 154, 73))
        for i in range(BOARD_SIZE):
            if i == 0 or i == BOARD_SIZE - 1:
                pygame.draw.line(screen, (0, 0, 0), (i * 44 + 27, 27), (i * 44 + 27, (BOARD_SIZE - 1) * 44 + 27), 4)
                pygame.draw.line(screen, (0, 0, 0), (27, i * 44 + 27), ((BOARD_SIZE - 1) * 44 + 27, i * 44 + 27), 4)
            else:
                pygame.draw.line(screen, (0, 0, 0), (i * 44 + 27, 27), (i * 44 + 27, (BOARD_SIZE - 1) * 44 + 27), 2)
                pygame.draw.line(screen, (0, 0, 0), (27, i * 44 + 27), ((BOARD_SIZE - 1) * 44 + 27, i * 44 + 27), 2)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == 1:
                    pygame.draw.circle(screen, (0, 0, 0), (i * 44 + 28, j * 44 + 28), 13)
                elif board[i][j] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (i * 44 + 28, j * 44 + 28), 13)

        # check winner
        if is_game_active:
            result_line = checking(board)
            if result_line is not None:
                is_game_active = False
                if result_line[2] == 1:
                    message = "Black Win"
                elif result_line[2] == 2:
                    message = "White Win"
                else:
                    message = "Draw"
            if is_game_active:
                message = "turn: Black" if move_count % 2 == 0 else "turn: White"
            # draw mouse hover
            color = (0, 0, 0) if move_count % 2 == 0 else (255, 255, 255)
            if 0 <= mouse_x < BOARD_SIZE and 0 <= mouse_y < BOARD_SIZE and board[mouse_x][mouse_y] == 0:
                pygame.draw.circle(screen, color, (mouse_x * 44 + 28, mouse_y * 44 + 28), 15, width=3)
        elif result_line is not None:
            pygame.draw.line(screen, (255, 0, 0), result_line[0], result_line[1], width=3)

        # draw button
        pygame.draw.rect(screen, (0, 0, 0), (0, board_x, 60, 30), 5)
        screen.blit(font.render("reset", True, (0, 0, 0)), (5, board_x + 5))
        pygame.draw.rect(screen, (0, 0, 0), (60, board_x, 60, 30), 5)
        screen.blit(font.render("exit", True, (0, 0, 0)), (70, board_x + 5))
        # draw button hover
        if 60 < mousex < 120 and mousey > board_x:
            pygame.draw.rect(screen, (255, 255, 255), (60, board_x, 60, 30), 5)
        if mousex < 60 and mousey > board_x:
            pygame.draw.rect(screen, (255, 255, 255), (0, board_x, 60, 30), 5)
        # draw mouse pos and message
        text = font.render(f"({mouse_x},{mouse_y})  {message}", True, (0, 0, 0))
        screen.blit(text, (125, board_x + 5))

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    BOARD_SIZE = 15
    main()
