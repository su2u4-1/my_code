import numpy as np

row, col = 6, 7
board = np.zeros((row, col), int)


def pc1():
    global s
    p = input("\n輪到玩家1\n請在1~7間選一個數字:")
    try:
        p = int(p)
    except ValueError:
        print("\n輸入錯誤")
        pc1()
    if p < 1 or p > 7:
        print("\n輸入錯誤")
        pc1()
    elif board[0][p - 1] != 0:
        print("\n此列已滿,請重新選擇")
        pc1()
    else:
        s = p


def pc2():
    global s
    p = input("\n輪到玩家2\n請在1~7間選一個數字:")
    try:
        p = int(p)
    except ValueError:
        print("\n輸入錯誤")
        pc2()
    if p < 1 or p > 7:
        print("\n輸入錯誤")
        pc2()
    elif board[0][p - 1] != 0:
        print("\n此列已滿,請重新選擇")
        pc2()
    else:
        s = p


def drop(x, y):
    while True:
        if x + 1 <= row - 1:
            if board[x + 1][y] == 0:
                board[x + 1][y] = board[x][y]
                board[x][y] = 0
                x += 1
            else:
                break
        else:
            break
    return


def check():
    a = [1, 1, 1, 0, 0, -1, -1, -1]
    b = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x in range(6):
        for y in range(7):
            if board[x][y] == 1:
                for i in range(8):
                    x1 = x
                    y1 = y
                    for _ in range(3):
                        if (
                            x1 + a[i] < 0
                            or x1 + a[i] > 5
                            or y1 + b[i] < 0
                            or y1 + b[i] > 6
                        ):
                            break
                        elif board[x1 + a[i]][y1 + b[i]] != 1:
                            break
                        x1 += a[i]
                        y1 += b[i]
                    else:
                        return 1
            elif board[x][y] == 2:
                for i in range(8):
                    x1 = x
                    y1 = y
                    for _ in range(3):
                        if (
                            x1 + a[i] < 0
                            or x1 + a[i] > 5
                            or y1 + b[i] < 0
                            or y1 + b[i] > 6
                        ):
                            break
                        elif board[x1 + a[i]][y1 + b[i]] != 2:
                            break
                        x1 += a[i]
                        y1 += b[i]
                    else:
                        return 2


side = 0
while True:
    if side == 0:
        pc1()
        p = s - 1
        board[0][p] = 1
    elif side == 1:
        pc2()
        p = s - 1
        board[0][p] = 2
    drop(0, p)
    print(f"\n{board}")
    if side == 0:
        side = 1
    elif side == 1:
        side = 0
    win = check()
    if win != None:
        break

if win == 1:
    print("\n玩家1獲勝")
elif win == 2:
    print("\n玩家2獲勝")
