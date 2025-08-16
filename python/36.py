from random import randint
from typing import Callable, Optional


def get_int(prompt: str, err_msg_1: str, err_msg_2: str, condition: Callable[[int], bool]) -> int:
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            print(err_msg_2)
        except ValueError:
            print(err_msg_1)


player_n = get_int("請輸入玩家數量: ", "請輸入整數", "請輸入正整數", lambda x: x > 0)
player_money: list[Optional[int]] = []
player_profit: list[int] = [0 for _ in range(player_n)]
for i in range(player_n):
    t = get_int(f"請輸入玩家{i + 1}的本金數量，如果為無限請輸入0: ", "請輸入整數", "請輸入0或正整數", lambda x: x >= 0)
    player_money.append(t if t != 0 else None)
t = get_int("請輸入莊家的本金數量，如果為無限請輸入0: ", "請輸入整數", "請輸入0或正整數", lambda x: x >= 0)
banker_money = t if t != 0 else None
banker_profit = 0
while True:
    broad: list[list[tuple[int, int]]] = [[], [], [], [], [], []]
    if banker_money is not None and banker_money <= 0:
        print("\n莊家已經破產，遊戲結束！")
        break
    if all(money is not None and money <= 0 for money in player_money):
        print("\n所有玩家都已經破產，遊戲結束！")
        break
    print("\n目前情況:")
    for i, money in enumerate(player_money):
        if money is None:
            print(f"    玩家 {i + 1} 的本金為無限，利潤: {player_profit[i]}")
        else:
            print(f"    玩家 {i + 1} 的本金: {money}，利潤: {player_profit[i]}")
    if banker_money is not None:
        print(f"莊家的本金: {banker_money}，利潤: {banker_profit}")
    else:
        print(f"莊家的本金為無限，利潤: {banker_profit}")
    dice_result = (randint(1, 6), randint(1, 6), randint(1, 6))
    print("\n莊家擲骰結束，玩家開始下注")
    player_b: list[int] = [0 for _ in range(player_n)] + [0]
    f = False
    for i in range(player_n):
        while True:
            position = get_int(f"玩家{i + 1}請輸入要下注的位置 (1-6), 停止下注請輸入0: ", "請輸入整數", "請輸入1-6之間的整數", lambda x: 0 <= x <= 6)
            if position == 0:
                if f:
                    print(f"玩家{i + 1}停止下注")
                    break
                print(f"玩家{i + 1}還沒下注過，請至少下注一次")
                continue
            f = True
            if player_money[i] is None:
                bet = get_int(f"玩家{i + 1}請輸入下注金額: ", "請輸入整數", "請輸入正整數", lambda x: 0 < x)
                print(f"玩家{i + 1}下注 {bet}")
            else:
                bet = get_int(f"玩家{i + 1}請輸入下注金額: ", "請輸入整數", "請輸入正整數且須小於剩餘金額", lambda x: 0 < x <= player_money[i])
                print(f"玩家{i + 1}下注 {bet}，剩餘本金 {player_money[i] - bet}")
                player_money[i] -= bet
            player_profit[i] -= bet
            player_b[i] -= bet
            if banker_money is not None:
                banker_money += bet
            banker_profit += bet
            player_b[-1] += bet
            broad[position - 1].append((i, bet))
    print("\n下注情況:")
    for i, bets in enumerate(broad):
        if bets:
            print(f"    位置 {i + 1} 的下注:")
            for player, bet in bets:
                print(f"        玩家 {player + 1} 下注 {bet}")
        else:
            print(f"    位置 {i + 1} 沒有下注")
    print(f"\n擲骰結果: {dice_result}")
    for position in range(6):
        if position + 1 in dice_result:
            for player, bet in broad[position]:
                bet *= dice_result.count(position + 1) + 1
                player_profit[player] += bet
                player_b[player] += bet
                banker_profit -= bet
                player_b[-1] -= bet
                if banker_money is not None:
                    banker_money -= bet
                if player_money[player] is not None:
                    player_money[player] += bet
    print("\n結算:")
    for i, b in enumerate(player_b):
        print(f"    玩家 {i + 1}" if i < player_n else "    莊家", end=" ")
        if b > 0:
            print(f"贏得 {b}")
        elif b < 0:
            print(f"損失 {-b}")
        else:
            print("沒輸沒贏")
