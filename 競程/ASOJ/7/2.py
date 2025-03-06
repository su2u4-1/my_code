n, m = map(int, input().split())
p = [["w" for _ in range(m)] for _ in range(n)]
x, y = n // 2, m // 2
d = 0
D = ((-1, 0), (0, 1), (1, 0), (0, -1))
a = [0, 0]


def update(nn: int):
    global d, x, y
    if nn == -1:
        if d == 0:
            d = 3
        else:
            d -= 1
    if nn == 1:
        if d == 3:
            d = 0
        else:
            d += 1
    x += D[d][0]
    y += D[d][1]
    a[0] += 1
    if x >= n or x < 0 or y >= m or y < 0:
        print(*a)
        return True
    elif a[0] >= 1000000:
        print("bad ant", a[1])
        return True
    return False


while True:
    if p[x][y] == "w":
        a[1] += 1
        p[x][y] = "b"
        if update(0):
            break
        if p[x][y] == "w":
            a[1] += 1
            p[x][y] = "b"
            if update(1):
                break
    elif p[x][y] == "b":
        if update(-1):
            break
        if p[x][y] == "b":
            a[1] -= 1
            p[x][y] = "w"
            if update(1):
                break
