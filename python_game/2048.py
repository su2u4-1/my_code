from random import randrange, choices


def check(m: list[list[int]]) -> bool:
    for i in m:
        if 0 in i:
            return False
    for i in range(R):
        for j in range(R):
            for k in range(4):
                if 0 <= i + D[k][0] < R and 0 <= j + D[k][1] < R and m[i][j] == m[i + D[k][0]][j + D[k][0]]:
                    return False
    return True


def add(m: list[list[int]]) -> None:
    while True:
        x, y = randrange(R), randrange(R)
        if m[x][y] == 0:
            m[x][y] = choices((2, 4), (4, 1))[0]
            return


def show(m: list[list[int]]) -> None:
    str_m = [[str(j) for j in i] for i in m]
    long = 1
    for i in str_m:
        for j in range(R):
            long = max(long, len(i[j]))
    for i in m:
        for j in range(R):
            if i[j] == 0:
                print(f"|{" "*long}|", end="")
            else:
                print(f"|{i[j]:{long}}|", end="")
        print()


def move(range1: range, range2: range, d: int) -> None:
    for i in range1:
        for j in range2:
            if m[i][j] == 0:
                continue
            now_i, now_j = i, j
            while True:
                if m[now_i + D[d][0]][now_j + D[d][1]] == 0:
                    m[now_i + D[d][0]][now_j + D[d][1]] = m[now_i][now_j]
                    m[now_i][now_j] = 0
                elif m[now_i][now_j] == m[now_i + D[d][0]][now_j + D[d][1]]:
                    m[now_i][now_j] = 0
                    m[now_i + D[d][0]][now_j + D[d][1]] *= 2
                    break
                now_i, now_j = now_i + D[d][0], now_j + D[d][1]
                if now_i + D[d][0] < 0 or now_i + D[d][0] >= R or now_j + D[d][1] < 0 or now_j + D[d][1] >= R:
                    break


D = [(-1, 0), (0, -1), (1, 0), (0, 1)]
R = 4
m = [[0 for _ in range(R)] for _ in range(R)]
d = ""
add(m)
add(m)

while True:
    if d == "w":
        move(range(1, R), range(R), 0)
    elif d == "a":
        move(range(R), range(1, R), 1)
    elif d == "s":
        move(range(R - 2, -1, -1), range(R), 2)
    elif d == "d":
        move(range(R), range(R - 2, -1, -1), 3)
    if d == "w" or d == "a" or d == "s" or d == "d":
        if add(m):
            break
    show(m)
    d = input("wasd: ")
