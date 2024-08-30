from Game import get_int


class Game_ooxx:
    def __init__(self, symbol: tuple[str, str], size: int) -> None:
        self.init(symbol, size)

    def init(self, symbol: tuple[str, str], size: int) -> None:
        self.m = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.symbol = symbol

    def check(self) -> None:
        pass

    def show(self) -> None:
        pass

    def main(self) -> None:
        pass

    def again(self) -> None:
        pass


if __name__ == "__main__":
    symbol_o = "O"
    symbol_x = "X"
    while len(symbol_o) != 1:
        symbol_o = input("symbol A: ")
    while len(symbol_x) != 1:
        symbol_x = input("symbol B: ")
    size = get_int("size: ", "must be greater than or equal to 3", lambda x: x >= 3)
    game = Game_ooxx((symbol_o, symbol_x), size)
    game.main()
