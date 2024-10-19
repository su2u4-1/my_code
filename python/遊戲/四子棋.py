import numpy as np

row, col = 6, 7
board = np.zeros((row, col), int)


def pc() -> int:
    op = input(f"\n輪到玩家{side+1}\n請在1~7間選一個數字:")
    try:
        op = int(op)
    except ValueError:
        print("\n輸入非數字")
        return pc()
    if op < 1 or op > 7:
        print("\n輸入錯誤")
        return pc()
    elif board[0][op - 1] != 0:
        print("\n此列已滿,請重新選擇")
        return pc()
    else:
        return op


def drop(x: int, y: int) -> None:
    while True:
        if x + 1 <= row - 1 and board[x + 1][y] == 0:
            board[x + 1][y] = board[x][y]
            board[x][y] = 0
            x += 1
        else:
            break


def check():
    a = [1, 1, 1, 0, 0, -1, -1, -1]
    b = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x in range(6):
        for y in range(7):
            p = board[x][y]
            for i in range(8):
                x1 = x
                y1 = y
                for _ in range(3):
                    if x1 + a[i] < 0 or x1 + a[i] > 5 or y1 + b[i] < 0 or y1 + b[i] > 6 or board[x1 + a[i]][y1 + b[i]] != p:
                        break
                    x1 += a[i]
                    y1 += b[i]
                else:
                    return p


side = 0
while True:
    if side == 0:
        p = pc() - 1
        board[0][p] = 1
    else:
        p = pc() - 1
        board[0][p] = 2
    drop(0, p)
    print(f"\n{board}")
    side = 1 if side == 0 else 0
    win = check()
    if win != None:
        break

if win == 1:
    print("\n玩家1獲勝")
elif win == 2:
    print("\n玩家2獲勝")
