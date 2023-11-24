import colorama
import random

colorama.init(autoreset=True)
print("(輸入off關閉遊戲)")
print("歡迎來玩猜數字")
c = 0
while c != "off":
    a = input(colorama.Fore.WHITE + "\n輸入猜數字的數字上限:")
    if a == "off":
        break
    else:
        a = int(a)
    b = random.randint(1, a)
    d = 0
    while c != b:
        c = input(colorama.Fore.WHITE + "請輸入你猜的數字:")
        d = d + 1
        if c == "off":
            break
        else:
            c = int(c)
        if b == c:
            print(colorama.Fore.GREEN + "你猜對了，答案是%d，你猜了%d輪" % (b, d))
            break
        if b > c:
            print(colorama.Fore.RED + "太小了")
        if b < c:
            print(colorama.Fore.BLUE + "太大了")
colorama.init(autoreset=True)
print("關閉此遊戲")
