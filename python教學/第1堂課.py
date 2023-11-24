# 載入模組
import random

# [\n]是換行的意思
print("歡迎玩猜數字遊戲")
# 輸入資料
up = input("\n輸入猜數字的數字上限:")
# 把up的類別從字串(str)改成整數(int)
up = int(up)
# 把answer設定成一個隨機數字,範圍是1到up
answer = random.randint(1, up)
r = 0
# 無限迴圈
while True:
    # 接受輸入並將類別從字串改成整數
    n = int(input("請輸入你猜的數字:"))
    # 把r的數字加一
    r = r + 1  # 等同於r += 1
    if answer == n:
        # %d只能接受數字，它會把後面括號裡的變數按順序放到前面的%d或其他的%[某個英文字母]裡面
        print("你猜對了，答案是%d，你猜了%d輪" % (answer, r))
        # 在字串前方加f就可以把後方{}內的變數直接代入
        print(f"你猜對了，答案是{answer}，你猜了{r}輪")
        # 離開迴圈
        break
    if answer > n:
        print("太小了")
    if answer < n:
        print("太大了")
