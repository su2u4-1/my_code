from random import random
from typing import NoReturn

# 初始資金
balance = 100000000  # 設定資金初值，1億

# 更新後的賠率和機率對應
odds = {
    "1/2": {"probability": 0.5, "multiplier": 1.85},
    "2/3": {"probability": 2 / 3, "multiplier": 1.32},
    "3/4": {"probability": 3 / 4, "multiplier": 1.2},
    "1/3": {"probability": 1 / 3, "multiplier": 2.75},
    "1/9": {"probability": 1 / 9, "multiplier": 8.8},
    "4/5": {"probability": 4 / 5, "multiplier": 1.15},
    "3/5": {"probability": 3 / 5, "multiplier": 1.55},
}


# 顯示歡迎界面
def show_welcome() -> None:
    print("\n\033[32m歡迎來到對賭程式！\033[0m")
    print(f"\033[33m當前資金: {balance} 元\033[0m")
    print("\033[36m可選擇的賠率和機率:\033[0m")
    for rate, details in odds.items():
        print(f"\033[33m{rate}: 機率 {details['probability'] * 100}% 賠率 {details['multiplier']}\033[0m")
    print("\n\033[36m請選擇一個賠率來進行下注，這個選擇將適用於所有後續的賭局。\033[0m")


# 設置初始賠率
def set_initial_odds() -> str:
    while True:
        print("\033[36m請選擇您想要的賠率：\033[0m")
        for rate in odds:
            print("\033[33m" + rate + "\033[0m")
        chosen_odds = input("\033[32m請輸入賠率（例如 '1/2'）：\033[0m").strip()

        if chosen_odds in odds:
            print(f"\033[32m您選擇了賠率 {chosen_odds}\033[0m")
            return chosen_odds
        else:
            print("\033[31m無效的選擇，請重新選擇。\033[0m")


# 進行賭局
def make_bet(chosen_odds: str) -> None:
    global balance
    print("\n\033[36m選擇您要參加的賭局\033[31m(提示：輸入'exit'關閉程式)\033[0m")
    try:
        v = input(f"\033[32m請輸入賭注金額（剩餘資金 {balance} 元）: \033[0m")
        if v == "exit":
            exit_program()
        bet_amount = float(v)
    except ValueError:
        print("\033[31m賭注金額無效，請確保輸入的是數字。\033[0m")
        return

    # 破產檢查
    if balance <= 0:
        print("\033[31m你破產了。\033[0m")
        exit_program()

    # 檢查賭注金額是否合法
    if bet_amount <= 0 or bet_amount > balance:
        print("\033[31m賭注金額無效，請確保您的賭注金額大於 0 且不超過剩餘資金。\033[0m")
        return

    # 確定賠率和機率
    prob = odds[chosen_odds]["probability"]
    multiplier = odds[chosen_odds]["multiplier"]

    # 隨機決定是否中獎
    outcome = random()  # 隨機生成 0 到 1 之間的浮動數
    print(f"\033[36m隨機結果: {outcome:.4f}\033[0m")

    if outcome <= prob:  # 如果隨機結果小於等於選擇的機率，表示中獎
        win_amount = bet_amount * multiplier
        balance += win_amount - bet_amount  # 贏得賠率後獲得的金額，扣除原賭注
        print(f"\033[32m白羊毛噴出！您中獎了！您獲得了 {win_amount - bet_amount:.2f} 元，當前資金為 \033[0m{balance:.2f} 元。")
    else:  # 否則為黑羊毛
        balance -= bet_amount  # 輸掉賭注
        print(f"\033[31m黑羊毛噴出！很遺憾，您沒中獎。您失去了 \033[0m{bet_amount:.2f} 元，當前資金為 {balance:.2f} 元。")


# 退出程序
def exit_program() -> NoReturn:
    print(f"\033[32m您最終的資金為 \033[0m{balance:.2f} 元。感謝遊玩！")
    exit()


# 程式入口
if __name__ == "__main__":
    show_welcome()

    # 用戶選擇一個賠率
    chosen_odds = set_initial_odds()

    # 無限循環賭局
    while True:
        make_bet(chosen_odds)
