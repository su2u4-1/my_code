import random


def bag_add(item, quantity):
    global money, bag_space, bag
    s = 0
    for i in range(len(item_list)):
        s += bag[item_list[i]]
    if bag_space - s >= quantity:
        bag[item] += quantity
        print(f"bag add【{item}】x{quantity}")
    elif bag_space - s < quantity and bag_space - s > 0:
        bag[item] += bag_space - s
        print(f"bag add【{item}】x{bag_space-s}")
        print(f"由於背包空間不足,將丟棄【{item}】x{quantity-(bag_space-s)}")
        b = input("是否擴大背包\t[1]是(花費【金錢】x{bag_space})  [2]否")
        if b == "1":
            money -= bag_space
            bag_space += 1


def show_bag():
    print(f"0:背包空間\t{bag_space}個")
    for i in range(len(item_list)):
        if bag[item_list[i]] > 0:
            print(f"{i+1}:【{item_list[i]}】\t{bag[item_list[i]]}個")


a = 0
ps = 10
bag_space = 100
money = 1000
job = ""
bag = {
    "石頭": 0,
    "煤礦": 0,
    "鐵礦": 0,
    "金礦": 0,
    "鑽石礦": 0,
    "石磚": 0,
    "煤炭": 0,
    "鐵錠": 0,
    "金錠": 0,
    "鑽石": 0,
    "稻米": 1,
    "小麥": 1,
    "地瓜": 1,
    "馬鈴薯": 1,
    "玉米": 1,
}
item_list = [
    "石頭",
    "煤礦",
    "鐵礦",
    "金礦",
    "鑽石礦",
    "石磚",
    "煤炭",
    "鐵錠",
    "金錠",
    "鑽石",
    "稻米",
    "小麥",
    "地瓜",
    "馬鈴薯",
    "玉米",
]
print("輸入help查詢\n輸入exit離開遊戲")
while True:
    if a == 0:
        print("請選擇接下來要做的事")
        b = input("[1]轉職/[2]工作/[3]吃飯/[4]買賣/[5]物品:")
        if b == "exit":
            break
        elif b == "1":
            a = 1
        elif b == "2":
            a = 2
        elif b == "3":
            a = 3
        elif b == "4":
            a = 4
        elif b == "5":
            a = 5
        elif a == "exit":
            break
        else:
            a = 0
    if a == 1:
        print("請選擇職業")
        b = input("[1]農夫/[2]劍士/[3]藥劑師/[4]法師/[5]礦工/[6]牧羊人/[7]鐵匠/[8]伐木工:")
        if b == "exit":
            break
        elif b == "1":
            job = "農夫"
        elif b == "2":
            job = "劍士"
        elif b == "3":
            job = "藥劑師"
        elif b == "4":
            job = "法師"
        elif b == "5":
            job = "礦工"
        elif b == "6":
            job = "牧羊人"
        elif b == "7":
            job = "鐵匠"
        elif b == "8":
            job = "伐木工"
        elif b == "exit":
            break
        if len(job) > 1:
            print(f"你轉職成了{job}")
            a = 0
        else:
            print("輸入錯誤")
    if a == 2:
        print("準備開始工作")
        while job == "農夫":
            for i in range(10, 15):
                print(f"{i-9}:【{item_list[i]}】剩餘{bag[item_list[i]]}個")
            b = input("請選擇種子(輸入編號):")
            # 農田編號，選擇種植，除草、除蟲、澆水、施肥、收成
        while job == "礦工":
            event_list = ["什麼都沒有", "石頭", "煤礦", "鐵礦", "金礦", "鑽石礦"]
            b = input("按enter鍵繼續\t輸入end結束")
            # 挖掘時間
            if b == "end":
                print("結束工作")
                a = 0
                break
            elif b == "exit":
                exit()
            else:
                if ps <= 0:
                    print("體力不足，工作結束")
                    a = 0
                    break
                elif ps > 0:
                    event = random.choices(event_list, [40, 40, 10, 5, 4, 1])
                    c = random.randint(1, 3)
                    ps -= 1
                    if event[0] == "什麼都沒有":
                        print(f"你什麼都沒看到")
                    else:
                        print(f"你遇上了【{event[0]}】獲得[{c}]個【{event[0]}】")
                        bag_add(event[0], c)
    if a == 5:
        show_bag()
        b = input("按enter鍵離開")
        if b == "exit":
            break
        a = 0
    a = 0
exit()
