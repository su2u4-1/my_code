from typing import Literal

import pygame

from Game import get_int, D8


class Game_gomoku:
    def __init__(self, size: int = 15) -> None:
        self.init(size)

    def init(self, size: int = 15) -> None:
        pygame.init()
        self.size = size
        self.h = 44 * size + 10
        self.w = 44 * size + 40
        pygame.display.set_caption("gomoku")
        self.screen = pygame.display.set_mode((self.h, self.w), pygame.RESIZABLE)
        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()
        self.status: Literal["Black wins", "White wins", "draw", "gamerun"] = "gamerun"
        self.mx, self.my = 0, 0
        self.turn: Literal["black", "white"] = "black"
        self.chessBoard = [[0 for _ in range(size)] for _ in range(size)]
        self.run = True
        self.result = (False, ((-1, -1), (-1, -1)))

    def show(self) -> None:
        self.screen.fill((238, 154, 73))
        for i in range(self.size):
            if i == 0 or i == self.size - 1:
                pygame.draw.line(self.screen, (0, 0, 0), (i * 44 + 27, 27), (i * 44 + 27, (self.size - 1) * 44 + 27), 4)
                pygame.draw.line(self.screen, (0, 0, 0), (27, i * 44 + 27), ((self.size - 1) * 44 + 27, i * 44 + 27), 4)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), (i * 44 + 27, 27), (i * 44 + 27, (self.size - 1) * 44 + 27), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (27, i * 44 + 27), ((self.size - 1) * 44 + 27, i * 44 + 27), 2)
        for i in range(self.size):
            for j in range(self.size):
                if self.chessBoard[i][j] == 1:
                    pygame.draw.circle(self.screen, (0, 0, 0), (i * 44 + 28, j * 44 + 28), 13)
                elif self.chessBoard[i][j] == 2:
                    pygame.draw.circle(self.screen, (255, 255, 255), (i * 44 + 28, j * 44 + 28), 13)
        if 0 <= self.mx < self.size and 0 <= self.my < self.size:
            if self.turn == "black":
                pygame.draw.circle(self.screen, (0, 0, 0), (self.mx * 44 + 28, self.my * 44 + 28), 15, width=3)
            else:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.mx * 44 + 28, self.my * 44 + 28), 15, width=3)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, self.h, 60, 30), 5)
        self.screen.blit(self.font.render("reset", True, (0, 0, 0)), (5, self.h + 5))
        pygame.draw.rect(self.screen, (0, 0, 0), (60, self.h, 60, 30), 5)
        self.screen.blit(self.font.render("exit", True, (0, 0, 0)), (70, self.h + 5))
        mx, my = pygame.mouse.get_pos()
        if 60 <= mx < 120 and self.h <= my < self.h + 30:
            pygame.draw.rect(self.screen, (255, 255, 255), (60, self.h, 60, 30), 5)
        elif 0 <= mx < 60 and self.h <= my < self.h + 30:
            pygame.draw.rect(self.screen, (255, 255, 255), (0, self.h, 60, 30), 5)
        if self.status == "gamerun":
            text = self.font.render(f"({self.mx},{self.my})  {self.turn}", True, (0, 0, 0))
        else:
            text = self.font.render(f"({self.mx},{self.my})  {self.status}", True, (0, 0, 0))
        self.screen.blit(text, (125, self.h + 5))

    def check(self) -> tuple[bool, tuple[tuple[int, int], tuple[int, int]]]:
        n = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.chessBoard[x][y] == 0:
                    n += 1
                else:
                    for i in range(8):
                        x1 = x
                        y1 = y
                        for _ in range(4):
                            if x1 + D8[i][0] < 0 or x1 + D8[i][0] > 14 or y1 + D8[i][1] < 0 or y1 + D8[i][1] > 14:
                                break
                            elif self.chessBoard[x1 + D8[i][0]][y1 + D8[i][1]] != self.chessBoard[x][y]:
                                break
                            x1 += D8[i][0]
                            y1 += D8[i][1]
                        else:
                            if self.chessBoard[x][y] == 1:
                                self.status = "Black wins"
                            else:
                                self.status = "White wins"
                            return True, ((x * 44 + 28, y * 44 + 28), (x1 * 44 + 28, y1 * 44 + 28))
        if n == 0:
            self.status = "draw"
        return False, ((-1, -1), (-1, -1))

    def main(self) -> None:
        while self.run:
            self.mx, self.my = map(lambda x: x // 44, pygame.mouse.get_pos())
            if self.status == "gamerun":
                self.result = self.check()
            self.show()
            if self.result[0]:
                pygame.draw.line(self.screen, (255, 0, 0), self.result[1][0], self.result[1][1], 3)
            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.run = False
                    return
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        self.run = False
                        break
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if 0 <= self.mx < self.size and 0 <= self.my < self.size:
                        if self.chessBoard[self.mx][self.my] == 0 and self.status == "gamerun":
                            if self.turn == "black":
                                self.turn = "white"
                                self.chessBoard[self.mx][self.my] = 1
                            else:
                                self.turn = "black"
                                self.chessBoard[self.mx][self.my] = 2
                    else:
                        mx, my = pygame.mouse.get_pos()
                        if 60 <= mx < 120 and self.h <= my < self.h + 30:
                            pygame.quit()
                            self.run = False
                            return
                        elif 0 <= mx < 60 and self.h <= my < self.h + 30:
                            pygame.quit()
                            self.run = False
                            break
        self.again()

    def again(self) -> None:
        self.init(self.size)
        self.main()


if __name__ == "__main__":
    game = Game_gomoku(get_int("size(greater than 19 may cause problems): ", "must be great than 5", lambda x: x > 5))
    game.main()
