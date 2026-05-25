from random import choice, choices
from random import randint as ri
from time import sleep
from uuid import uuid4

i = 0
level = 1
monster_ability: list[list[int | str]] = []
monster: list[str] = []
player_atk = 10
player_def = 10
player_agi = 10
player_HP = 10
exp = 0
player_name = "set"
player_ability = [player_atk, player_def, player_agi, player_HP, level, exp]
residual_points = 8
residual_five_points = 10
money = 1000
player_property = [1, 1, 1, 1, 1]  # 金,木,水,火,土
difficulty = 1
property_equip: list[str] = []
storehouse_item: list[list[str | int]] = [
    ["物品倉庫", "數量"],
    ["item1", 1],
    ["item2", 2],
    ["item3", 3],
    ["item4", 4],
    ["item5", 5],
]
storehouse_equip: list[list[str | int]] = [
    ["裝備倉庫", "編號"],
    ["equip1", 1],
    ["equip2", 2],
    ["equip3", 3],
    ["equip4", 4],
    ["equip5", 5],
]
bag_item: list[list[str | int]] = [
    ["物品背包", "數量"],
    ["item1", 1],
    ["item2", 2],
    ["item3", 3],
    ["item4", 4],
    ["item5", 5],
]
bag_equip: list[list[str | int]] = [
    ["裝備背包", "編號"],
    ["equip1", 1],
    ["equip2", 2],
    ["equip3", 3],
    ["equip4", 4],
    ["equip5", 5],
]
attribute_equip_list = ["爆傷", "爆率", "閃避", "減傷", "血增", "金錢", "經驗", "屬傷", "屬防"]
type_equip_list = ["防具", "武器", "頭盔", "飾品"]
rarity_list = ["荒", "洪", "宙", "宇", "黃", "玄", "地", "天"]


def produce_equip(level: int, property: str):
    rarity = choices([0, 1, 2, 3, 4, 5, 6, 7], weights=[90, 9, 0.9, 0.09, 0.009, 0.0009, 0.00009, 0.00001])[0]
    attribute_equip: list[str] = []
    ID_equip = str(uuid4())
    for _ in range(1, rarity):
        rarity_list[rarity]
        attribute_equip.append(attribute_equip_list[ri(0, 8)])
    type_equip_list[ri(0, 2)]
    return ID_equip


def use(item: str, amount: int):
    product: list[str | int] = ["item1", 1]
    print(f"{player_name}使用{amount}個{item}獲得{product}")


def storehouse():
    global storehouse_item, storehouse_equip, bag_equip, bag_item
    option_3 = input("\n[1]物品倉庫\t[2]裝備倉庫\t[3]離開\t:")
    judgment(option_3)
    while option_3 == "1":
        if len(storehouse_item) == 1:
            option_4 = input("\n物品倉庫空空如也\n(按[0]退出)\t:")
            judgment(option_4)
            if option_4 == "0":
                break
        for i in range(len(storehouse_item)):
            print("%d:%s\t%s個\n(屬性+介紹)" % (i, storehouse_item[i][0], storehouse_item[i][1]))
        option_4 = input("\n請輸入要操作的項目編號(按[0]退出)\t:")
        judgment(option_4)
        if option_4 == "0":
            break
        option_4 = int(option_4)
        print("%s\t%s%d" % (storehouse_item[option_4][0], storehouse_item[option_4][1]))
        option_5 = input("\n[0]退出\t[1]使用\t[2]丟棄\t[3]拿到背包\t:")
        judgment(option_5)
        txt = "error"
        if option_5 == "1":
            txt = "用"
        if option_5 == "2":
            txt = "丟"
        if option_5 == "3":
            txt = "拿"
        option_6 = input(f"\n請輸入要{txt}的數量(輸入[0]取消)")
        judgment(option_6)
        while option_6 != "0":
            try:
                option_6 = int(option_6)
            except:
                print("\n輸入錯誤")
                break
            if option_6 > int(storehouse_item[option_4][1]):
                print("\n輸入錯誤")
                break
            elif option_6 == int(storehouse_item[option_4][1]):
                print(f"{storehouse_item[option_4][0]}全部{txt}完了")
                del storehouse_item[option_4]
            elif option_6 < int(storehouse_item[option_4][1]):
                print(f"{txt}了{option_6}個{storehouse_item[option_4][0]}剩下{int(storehouse_item[option_4][1]) - option_6}個")
            if option_5 == "1":
                use(str(storehouse_item[option_4][0]), option_6)
            if option_5 == "3":
                a = 0
                for i in range(len(bag_item)):
                    if bag_item[i][0] == storehouse_item[option_4][0]:
                        bag_item[i][1] = int(bag_item[i][1]) + option_6
                        storehouse_item[option_4][1] = int(storehouse_item[option_4][1]) - option_6
                        a = 1
                if a == 0:
                    bag_item.append(storehouse_item[option_4])
    while option_3 == "2":
        if len(storehouse_equip) == 1:
            option_4 = input("\n裝備倉庫空空如也\n(按[0]退出)\t:")
            judgment(option_4)
            if option_4 == "0":
                break
        for i in range(len(storehouse_equip)):
            print("%d:%s\n(屬性+介紹)\n編號:%s" % (i, storehouse_equip[i][0], storehouse_equip[i][1]))
        option_4 = input("\n請輸入要操作的項目編號(按[0]退出)\t:")
        judgment(option_4)
        if option_4 == "0":
            break
        option_4 = int(option_4)
        print("%s\t%s%d" % (storehouse_equip[option_4][0], storehouse_equip[option_4][1]))
        option_5 = input("\n[0]退出\t[1]穿戴\t[2]丟棄\t[3]拿到背包\t:")
        judgment(option_5)
        if option_5 == "1":
            txt = f"{player_name}穿上了{storehouse_equip[option_4][0]}"
        if option_5 == "2":
            txt = f"{player_name}丟掉了{storehouse_equip[option_4][0]}"
            del storehouse_equip[option_4]
        if option_5 == "3":
            txt = f"{player_name}把{storehouse_equip[option_4][0]}放進背包"
            bag_equip.append(storehouse_equip[option_4])
    if option_3 == "3":
        return


def add_five_point(residual_five_points: int) -> int:
    global player_property
    sleep(0.25)
    print("\n你目前的五行屬性:")
    print(
        "等級:%d\n金:%d\t木:%d\t水:%d\t火:%d\t土:%d\n剩餘點數:%d"
        % (
            player_ability[4],
            player_property[0],
            player_property[1],
            player_property[2],
            player_property[3],
            player_property[4],
            residual_five_points,
        )
    )
    ap = input("\n輸入要加的點數每個數字之間用空白隔開\tex.0 0 0 1 0(火加1)\t[0]退出\t:")
    judgment(ap)
    if ap == "0":
        return residual_five_points
    add_point = [int(i) for i in ap.split()]
    residual = add_point[0] + add_point[1] + add_point[2] + add_point[3] + add_point[4]
    sleep(0.25)
    if residual > residual_five_points:
        print("\n剩餘點數不夠")
    elif residual < 0:
        print("\n輸入錯誤")
    else:
        residual_five_points -= residual
        temporary_0 = player_property[0]
        temporary_1 = player_property[1]
        temporary_2 = player_property[2]
        temporary_3 = player_property[3]
        temporary_4 = player_property[4]
        player_property[0] += add_point[0]
        player_property[1] += add_point[1]
        player_property[2] += add_point[2]
        player_property[3] += add_point[3]
        player_property[4] += add_point[4]
        sleep(0.25)
        print(
            "\n金:%d->%d\n木:%d->%d\n水:%d->%d\n火:%d->%d\n土:%d->%d\n剩餘點數:%d"
            % (
                temporary_0,
                player_property[0],
                temporary_1,
                player_property[1],
                temporary_2,
                player_property[2],
                temporary_3,
                player_property[3],
                temporary_4,
                player_property[4],
                residual_five_points,
            )
        )
    option_5 = input("\n[1]繼續加點\t[2]退出\t:")
    if option_5 == "1":
        return add_five_point(residual_five_points)
    else:
        return residual_five_points


def add_point(residual_points: int) -> int:
    global player_ability
    sleep(0.25)
    print("\n你目前的屬性:")
    print(
        "等級:%d\n攻擊力:%d\n防禦力:%d\n速度:%d\n血量:%d\n剩餘點數:%d"
        % (
            player_ability[4],
            player_ability[0],
            player_ability[1],
            player_ability[2],
            player_ability[3],
            residual_points,
        )
    )
    ap = input("\n輸入要加的點數每個數字之間用空白隔開\tex.0 0 0 1(血量加1)\t[0]退出\t:")
    judgment(ap)
    if ap == "0":
        return residual_points
    add_points = [int(i) for i in ap.split()]
    residual = add_points[0] + add_points[1] + add_points[2] + add_points[3]
    sleep(0.25)
    if residual > residual_points:
        print("\n剩餘點數不夠")
    elif residual < 0:
        print("\n輸入錯誤")
    else:
        residual_points -= residual
        temporary_0 = player_ability[0]
        temporary_1 = player_ability[1]
        temporary_2 = player_ability[2]
        temporary_3 = player_ability[3]
        player_ability[0] += add_points[0]
        player_ability[1] += add_points[1]
        player_ability[2] += add_points[2]
        player_ability[3] += add_points[3]
        sleep(0.25)
        print(
            "\n攻擊力:%d->%d\n防禦力:%d->%d\n速度:%d->%d\n血量:%d->%d\n剩餘點數:%d"
            % (
                temporary_0,
                player_ability[0],
                temporary_1,
                player_ability[1],
                temporary_2,
                player_ability[2],
                temporary_3,
                player_ability[3],
                residual_points,
            )
        )
    option_5 = input("\n[1]繼續加點\t[2]退出\t:")
    if option_5 == "1":
        return add_point(residual_points)
    else:
        return residual_points


def judgment(option: str):
    global player_ability, monster_ability, monster, level, player_agi, player_atk, player_def, player_HP, player_name, player_property, exp, money, residual_five_points, residual_points, difficulty
    if option == "set":
        place = "設定介面"
        print("\n你進入了%s" % (place))
        option_ = input("\n[1]更改名稱\t[2]存檔\t[3]讀檔\t[4]返回\t:")
        judgment(option_)
        if option_ == "1":
            player_name = input("\n請輸入玩家名稱:")
            judgment(player_name)
            print("\n你的名字改成了%s" % (player_name))
        if option_ == "2":
            sleep(0.5)
            try:
                line = input("\n請先在C槽建立名為_game_的資料夾,存檔會存在裡面,請輸入檔名:")
                judgment(line)
                sleep(0.5)
                with open("C:/_game_/%s.txt" % (line), "w+") as f:
                    f.write(f"{level}\n{player_agi}\n{player_atk}\n{player_def}\n{player_HP}\n{player_name}\n{player_property[0]}\n{player_property[1]}\n{player_property[2]}\n{player_property[3]}\n{player_property[4]}\n{exp}\n{money}\n{residual_five_points}\n{residual_points}\n{difficulty}")
            except FileNotFoundError:
                print("\n路徑出錯,檔案未儲存")
            except:
                print("\n出錯,檔案未儲存")
            else:
                print("\n檔案已儲存,路徑:C:/_game_/%s.txt" % (line))
            sleep(0.5)
        if option_ == "3":
            sleep(0.5)
            try:
                line = input("\n請把存檔放到C:/_game_/,並輸入檔案名稱(不用加附檔名)(只接受txt檔)\t:")
                judgment(line)
                sleep(0.5)
                variable: list[str] = []
                with open("C:/_game_/%s.txt" % (line), "r") as f:
                    for i in f.readlines():
                        i = i.strip("\n")
                        variable.append(i)
                    level = int(variable[0])
                    player_agi = int(variable[1])
                    player_atk = int(variable[2])
                    player_def = int(variable[3])
                    player_HP = int(variable[4])
                    player_name = variable[5]
                    player_property[0] = int(variable[6])
                    player_property[1] = int(variable[7])
                    player_property[2] = int(variable[8])
                    player_property[3] = int(variable[9])
                    player_property[4] = int(variable[10])
                    exp = int(variable[11])
                    money = int(variable[12])
                    residual_five_points = int(variable[13])
                    residual_points = int(variable[14])
                    difficulty = int(variable[15])
                    player_ability = [
                        player_atk,
                        player_def,
                        player_agi,
                        player_HP,
                        level,
                        exp,
                    ]
                    monster_ability = []
                    monster = []
                    print(variable)
            except FileNotFoundError:
                print("\n找不到檔案,讀取失敗")
            except:
                print("\n出錯,檔案讀取失敗")
            else:
                print("\n成功讀取存檔%s" % (line))
            sleep(0.5)
        if option_ == "4":
            return
    if option == "off":
        print("\n離開遊戲中")
        sleep(1)
        print("\n離開遊戲")
        sleep(1)
        exit()


def PvE(place: str):
    global exp, money, player_HP, player_ability
    i = 1
    money_add = 0
    while i <= ri(1, 5):
        property = [-1, -1, -1, -1, -1]
        if place == "東嶽泰山":
            property = [1, 4, 1, 1, 1]
        if place == "西嶽華山":
            property = [4, 1, 1, 1, 1]
        if place == "中嶽嵩山":
            property = [1, 1, 1, 1, 4]
        if place == "南嶽衡山":
            property = [1, 1, 1, 4, 1]
        if place == "北嶽恆山":
            property = [1, 1, 4, 1, 1]
        monster.append(summon(property, level, i))
        for j in monster:
            try:
                money_add = int(j[5])
            except:
                money_add = 0
        i += 1
    print("\n你遇上了敵人:\n")
    for a in range(0, len(monster)):
        print(monster[a])
    option = input("\n[1]戰鬥\t[2]逃跑\t:")
    sleep(0.5)
    if option == "2":
        print("\n你選擇了逃跑")
    if option == "1":
        print("\n你選擇了戰鬥")
        HP = player_ability[3]
        if fighting(monster_ability, player_ability) == True:
            print("\n錢:%d->%d\n經驗值:%d->%d" % (money, money + money_add, exp, exp + money_add))
            money += money_add
            exp += money_add
        else:
            print("\n錢:%d->%d" % (money, money * 0.9))
            money = money * 0.9
        player_ability[3] = player_HP = HP
    monster.clear()
    monster_ability.clear()


def summon(property: list[int], level: int, i: int):
    global player_ability
    summons_property_list: list[str] = []
    summons_property_list.extend(["金"] * property[0])
    summons_property_list.extend(["木"] * property[1])
    summons_property_list.extend(["水"] * property[2])
    summons_property_list.extend(["火"] * property[3])
    summons_property_list.extend(["土"] * property[4])
    summons_property = summons_property_list[ri(0, 7)]
    summon_type_list = ["monster1", "monster2", "monster3", "monster4", "monster5", "monster6", "monster6", "monster7", "monster8", "monster9"]
    summons_type = "error"
    if player_ability[4] == 1:
        summons_type = choice(summon_type_list)
    level = abs(ri(level - difficulty, level + difficulty))
    if level == 0:
        level = 1
    summons_atk = ri(10 ** (level - 1), 10**level)
    summons_def = ri(10 ** (level - 1), 10**level)
    summons_agi = ri(10 ** (level - 1), 10**level)
    summons_HP = ri(10 ** (level - 1), 10**level)
    ability: list[int | str] = [i, summons_atk, summons_def, summons_agi, summons_HP, level, summons_property, summons_type]
    monster_ability.append(ability)
    return "%d級%s屬性%s" % (level, summons_property, summons_type)


def fighting(monster_ability: list[list[int | str]], player_ability: list[int]):  # atk,def,agi,HP
    global property_equip
    b: list[int] = []
    property_equip = []
    print(["序號", "攻擊", "防禦", "速度", "血量", "等級", "屬性", "種類"])
    for i in range(len(monster_ability)):
        print(monster_ability[i])
    while player_ability[4] > 0 and len(monster) > 0:
        for a in range(len(monster)):
            if b.count(a) == 0:
                if (player_ability[2] / player_ability[2] + int(monster_ability[a][3])) * 50 > ri(1, 100):
                    property = 1
                    if monster_ability[a][6] == "金":
                        property = player_property[3]
                    if monster_ability[a][6] == "木":
                        property = player_property[0]
                    if monster_ability[a][6] == "水":
                        property = player_property[4]
                    if monster_ability[a][6] == "火":
                        property = player_property[2]
                    if monster_ability[a][6] == "土":
                        property = player_property[1]
                    atk = (player_ability[0] - (player_ability[0] * (int(monster_ability[a][2]) // int(monster_ability[a][2]) + player_ability[1]))) * property
                    if atk <= 0:
                        atk = 1
                        sleep(0.25)
                    print("\n%s攻擊了%s造成%d傷害" % (player_name, monster[a], atk))
                    monster_ability[a][4] = int(monster_ability[a][4]) - atk
                    if int(monster_ability[a][4]) <= 0:
                        print("[%s打贏了%s]" % (player_name, monster[a]))
                        print(monster_ability[a][6], type(monster_ability[a][6]))
                        property_equip.append(str(monster_ability[a][6]))
                        if len(b) < len(monster_ability):
                            b.append(a)
                        else:
                            sleep(0.25)
                            print("\n%s獲勝了" % (player_name))
                            return True
                    else:
                        print("%s剩餘%d血量" % (monster[a], monster_ability[a][4]))
                else:
                    sleep(0.25)
                    print("\n%s躲過了%s的攻擊" % (monster[a], player_name))
        for a in range(len(monster)):
            if b.count(a) == 0:
                if (int(monster_ability[a][3]) / player_ability[2] + int(monster_ability[a][3])) * 50 > ri(1, 100):
                    property = 1
                    if monster_ability[a][6] == "金":
                        property = player_property[3]
                    if monster_ability[a][6] == "木":
                        property = player_property[0]
                    if monster_ability[a][6] == "水":
                        property = player_property[4]
                    if monster_ability[a][6] == "火":
                        property = player_property[2]
                    if monster_ability[a][6] == "土":
                        property = player_property[1]
                    atk = (int(monster_ability[a][1]) - (int(monster_ability[a][1]) * (player_ability[1] // int(monster_ability[a][2]) + player_ability[1]))) // property
                    if atk <= 0:
                        atk = 1
                    sleep(0.25)
                    print("\n%s攻擊了%s造成%d傷害" % (monster[a], player_name, atk))
                    player_ability[3] -= atk
                    if player_ability[3] <= 0:
                        print("\n%s被%s打死了" % (player_name, monster[a]))
                        return False
                    else:
                        print("%s剩餘%d血量" % (player_name, player_ability[3]))
                else:
                    sleep(0.25)
                    print("\n%s躲過了%s的攻擊" % (player_name, monster[a]))


def open_list(a: str):
    product_list = []
    if a == "雜貨舖":
        product_list: list[list[str | int]] = [
            ["商品編號", "商品名稱", "商品價格", "商品介紹"],
            [1, "product1", 10, "介紹1"],
            [2, "product2", 10, "介紹2"],
            [3, "product3", 10, "介紹3"],
        ]
    for i in range(0, len(product_list) - 1):
        print(product_list[i][0], product_list[i][1], product_list[i][2])


print("歡迎進入遊戲")
sleep(0.5)
print("\n在任意地方輸入[off]關閉遊戲\n在任意地方輸入[set]進入設定介面")
sleep(0.5)
repeat = 1
player_name = input("\n請輸入玩家名稱:")
judgment(player_name)
sleep(0.5)
print("\n進入遊戲中")
sleep(0.5)
print("(建議先打開背包看看)")
while 1 == 1:
    place = "大廳"
    option_1 = input("\n[1]出門歷練\t[2]進洞府\t[3]整理狀態\t[4]去集市\t:")
    judgment(option_1)

    while option_1 == "1":
        sleep(0.5)
        print("\n%s決定出門打怪" % (player_name))
        option_2 = input("\n[1]去東嶽泰山\t[2]去西嶽華山\t[3]去中嶽嵩山\t[4]去南嶽衡山\t[5]去北嶽恆山\t[6]結束冒險\t:")
        judgment(option_2)
        if option_2 == "1":
            place = "東嶽泰山"
            sleep(0.5)
            print("\n你進入了%s" % (place))
            PvE(place)
        if option_2 == "2":
            place = "西嶽華山"
            sleep(0.5)
            print("\n你進入了%s" % (place))
            PvE(place)
        if option_2 == "3":
            place = "中嶽嵩山"
            sleep(0.5)
            print("\n你進入了%s" % (place))
            PvE(place)
        if option_2 == "4":
            place = "南嶽衡山"
            sleep(0.5)
            print("\n你進入了%s" % (place))
            PvE(place)
        if option_2 == "5":
            place = "北嶽恆山"
            sleep(0.5)
            print("\n你進入了%s" % (place))
            PvE(place)
        if option_2 == "6":
            place = "大廳"
            print("\n你進入了%s" % (place))
            break

    while option_1 == "2":
        sleep(0.5)
        print("\n%s決定先回洞府準備好再出發" % (player_name))
        option_2 = input("\n[1]去倉庫\t[2]去鍛造室\t[3]去煉丹房\t[4]去礦場\t[5]去種植園\t[6]去祭壇\t[7]離開\t:")
        judgment(option_2)
        if option_2 == "1":
            place = "倉庫"
            print("\n你進入了%s" % (place))
            storehouse()
        if option_2 == "2":
            place = "鍛造室"
            print("\n你進入了%s" % (place))
        if option_2 == "3":
            place = "煉丹房"
            print("\n你進入了%s" % (place))
        if option_2 == "4":
            place = "礦場"
            print("\n你進入了%s" % (place))
        if option_2 == "5":
            place = "種植園"
            print("\n你進入了%s" % (place))
        if option_2 == "6":
            place = "祭壇"
            print("\n你進入了%s" % (place))
            residual_five_points = add_five_point(residual_five_points)
        if option_2 == "7":
            place = "大廳"
            print("\n你進入了%s" % (place))
            break

    while option_1 == "3":
        sleep(0.5)
        print("\n%s決定先把自身狀態整理好再出發" % (player_name))
        option_2 = input("\n[1]角色屬性\t[2]角色裝備\t[3]背包\t[4]離開\t:")
        judgment(option_2)
        sleep(0.5)
        if option_2 == "1":
            place = "屬性面板"
            print("\n你進入了%s" % (place))
            residual_points = add_point(residual_points)
            player_atk = player_ability[0]
            player_def = player_ability[1]
            player_agi = player_ability[2]
            player_HP = player_ability[3]
        if option_2 == "2":
            place = "裝備介面"
            print("\n你進入了%s" % (place))
        if option_2 == "3":
            place = "背包空間"
            print("\n你進入了%s" % (place))
        if option_2 == "4":
            place = "大廳"
            print("\n你進入了%s" % (place))
            break

    while option_1 == "4":
        sleep(0.5)
        print("\n%s決定去集市採購一些物資")
        option_2 = input("\n[1]雜貨舖\t[2]丹藥閣\t[3]鍛器閣\t[4]陣法樓\t[5]靈材閣\t[6]藏書鋪\t[7]離開\t:")
        judgment(option_2)
        if option_2 == "1":
            place = "雜貨舖"
            print("\n你進入了%s" % (place))
            open_list(place)
        if option_2 == "2":
            place = "丹藥閣"
            print("\n你進入了%s" % (place))
        if option_2 == "3":
            place = "鍛器閣"
            print("\n你進入了%s" % (place))
        if option_2 == "4":
            place = "陣法樓"
            print("\n你進入了%s" % (place))
        if option_2 == "5":
            place = "靈材閣"
            print("\n你進入了%s" % (place))
        if option_2 == "6":
            place = "藏書鋪"
            print("\n你進入了%s" % (place))
        if option_2 == "7":
            place = "大廳"
            print("\n你進入了%s" % (place))
            break
