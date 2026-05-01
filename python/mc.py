def pottery():
    class Pottery:
        def __init__(self, a: int, b: int, c: int, d: int):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

        def __hash__(self) -> int:
            return hash(str(sorted([(self.a, self.b, self.c, self.d), (self.d, self.c, self.b, self.a), (self.c, self.d, self.a, self.b), (self.b, self.a, self.d, self.c)])))

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Pottery):
                return NotImplemented
            return self.__hash__() == other.__hash__()

        def __repr__(self) -> str:
            return f"({self.a}, {self.b}, {self.c}, {self.d})"

    all_0: set[tuple[int, int, int, int]] = set()
    all_1: set[Pottery] = set()
    for i in range(21):
        for j in range(21):
            for k in range(21):
                for l in range(21):
                    all_0.add((i, j, k, l))
                    all_1.add(Pottery(i, j, k, l))
    all_2: set[tuple[int, int, int, int]] = set()
    for i in range(21):
        for j in range(i, 21):
            for k in range(j, 21):
                for l in range(k, 21):
                    all_2.add((i, j, k, l))
    print(len(all_0))  # 194481 = 3^4 * 7^4
    print(len(all_1))  # 48951 = 3^3 * 7^2 * 37
    print(len(all_2))  # 10626 = 2 * 3 * 7 * 11 * 23
    # 194481 = 441^2
    # 48951 / 27 = 1813
    # 1813 = 7^2 * 37


def leather_armor_dyeing():
    #  5713438
    # 16777216
    def average_color(colors: list[tuple[int, int, int]]) -> tuple[int, int, int]:
        sum = [0, 0, 0]
        sumMax = 0
        for color in colors:
            sum[0] += color[0]
            sum[1] += color[1]
            sum[2] += color[2]
            sumMax += max(color)
        average = (sum[0] * sumMax, sum[1] * sumMax, sum[2] * sumMax)
        return (round(average[0] / max(average)), round(average[1] / max(average)), round(average[2] / max(average)))
