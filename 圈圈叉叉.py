def check(m):
    n = 0
    win = -1
    for i in range(3):
        t = []
        t1 = []
        for j in range(3):
            if m[i][j] == 0:
                n += 1
            else:
                t.append(m[i][j])
            if m[j][i] == 0:
                n += 1
            else:
                t1.append(m[j][i])
        if len(t) == 3 and t[0] == t[1] == t[2]:
            win = t[0]
        if len(t1) == 3 and t1[0] == t1[1] == t1[2]:
            win = t1[0]
    t = []
    for i in range(3):
        t.append(m[i][i])
    for i in range(3):
        t.append(m[i][2 - i])
    if t[0] == t[1] == t[2] and t[0] != 0:
        win = t[0]
    elif t[3] == t[4] == t[5] and t[3] != 0:
        win = t[0]
    return win, n


def input_l(m):
    while True:
        print("如果輸入非整數，程式會報錯並停止運行")
        l = input(f"{p[player]}請輸入位置(1~9): ")
        l = int(l)
        if 1 <= l <= 9:
            if m[x[l]][y[l]] == 0:
                return l
            else:
                print("輸入錯誤: 只能下在空白處")
        else:
            print("輸入錯誤: 需在1~9的範圍內")


def draw(m):
    for i in m:
        print("", end="|")
        for j in i:
            if j == 0:
                print(" ", end="|")
            elif j == 1:
                print("O", end="|")
            elif j == 2:
                print("X", end="|")
        print()


m = []
for _ in range(3):
    t = []
    for _ in range(3):
        t.append(0)
    m.append(t)
player = 1
p = (-1, "P1", "P2")
x = (-1, 2, 2, 2, 1, 1, 1, 0, 0, 0)
y = (-1, 0, 1, 2, 0, 1, 2, 0, 1, 2)
print("位置編號:\n7|8|9\n4|5|6\n1|2|3")
while True:
    l = input_l(m)
    m[x[l]][y[l]] = player
    if m[x[l]][y[l]] == 0:
        m[x[l]][y[l]] = player
    draw(m)
    if player == 1:
        player = 2
    else:
        player = 1
    win, n = check(m)
    if n == 9 and win == -1:
        print("平手")
        break
    elif win != -1:
        print(f"{p[win]}獲勝")
        break
