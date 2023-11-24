from random import randint as ri

print("(輸入exit或0關閉遊戲)\n歡迎遊玩猜數字")
c = 0
while c != "exit" and c != "0":
    a = input("\n輸入要猜的數字上限:")
    if a == "exit" or a == "0":
        break
    else:
        try:
            a = int(a)
        except:
            print("輸入錯誤")
            continue
    b = ri(1, a)
    d = 0
    while c != b:
        c = input("\n請輸入你猜的數字:")
        d += 1
        if c == "exit" or c == "0":
            break
        else:
            try:
                c = int(c)
            except:
                print("輸入錯誤")
                continue
        if b == c:
            print(f"你猜對了,答案是{b},你猜了{d}輪")
            break
        elif b > c:
            print("太小了")
        elif b < c:
            print("太大了")
print("關閉此遊戲")
