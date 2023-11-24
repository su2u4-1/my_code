a = []
b = []
c = []
e = []
n = 0
f = 0


def difficulty():
    global f, a, e
    f = input("請輸入難度:")
    if f == "exit":
        print("\n離開遊戲中")
        exit()
    else:
        try:
            f = int(f)
        except:
            print("輸入錯誤")
            difficulty()
        for i in range(f):
            a.append(i + 1)
            e.append(i + 1)


print("歡迎遊玩[河內塔]小遊戲^_^\n(輸入exit離開)")
difficulty()
a.reverse()
e.reverse()
while True:
    print("\n第一座塔", end=":")
    for i in a:
        print(i, end=",")
    print("\n第二座塔", end=":")
    for i in b:
        print(i, end=",")
    print("\n第三座塔", end=":")
    for i in c:
        print(i, end=",")
    d = input("\n要移動的塔+空格+要移去的塔:").split()
    n += 1
    if d[0] == "exit":
        print("\n離開遊戲中")
        break
    try:
        d1 = int(d[0])
        d2 = int(d[1])
    except:
        print("輸入錯誤")
        n -= 1
        continue
    if d1 > 3 or d1 < 1 or d2 > 3 or d2 < 1 or d1 == d2:
        print("輸入錯誤")
        n -= 1
        continue
    if d1 == 1:
        d = a.pop()
    elif d1 == 2:
        d = b.pop()
    elif d1 == 3:
        d = c.pop()
    if d2 == 1:
        try:
            if d > a[-1]:
                print("輸入錯誤")
                n -= 1
                if d1 == 2:
                    b.append(d)
                elif d1 == 3:
                    c.append(d)
                continue
            else:
                a.append(d)
        except IndexError:
            a.append(d)
    elif d2 == 2:
        try:
            if d > b[-1]:
                print("輸入錯誤")
                n -= 1
                if d1 == 1:
                    a.append(d)
                elif d1 == 3:
                    c.append(d)
                continue
            else:
                b.append(d)
        except IndexError:
            b.append(d)
    elif d2 == 3:
        try:
            if d > c[-1]:
                print("輸入錯誤")
                n -= 1
                if d1 == 1:
                    a.append(d)
                elif d1 == 2:
                    b.append(d)
                continue
            else:
                c.append(d)
        except IndexError:
            c.append(d)
    if b == e or c == e:
        if len(a) == 0:
            print(f"\n你贏了,移動了{n}次,最佳步驟為{(2**f)-1}次")
            break
