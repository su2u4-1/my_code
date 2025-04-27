from typing import Literal, Callable

from lib import get_int, D8, AI_1, plus_model_1, show_model


class Game_gomoku:
    def __init__(self, size: int = 15) -> None:
        self.init(size)

    def init(self, size: int = 15) -> None:
        self.size = size
        self.status: Literal["Black wins", "White wins", "draw", "gamerun"] = "gamerun"
        self.turn: int = 1
        self.chessBoard = [[0 for _ in range(size)] for _ in range(size)]
        self.run = True
        self.result = (False, ((-1, -1), (-1, -1)))
        self.p1: Callable[[list[list[int]], int, int], tuple[int, int]] = ai_a.next
        self.p2: Callable[[list[list[int]], int, int], tuple[int, int]] = ai_b.next

    def check(self) -> tuple[bool, tuple[tuple[int, int], tuple[int, int]]]:
        n = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.chessBoard[x][y] == 0:
                    n += 1
                else:
                    nx, ny = x, y
                    for i in range(4):
                        for j in range(4):
                            nx, ny = x + D8[i][0] * j, y + D8[i][1] * j
                            if not (0 <= nx + D8[i][0] < self.size and 0 <= ny + D8[i][1] < self.size):
                                break
                            elif self.chessBoard[nx + D8[i][0]][ny + D8[i][1]] != self.chessBoard[x][y]:
                                break
                        else:
                            if self.chessBoard[x][y] == 1:
                                self.status = "Black wins"
                            else:
                                self.status = "White wins"
                            self.ai = [True, True]
                            nx, ny = x + D8[i][0] * 4, y + D8[i][1] * 4
                            return True, ((x * 44 + 28, y * 44 + 28), (nx * 44 + 28, ny * 44 + 28))
        if n == 0:
            self.status = "draw"
        return False, ((-1, -1), (-1, -1))

    def put_chess(self, x: int, y: int) -> None:
        if self.chessBoard[x][y] == 0 and self.status == "gamerun":
            if self.turn == 1:
                self.turn = 2
                self.chessBoard[x][y] = 1
            else:
                self.turn = 1
                self.chessBoard[x][y] = 2
        else:
            raise RuntimeError("position is not empty or game is over")

    def main(self) -> None:
        while self.run:
            if self.status == "gamerun":
                self.result = self.check()
            if self.status == "gamerun":
                if self.turn == 1:
                    x, y = self.p1(self.chessBoard, 1, 2)
                    self.put_chess(x, y)
                elif self.turn == 2:
                    x, y = self.p2(self.chessBoard, 2, 1)
                    self.put_chess(x, y)
            if self.status != "gamerun":
                if self.status == "Black wins":
                    plus_model_1("./gomoku/ai.pkl", (ai_a.log, 5), (ai_b.log, -5))
                elif self.status == "White wins":
                    plus_model_1("./gomoku/ai.pkl", (ai_a.log, -5), (ai_b.log, 5))
                else:
                    plus_model_1("./gomoku/ai.pkl", (ai_a.log, -1), (ai_b.log, -1))
                return
        self.again()

    def again(self) -> None:
        self.init(self.size)
        self.main()


if __name__ == "__main__":
    size = get_int("size(recommended size: 15): ", "must be great than 5", lambda x: x >= 5)
    loop = get_int("loop: ", "must be great than 0", lambda x: x >= 0)
    for _ in range(loop):
        ai_a = AI_1("./gomoku/ai.pkl")
        ai_b = AI_1("./gomoku/ai.pkl")
        game = Game_gomoku(size)
        game.main()

show_model("./gomoku/ai.pkl")
