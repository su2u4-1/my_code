def difficulty() -> tuple[list[int], list[int], int]:
    a: list[int] = []
    e: list[int] = []
    f = 0
    try:
        t = input("請輸入難度:")
        if t == "exit":
            print("\n離開遊戲中")
            exit()
        f = int(t)
    except ValueError:
        print("輸入錯誤")
        return difficulty()
    for i in range(f):
        a.append(i + 1)
        e.append(i + 1)
    return a, e, f


def show(a: list[int], b: list[int], c: list[int], d: int):
    print()
    for i in range(d - 1, -1, -1):
        print(" ", str(a[i]) if len(a) > i else "|", " " * 7, str(b[i]) if len(b) > i else "|", " " * 7, str(c[i]) if len(c) > i else "|")
    print("第一座塔  第二座塔  第三座塔")


print("歡迎遊玩[河內塔]小遊戲^_^\n(輸入exit離開)")
a, ans, f = difficulty()
a.reverse()
m: tuple[list[int], list[int], list[int]] = (a, [], [])
ans.reverse()
n = 0
while True:
    show(m[0], m[1], m[2], f)
    d = input("\n要移動的塔+空格+要移去的塔:").split()
    if d[0] == "exit":
        print("\n離開遊戲")
        break
    try:
        d1, d2 = map(int, d)
    except:
        print("輸入錯誤: 輸入非數字")
        continue
    if d1 > 3 or d1 < 1 or d2 > 3 or d2 < 1 or d1 == d2:
        print("輸入錯誤: 輸入數字超過上限")
        continue
    d = m[d1 - 1].pop()
    if len(m[d2 - 1]) > 0 and d > m[d2 - 1][-1]:
        print("輸入錯誤: 大的不能疊在小的上面")
        m[d1 - 1].append(d)
        continue
    m[d2 - 1].append(d)
    n += 1
    if m[1] == ans or m[2] == ans and len(m[0]) == 0:
        show(m[0], m[1], m[2], f)
        print(f"\n你贏了,移動了{n}次,最佳步驟為{(2 ** f) -1}次")
        break
