import random

a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def summon():
    global a
    b = [random.randint(0, 3), random.randint(0, 3)]
    if a[b[0]][b[1]] == 0:
        a[b[0]][b[1]] = 1
        print(b)
    elif judgment(a) == 5:
        return
    else:
        summon()


def up():
    global a
    for i in range(1, 4):
        for j in range(0, 4):
            for r in range(0, i):
                if a[i - r - 1][j] == 0:
                    a[i - r - 1][j] = a[i - r][j]
                    a[i - r][j] = 0
                elif a[i - r][j] == a[i - r - 1][j]:
                    a[i - r][j] = 0
                    a[i - r - 1][j] += 1
                elif a[i - r][j] != a[i - r - 1][j] and a[i - r - 1][j] != 0:
                    break


def down():
    global a
    for i in range(0, 3):
        for j in range(0, 4):
            for r in range(0, 3 - i):
                if a[i + r + 1][j] == 0:
                    a[i + r + 1][j] = a[i + r][j]
                    a[i + r][j] = 0
                elif a[i + r][j] == a[i + r + 1][j]:
                    a[i + r][j] = 0
                    a[i + r + 1][j] += 1
                elif a[i + r][j] != a[i + r + 1][j] and a[i + r + 1][j] != 0:
                    break


def left():
    global a
    for i in range(0, 4):
        for j in range(1, 4):
            for r in range(0, j):
                if a[i][j - r - 1] == 0:
                    a[i][j - r - 1] = a[i][j - r]
                    a[i][j - r] = 0
                elif a[i][j - r] == a[i][j - r - 1]:
                    a[i][j - r] = 0
                    a[i][j - r - 1] += 1
                elif a[i][j - r] != a[i][j - r - 1] and a[i][j - r - 1] != 0:
                    break


def right():
    global a
    for i in range(0, 4):
        for j in range(0, 3):
            for r in range(0, 3 - j):
                if a[i][j + r + 1] == 0:
                    a[i][j + r + 1] = a[i][j + r]
                    a[i][j + r] = 0
                elif a[i][j + r] == a[i][j + r + 1]:
                    a[i][j + r] = 0
                    a[i][j + r + 1] += 1
                elif a[i][j + r] != a[i][j + r + 1] and a[i][j + r + 1] != 0:
                    break


def judgment(n: list[list[int]]):
    g = 0
    h = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if n[i][j] >= 11:
                return True
            if n[i][j] != 0:
                h += 1
    for i in range(0, 4):
        for j in range(0, 4):
            for _ in range(0, 3):
                try:
                    if n[i][j] != n[i - 1][j] and n[i][j] != n[i + 1][j] and n[i][j] != n[i][j - 1] and n[i][j] != n[i][j + 1]:
                        g += 1
                except:
                    pass
    if g == 16:
        return False
    if h == 16:
        return 5


summon()
while True:
    summon()
    c = "|"
    d: list[str] = []
    for i in range(0, 4):
        for j in range(0, 4):
            f = a[i][j]
            if f == 0:
                c += " |"
            elif f > 0:
                c += f"{2**f}|"
        d.append(c)
        c = "|"
    for i in range(0, 4):
        print(d[i])
    e = input("請輸入wasd來移動,輸入off關閉")
    if e == "w":
        up()
    if e == "s":
        down()
    if e == "a":
        left()
    if e == "d":
        right()
    if e == "off":
        print("結束遊戲")
        break
    if judgment(a) == True:
        print("你贏了")
        break
    if judgment(a) == False and judgment(a) == 5:
        print("你輸了")
        break
