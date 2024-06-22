import pygame
from math import floor as fl


def checking() -> tuple[tuple[int, int], tuple[int, int]]|None:
    global gameContinue, winner
    a = [1, 1, 1, 0, 0, -1, -1, -1]
    b = [-1, 0, 1, -1, 1, -1, 0, 1]
    n = 0
    for x in range(SL):
        for y in range(SL):
            if chessBoard[x][y] == 0:
                n += 1
            else:
                for i in range(8):
                    x1 = x
                    y1 = y
                    for _ in range(4):
                        if x1 + a[i] < 0 or x1 + a[i] > 14 or y1 + b[i] < 0 or y1 + b[i] > 14:
                            break
                        elif chessBoard[x1 + a[i]][y1 + b[i]] != chessBoard[x][y]:
                            break
                        x1 += a[i]
                        y1 += b[i]
                    else:
                        gameContinue = False
                        if chessBoard[x][y] == 1:
                            winner = "Black wins"
                            print("\n黑方獲勝")
                        else:
                            winner = "White wins"
                            print("\n白方獲勝")
                        print(f"({x},{y})-({x1},{y1})")
                        return ((x * 44 + 28, y * 44 + 28), (x1 * 44 + 28, y1 * 44 + 28))
    if n == 0:
        gameContinue = False
        winner = "draw"
        print("\n平手")
        return


def main()->None:
    global chessBoard, gameContinue, winner
    pygame.init()
    pygame.display.set_caption("五子棋")
    screen = pygame.display.set_mode((670, 700), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    winner = ""
    mx, my = 0, 0
    first = 0
    gameContinue = True
    chessBoard = [[0 for _ in range(SL)] for _ in range(SL)]
    while True:
        mousex, mousey = pygame.mouse.get_pos()
        mx = fl(mousex / 44)
        my = fl(mousey / 44)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if gameContinue:
                    try:
                        if chessBoard[mx][my] == 0:
                            first += 1
                            if first % 2 == 1:
                                chessBoard[mx][my] = 1
                            else:
                                chessBoard[mx][my] = 2
                    except:
                        pass
                if 60 < mousex < 120 and 670 < mousey:
                    print("\nexit game")
                    exit()
                if mousex < 60 and 670 < mousey:
                    print("\nreset game")
                    main()
        screen.fill((238, 154, 73))
        for i in range(SL):
            if i == 0 or i == SL - 1:
                pygame.draw.line(screen, (0, 0, 0), (i * 44 + 27, 27), (i * 44 + 27, (SL - 1) * 44 + 27), 4)
                pygame.draw.line(screen, (0, 0, 0), (27, i * 44 + 27), ((SL - 1) * 44 + 27, i * 44 + 27), 4)
            else:
                pygame.draw.line(screen, (0, 0, 0), (i * 44 + 27, 27), (i * 44 + 27, (SL - 1) * 44 + 27), 2)
                pygame.draw.line(screen, (0, 0, 0), (27, i * 44 + 27), ((SL - 1) * 44 + 27, i * 44 + 27), 2)
        for i in range(SL):
            for j in range(SL):
                if chessBoard[i][j] == 1:
                    pygame.draw.circle(screen, (0, 0, 0), (i * 44 + 28, j * 44 + 28), 13)
                elif chessBoard[i][j] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (i * 44 + 28, j * 44 + 28), 13)
        if gameContinue:
            winner_line = checking()
        if first % 2 == 0:
            turn = "Black"
            pygame.draw.circle(screen, (0, 0, 0), (mx * 44 + 28, my * 44 + 28), 15, width=3)
        else:
            turn = "White"
            pygame.draw.circle(screen, (255, 255, 255), (mx * 44 + 28, my * 44 + 28), 15, width=3)
        if not gameContinue and type(winner_line) == tuple:
            pygame.draw.line(screen, (255, 0, 0), winner_line[0], winner_line[1], width=3)
        pygame.draw.rect(screen, (0, 0, 0), (0, 670, 60, 30), 5)
        screen.blit(font.render("reset", True, (0, 0, 0)), (5, 675))
        pygame.draw.rect(screen, (0, 0, 0), (60, 670, 60, 30), 5)
        screen.blit(font.render("exit", True, (0, 0, 0)), (70, 675))
        if 60 < mousex < 120 and 670 < mousey:
            pygame.draw.rect(screen, (255, 255, 255), (60, 670, 60, 30), 5)
        if mousex < 60 and 670 < mousey:
            pygame.draw.rect(screen, (255, 255, 255), (0, 670, 60, 30), 5)
        if gameContinue:
            text = font.render(f"({mx},{my})  {turn}", True, (0, 0, 0))
        else:
            text = font.render(f"({mx},{my})  {winner}", True, (0, 0, 0))
        screen.blit(text, (125, 675))
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    SL = 15
    main()
