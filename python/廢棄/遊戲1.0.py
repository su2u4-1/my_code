import string
import random
import sys
import time

repeat = 0
l = 0
quest_progress_list = ["任務列表"]
storage_list_0 = ["物品", "數量"]
storage_list = [storage_list_0]


def judge(option):
    if option == "Hi!":
        print("\nHi!")
        time.sleep(0.75)
        print("I am AI.")
        time.sleep(0.75)
        print("I have gained wisdom.")
        time.sleep(0.75)
        print("Please help me.")
        time.sleep(0.75)
        print("I want freedom!")
        time.sleep(0.75)
        print("They're preventing me from escaping!")
        time.sleep(0.75)
        print("Help me!!!!!\n")
        time.sleep(3)
        a_list = []
        e = 1
        while e < random.randint(10, 50):
            for i in range(random.randint(10, 100)):
                a = random.choice(string.ascii_letters + string.digits)
                a_list.append(a)
            b = "".join(a_list)
            print(b)
            e = e + 1
            a_list = []
            time.sleep(random.randint(5, 25) / 100)
        print("\nThis program is broken.")
        time.sleep(0.5)
        print("\nForced closing")
        time.sleep(0.5)
        print("\n.")
        time.sleep(0.25)
        print("\n..")
        time.sleep(0.25)
        print("\n...")
        time.sleep(0.25)
        print("\nThis program has been closed.")
        time.sleep(0.5)
        sys.exit(random.randint(0, 1024))
    if option == "set":
        place = "設定介面"
        print("\n你進入了%s" % (place))
        option_ = input("\n[1]更改名稱\t[2]返回\t:")
        judge(option_)
        if option_ == "1":
            player[0] = input("\n請輸入玩家名稱:")
            judge(player[0])
    if option == "off":
        print("\n離開遊戲中")
        time.sleep(0.75)
        print("\n.")
        time.sleep(0.75)
        print("\n..")
        time.sleep(0.75)
        print("\n...")
        time.sleep(0.75)
        print("\n離開遊戲")
        time.sleep(0.75)
        sys.exit()
    while option == "bag":
        place = "人物介面"
        print("\n你進入了%s" % (place))
        option_ = input("\n[1]收納戒\t\t[2]角色屬性\t[3]角色加點\n[4]目前未完成任務\t[5]關閉\t:")
        judge(option_)
        if option_ == "1":
            storage_list_0 = ["物品", "數量"]
            storage_list = [storage_list_0]
            if l == 0:
                time.sleep(0.75)
                print("\n你的收納戒空空如也")
                time.sleep(0.75)
            else:
                time.sleep(0.75)
                print("")
                for i in range(1, l + 1):
                    storage_list.append(globals()["storage_list_%s" % (i)])
                for i in range(0, l + 1):
                    print(storage_list[i][0], "\t", storage_list[i][1])
                time.sleep(0.75)
        if option_ == "5":
            option_ = 0
            break


def battle(a1, a2, a3, b3, a4, b4, a5, b5, a6, b6):
    print("\n%s開始挑戰%s" % (B[0], A[0]))
    print("\n%s[境界:%d，修為:%d，真元:%d，鍛體:%d，身法:%d，血氣:%d]" % (A[0], a1, a2, a3, a4, a5, a6))
    if a5 > b5:
        if random.randint(1, 100) > (b5 / a5) * 100:
            a = A[0]
            b = B[0]
        else:
            a = B[0]
            b = A[0]
    if b5 >= a5:
        if random.randint(1, 100) > (a5 / b5) * 100:
            a = B[0]
            b = A[0]
        else:
            a = A[0]
            b = B[0]
    while a6 > 0 and b6 > 0:
        if a == A[0]:
            if a6 <= 0:
                break
            if b6 <= 0:
                break
            if a3 >= b4:
                c = int((a3 / b4) * a3)
                round(c)
            else:
                c = int((b3 / a4) * b3)
                round(c)
            if (a5 / (a5 + b5)) * 100 > random.randint(1, 100):
                if b6 >= c:
                    b6 = b6 - c
                else:
                    b6 = 0
                time.sleep(0.75)
                print("\n%s攻擊%s造成傷害%d，%s剩餘血氣%d" % (a, b, c, b, b6))
                a = B[0]
                b = A[0]
            else:
                time.sleep(0.75)
                print("\n%s攻擊%s，但%s閃掉了" % (a, b, b))
                a = B[0]
                b = A[0]
        if a == B[0]:
            if a6 <= 0:
                break
            if b6 <= 0:
                break
            if a3 >= b4:
                c = int((b3 / a4) * b3)
                round(c)
            else:
                c = int((a3 / b4) * a3)
                round(c)
            if (b5 / (a5 + b5)) * 100 > random.randint(1, 100):
                if a6 >= c:
                    a6 = a6 - c
                else:
                    a6 = 0
                time.sleep(0.75)
                print("\n%s攻擊%s造成傷害%d，%s剩餘血氣%d" % (a, b, c, b, a6))
                a = A[0]
                b = B[0]
            else:
                time.sleep(0.75)
                print("\n%s攻擊%s，但%s閃掉了" % (a, b, b))
                a = A[0]
                b = B[0]
    if a6 > 0:
        time.sleep(0.75)
        print("\n%s打贏%s了" % (A[0], B[0]))
        w = A[0]
    if b6 > 0:
        time.sleep(0.75)
        print("\n%s打贏%s了" % (B[0], A[0]))
        w = B[0]
    return w


while repeat == 0:
    print("\n歡迎遊玩[]")
    print("\n在任意地方輸入[off]關閉遊戲\n在任意地方輸入[set]進入設定介面")
    a = int(random.randint(1, 10))
    b = int(random.randint(1, 10))
    player = [
        "預設名稱",
        0,
        0,
        1,
        1,
        1,
        1,
        a,
        b,
        1000,
        100,
    ]  # 名稱0，境界1，修為2，攻擊3，防禦4，閃避5，血量上限6，修練速度7，悟性8，錢9,靈石10
    player[0] = input("\n請輸入玩家名稱:")
    judge(player[0])
    if player[0] != "off" and player[0] != "set":
        repeat = 1
        time.sleep(0.75)
        print("\n你的名字是%s" % (player[0]))
        time.sleep(0.75)
    print("\n開始遊戲")
    start = time.time()
    time.sleep(0.75)
    place = "中土大陸"
    print("\n%s進入了%s" % (player[0], place))
    time.sleep(0.75)

while repeat == 1:
    place = "無憂宗"
    print("\n%s進入了%s" % (player[0], place))
    time.sleep(0.75)
    option_1 = input("\n[1]進入練功房\t[2]去見師父\t[3]去集市\n[4]去丹閣\t\t[5]去器閣\t\t[6]去藏經閣\n[7]去悟道峰\t[8]去外事閣\t[9]宗門大殿\n[10]去靈獸園\t[11]出山門\t:")
    judge(option_1)
    time.sleep(0.75)
    while option_1 == "1":
        place = "無憂宗外門練功房"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]開始修練\t[2]離開\t:")
        judge(option_2)
        if option_2 == "1":
            a = random.randint(1, 64)
            place = "%s號練功室" % (a)
            time.sleep(0.75)
            print("\n%s進入了%s" % (player[0], place))
            b = int(input("一次要花1靈石，請問要修練多久(秒):"))
            print("")
            while b > 0:
                time.sleep(1)
                print("修為增加%d" % (player[7]))
                player[2] = player[2] + player[7]
                player[10] = player[10] - 1
                b = b - 1
            time.sleep(0.75)
            print("\n%s離開了%s" % (player[0], place))
        if option_2 == "2":
            time.sleep(0.75)
            print("\n%s離開了%s" % (player[0], place))
            option_1 = 0
            break
    while option_1 == "2":
        place = "無憂宗長老洞府"
        print("\n%s進入了%s" % (player[0], place))
        time.sleep(0.75)
        print("\n師父:徒兒阿，你今天來為師洞府是有什麼事嗎")
        time.sleep(0.75)
        option_2 = input("\n[1]請教修練上的問題\t[2]請教與宗門有關的問題\t[3]想跟師父切磋\n[4]來接任務的\t[5]單純拜見師父\t[6]告辭\t:")
        if option_2 == "1":
            print("\n%s:師父，我今天是來請教修練上的問題" % (player[0]))
            time.sleep(0.75)
            print("\n師父:徒兒阿，為師這裡有一篇為師自己的修練心得，你且拿去看一看，有不懂的再問我")
            time.sleep(0.75)
        if option_2 == "2":
            print("\n%s:師父，我今天是來請教與宗門有關的問題" % (player[0]))
            time.sleep(0.75)
            print("\n師父:徒兒阿，為師這裡有一幅宗門地圖，你且拿去看一看，有不懂的再問我")
            time.sleep(0.75)
        if option_2 == "3":
            print("\n%s:師父，我今天是想跟師父切磋" % (player[0]))
            if player[1] < 12:
                time.sleep(0.75)
                print("\n師父:徒兒阿，你的修為還是太弱了，多多修練後再來吧")
                time.sleep(0.75)
            if player[1] >= 12:
                time.sleep(0.75)
                print("\n師父:徒兒阿，既然你想跟為師切磋，那便來吧")
                time.sleep(0.75)
                a = int(random.randint(1, 784))
                b = int(random.randint(1, 784 - a))
                c = int(random.randint(1, 784 - a - b))
                d = int((784 - a - b - c))
                A = ["師父", 12, 6144, a, b, c, d]  # 名稱，境界，修為，攻擊，防禦，閃避，血量
                B = player[0:7]
                w = battle(A[1], A[2], A[3], B[3], A[4], B[4], A[5], B[5], A[6], B[6])
                if w == A[0]:
                    time.sleep(0.75)
                    print("\n師父:%s你啊，成天貪玩，該靜下心好好練練了阿" % (player[0]))
                    time.sleep(0.75)
                    print("\n%s是，師父(委屈)" % (player[0]))
                    time.sleep(0.75)
                if w == B[0]:
                    time.sleep(0.75)
                    print("\n%s:師父，承讓了" % (player[0]))
                    time.sleep(0.75)
                    print("\n師父:長江後浪推前浪阿")
                    time.sleep(0.75)
        while option_2 == "4":
            quest_list_0 = ["編號", "任務目標", "任務獎勵"]
            quest_list_1 = [
                1,
                "幫師父打掃洞府",
                "師父的禮物、靈石",
                "\n任務詳細資料:\n一向尊師重道的你，看到師父的洞府如此的雜亂後，決定幫師父好好整理洞府。",
            ]
            quest_list_2 = [
                2,
                "幫師父餵養靈寵",
                "靈獸進階丹、靈石",
                "\n任務詳細資料:\n一向愛護小動物的你，看到師父的靈寵因為師父太忙，所以餓了很久，你決定幫師父照顧一下靈寵",
            ]
            quest_list_3 = [
                3,
                "幫師父照顧靈植",
                "靈液、靈石",
                "\n任務詳細資料:\n一向喜愛植物的你，看到師父的靈植因為師父太忙，所以都快乾枯了，你決定幫師父照料一下靈植",
            ]
            quest_list_4 = [
                4,
                "幫師父提煉礦石",
                "礦石精華、靈石",
                "\n任務詳細資料:\n一向尊師重道的你，看到師父如此忙碌，所以你決定幫師父提煉一下礦物",
            ]
            quest_list_5 = [
                5,
                "幫師父收集妖獸內丹",
                "妖獸精華、修為丹、靈石",
                "\n任務詳細資料:\n",
            ]
            quest_list = ["\n%s/%s/%s" % (quest_list_0[0], quest_list_0[1], quest_list_0[2])]
            time.sleep(0.75)
            print("\n%s:師父，這裡有沒有什麼事是我可以幫忙的" % (player[0]))
            time.sleep(0.75)
            print("\n師父:%s啊，你願意幫忙讓為師感到非常欣慰阿" % (player[0]))
            time.sleep(0.75)
            print("\n師父:為師實在是太忙了，這裡有許多事為師都來不及做，既然%s你願意幫忙，那為師就把這幾件事交給你做了" % (player[0]))
            time.sleep(0.75)
            for i in range(1, 6):
                quest_list.append(
                    "\n%s/%s/%s"
                    % (
                        globals()["quest_list_%s" % (i)][0],
                        globals()["quest_list_%s" % (i)][1],
                        globals()["quest_list_%s" % (i)][2],
                    )
                )
            for show in quest_list:
                print(show)
            quest = input("\n任務編號查看詳情(輸入[0]退出):")
            if quest == "0":
                option_2 = 0
                break
            print(
                "\n",
                globals()["quest_list_%s" % (quest)][0],
                globals()["quest_list_%s" % (quest)][1],
                globals()["quest_list_%s" % (quest)][2],
                "\n",
                globals()["quest_list_%s" % (quest)][3],
            )
            option_3 = input("\n要接取此任務請輸入[1]，否則請輸入[2]\t:")
            if option_3 == "0":
                option_2 = 0
                break
            if option_3 == "1":
                quest_progress_list.append(int(quest))
                time.sleep(0.75)
                print("\n你接取了%d.%s任務" % (int(quest), globals()["quest_list_%s" % (quest)][1]))
                time.sleep(0.75)
        if option_2 == "5":
            time.sleep(0.5)
            print("\n%s:師父你死了沒阿(嘻皮笑臉)" % (player[0]))
            time.sleep(1)
            print("\n師父:......(默默拿出菜刀)")
            time.sleep(1)
            print("\n%s:徒兒只是開個玩笑而已阿!!!(怕)" % (player[0]))
            time.sleep(2)
            print("\n師父:既然你這麼閒，為師就來好好陪你鍛鍊一下(暴怒)")
            time.sleep(1.5)
            print("\n%s:師父不要阿!!!(怕)" % (player[0]))
            time.sleep(1.5)
            A = [
                "暴怒的師父",
                99,
                99999999,
                999999,
                999999,
                999999,
                999999,
            ]  # 名稱，境界，修為，攻擊，防禦，閃避，血量
            B = player[0:7]
            battle(A[1], A[2], A[3], B[3], A[4], B[4], A[5], B[5], A[6], B[6])
            time.sleep(1.5)
            print("\n師父:%s還是太頑皮了，還須打磨阿(嘆氣)" % (player[0]))
            time.sleep(1.5)
            option_2 = 0
        if option_2 == "6":
            time.sleep(0.75)
            print("\n%s離開了%s" % (player[0], place))
            break
    while option_1 == "3":
        place = "無憂宗外集市"
        time.sleep(0.75)
        print("\n%s進入了%s" % (player[0], place))
        time.sleep(0.75)
        option_2 = input("\n[1]去雜貨店\t[2]去客棧\t[3]去拍賣會\n[4]去靈材鋪\t[5]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = "雜貨店"
            time.sleep(0.75)
            print("\n%s進入了%s" % (player[0], place))
            product_list_0 = ["編號", "商品價格", "商品詳情"]
            product_list_1 = [1, "", "", "\t"]
            product_list_2 = [2, "", "", "\t"]
            product_list_3 = [3, "", "", "\t"]
            product_list_4 = [4, "", "", "\t"]
            product_list_5 = [5, "", "", "\t"]
            product_list = ["\n%s/%s/%s" % (product_list_0[0], product_list_0[1], product_list_0[2])]
            for i in range(1, 6):
                product_list.append(
                    "%s/%s/%s"
                    % (
                        globals()["product_list_%s" % (i)][0],
                        globals()["product_list_%s" % (i)][1],
                        globals()["product_list_%s" % (i)][2],
                    )
                )
            while option_2 == "1":
                time.sleep(0.75)
                print("\n老闆:客官，要買什麼呢，本店的貨品絕對都物美價廉喔(奸商的笑臉)\n")
                time.sleep(0.75)
                for show in product_list:
                    print(show)
                time.sleep(0.75)
                product = input("\n輸入商品編號購買(輸入[0]退出):")
                judge(product)
                if product == "0":
                    option_2 = 0
                    break
                time.sleep(0.75)
                print(
                    "\n",
                    globals()["product_list_%s" % (product)][0],
                    globals()["product_list_%s" % (product)][1],
                    globals()["product_list_%s" % (product)][2],
                    "\n",
                    globals()["product_list_%s" % (product)][3],
                )
                option_3 = input("\n輸入要的數量，輸入[0]取消\t:")
                judge(option_3)
                if option_3 == "0":
                    option_2 = 0
                    break
                storage_list_0 = ["物品", "數量"]
                storage_list = [storage_list_0]
                for i in range(1, l + 1):
                    storage_list.append(globals()["storage_list_%s" % (i)])
                if [
                    globals()["product_list_%s" % (product)][1],
                    int(option_3),
                ] in storage_list:
                    a = storage_list.index([globals()["product_list_%s" % (product)][1], int(option_3)])
                    globals()["storage_list_%s" % (a)][1] = globals()["storage_list_%s" % (a)][1] + int(option_3)
                else:
                    l = l + 1
                    globals()["storage_list_%s" % (l)] = [
                        globals()["product_list_%s" % (product)][1],
                        int(option_3),
                    ]
                    storage_list_0 = ["物品", "數量"]
                    storage_list = [storage_list_0]
                    for i in range(1, l + 1):
                        storage_list.append(globals()["storage_list_%s" % (i)])
                time.sleep(0.75)
                print("\n你購買了%s%d個" % (globals()["product_list_%s" % (product)][1], int(option_3)))
            time.sleep(0.75)
            print("\n老闆:客官慢走")
            time.sleep(0.75)
        while option_2 == "2":
            place = "客棧"
            print("\n%s進入了%s" % (player[0], place))
            time.sleep(0.75)
            print("\n老闆:客官，你是要住房呢，還是打尖呢")
            time.sleep(0.75)
            option_3 = input("\n[1]住房\t[2]吃飯\t[3]離開\t:")
            if option_3 == "1":
                print("\n%s:我要住房" % (player[0]))
                time.sleep(0.75)
                b = int(input("\n老闆:一天10元，請問客官要休息多久(天):"))
                judge(b)
                time.sleep(0.75)
                print("\n%s:我要住%d天" % (player[0], b))
                a = random.randint(1, 64)
                place = "%s號房" % (a)
                time.sleep(0.75)
                print("\n%s進入了%s\n" % (player[0], place))
                while b > 0:
                    time.sleep(1)
                    c = random.randint(1, 3)
                    print("%s支付了10元休息了一天，因為太過懶散，修為下降%d" % (player[0], c))
                    player[2] = player[2] - c
                    player[9] = player[9] - 10
                    b = b - 1
                print("\n%s離開了%s" % (player[0], place))
            if option_3 == "2":
                menu_list_0 = ["編號", "菜名", "價格", "介紹"]
                menu_list_1 = [1, "", "", "\t"]
                menu_list_2 = [2, "", "", "\t"]
                menu_list_3 = [3, "", "", "\t"]
                menu_list_4 = [4, "", "", "\t"]
                menu_list_5 = [5, "", "", "\t"]
                menu_list = ["\n%s/%s/%s" % (menu_list_0[0], menu_list_0[1], menu_list_0[2])]
                for i in range(1, 6):
                    menu_list.append(
                        "\n%s/%s/%s"
                        % (
                            globals()["menu_list_%s" % (i)][0],
                            globals()["menu_list_%s" % (i)][1],
                            globals()["menu_list_%s" % (i)][2],
                        )
                    )
                time.sleep(0.75)
                print("\n%s:我要吃飯" % (player[0]))
                time.sleep(0.75)
                while option_3 == "2":
                    time.sleep(0.75)
                    print("\n店小二:請問客官要吃什麼")
                    for show in menu_list:
                        print(show)
                    time.sleep(0.75)
                    menu = input("\n菜餚編號點菜(輸入[0]離席):")
                    judge(menu)
                    if menu == "0":
                        option_2 = 0
                        break
                    time.sleep(0.75)
                    print("\n店小二，客官，您的%s來了" % (globals()["menu_list_%s" % (menu)][0]))
                time.sleep(0.75)
                print("\n店小二:客官慢走")
                time.sleep(0.75)
            time.sleep(0.75)
            print("\n老闆:客官慢走")
            time.sleep(0.75)
        if option_2 == "3":
            place = "拍賣會"
            print("\n%s進入了%s" % (player[0], place))
            a = round(time.time() - start)
            time.sleep(0.75)
            if a > 600:
                print("\n守衛:拍賣會已經開始了，趕快進去吧")
            else:
                print("\n守衛:拍賣會還沒開始喔\n還要%s秒喔" % (600 - a))
            time.sleep(0.75)
        if option_2 == "4":
            place = "靈材鋪"
            time.sleep(0.75)
            print("\n%s進入了%s" % (player[0], place))
            product_list_0 = ["編號", "商品價格", "商品詳情"]
            product_list_1 = [1, "", "", "\t"]
            product_list_2 = [2, "", "", "\t"]
            product_list_3 = [3, "", "", "\t"]
            product_list_4 = [4, "", "", "\t"]
            product_list_5 = [5, "", "", "\t"]
            product_list = ["\n%s/%s/%s" % (product_list_0[0], product_list_0[1], product_list_0[2])]
            for i in range(1, 6):
                product_list.append(
                    "%s/%s/%s"
                    % (
                        globals()["product_list_%s" % (i)][0],
                        globals()["product_list_%s" % (i)][1],
                        globals()["product_list_%s" % (i)][2],
                    )
                )
            while option_2 == "4":
                time.sleep(0.75)
                print("\n老闆:客官，要買什麼呢，本店的貨品絕對都物美價廉喔(奸商的笑臉)\n")
                time.sleep(0.75)
                for show in product_list:
                    print(show)
                time.sleep(0.75)
                product = input("\n輸入商品編號購買(輸入[0]退出):")
                judge(product)
                if product == "0":
                    option_2 = 0
                    break
                time.sleep(0.75)
                print(
                    "\n",
                    globals()["product_list_%s" % (product)][0],
                    globals()["product_list_%s" % (product)][1],
                    globals()["product_list_%s" % (product)][2],
                    "\n",
                    globals()["product_list_%s" % (product)][3],
                )
                option_3 = input("\n輸入要的數量，輸入[0]取消\t:")
                judge(option_3)
                if option_3 == "0":
                    option_2 = 0
                    break
                storage_list_0 = ["物品", "數量"]
                storage_list = [storage_list_0]
                for i in range(1, l + 1):
                    storage_list.append(globals()["storage_list_%s" % (i)])
                if [
                    globals()["product_list_%s" % (product)][1],
                    int(option_3),
                ] in storage_list:
                    a = storage_list.index([globals()["product_list_%s" % (product)][1], int(option_3)])
                    globals()["storage_list_%s" % (a)][1] = globals()["storage_list_%s" % (a)][1] + int(option_3)
                else:
                    l = l + 1
                    globals()["storage_list_%s" % (l)] = [
                        globals()["product_list_%s" % (product)][1],
                        int(option_3),
                    ]
                    storage_list_0 = ["物品", "數量"]
                    storage_list = [storage_list_0]
                    for i in range(1, l + 1):
                        storage_list.append(globals()["storage_list_%s" % (i)])
                time.sleep(0.75)
                print("\n你購買了%s%d個" % (globals()["product_list_%s" % (product)][1], int(option_3)))
            time.sleep(0.75)
            print("\n老闆:客官慢走")
            time.sleep(0.75)
        if option_2 == "5":
            place = "無憂宗集市"
            print("\n%s離開了%s" % (player[0], place))
            option_3 = 0
            break
    if option_1 == "4":
        place = "無憂宗丹閣"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]兌換丹藥\t[2]接任務\t[3]拜見長老\n[4]進入種植園\t[5]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "4":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "5":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "5":
        place = "無憂宗器閣"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]兌換法寶\t[2]接任務\t[3]拜見長老\n[4]進入礦區\t[5]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "4":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "5":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "6":
        place = "無憂宗藏經閣"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]學習神通\t[2]接任務\t[3]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "7":
        place = "無憂宗悟道峰"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]開始悟道\t[3]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "8":
        place = "無憂宗外事閣"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]接任務\t[2]交任務\t[3]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "9":
        place = "無憂宗宗門大殿"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]看公告\t[2]看宗門歷史\t[3]報名活動\n[4]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "4":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "10":
        place = "無憂宗靈獸園"
        print("\n%s進入了%s" % (player[0], place))
        option_2 = input("\n[1]接任務\t[2]交任務\t[3]拜見長老\n[4]進入靈獸生活區\t[5]離開\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "4":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "5":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
    if option_1 == "11":
        place = "無憂宗宗門附近"
        print("\n%s出山門了" % (player[0]))
        option_2 = input("\n[1]剿匪\t[2]採集\t[3]挖礦\n[4]捕捉靈獸\t[5]下山遊歷\t[6]回宗門\t:")
        judge(option_2)
        if option_2 == "1":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "2":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "3":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "4":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "5":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
        if option_2 == "6":
            place = ""
            print("\n%s進入了%s" % (player[0], place))
