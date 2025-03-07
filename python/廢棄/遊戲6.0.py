from random import randint as ri
import os
from typing import Any


def attributepage():
    print(
        f"\n1.攻擊力:{player.att}\n2.防禦力:{player.Def}\n3.速度:{player.agi}\n4.血量:{player.hp}\n5.金:{player.metal}\n6.木:{player.wood}\n7.水:{player.water}\n8.火:{player.fire}\n9.土:{player.earth}\n基礎屬性剩餘點:{player.rp1}\n五行屬性剩餘點:{player.rp2}\n"
    )
    option = input("\n輸入你要加點的屬性名稱或編號\n輸入10離開\n")
    if option in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        option1 = input("\n輸入你要加的點數\n")
        try:
            option1 = int(option1)
        except:
            print("輸入錯誤")
            return
        if option == "1":
            if option1 <= player.rp1:
                print(f"攻擊力:{player.att} -> {player.att + option1}\n基礎屬性剩餘點:{player.rp1} -> {player.rp1 - option1}")
                player.att += option1
                player.rp1 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "2":
            if option1 <= player.rp1:
                print(f"防禦力:{player.Def} -> {player.Def + option1}\n基礎屬性剩餘點:{player.rp1} -> {player.rp1 - option1}")
                player.Def += option1
                player.rp1 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "3":
            if option1 <= player.rp1:
                print(f"速度:{player.agi} -> {player.agi + option1}\n基礎屬性剩餘點:{player.rp1} -> {player.rp1 - option1}")
                player.agi += option1
                player.rp1 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "4":
            if option1 <= player.rp1:
                print(f"血量:{player.hp} -> {player.hp + option1}\n基礎屬性剩餘點:{player.rp1} -> {player.rp1 - option1}")
                player.hp += option1
                player.rp1 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "5":
            if option1 <= player.rp2:
                print(f"金:{player.metal} -> {player.metal + option1}\n五行屬性剩餘點:{player.rp2} -> {player.rp2 - option1}")
                player.metal += option1
                player.rp2 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "6":
            if option1 <= player.rp2:
                print(f"木:{player.wood} -> {player.wood + option1}\n五行屬性剩餘點:{player.rp2} -> {player.rp2 - option1}")
                player.wood += option1
                player.rp2 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "7":
            if option1 <= player.rp2:
                print(f"水:{player.water} -> {player.water + option1}\n五行屬性剩餘點:{player.rp2} -> {player.rp2 - option1}")
                player.water += option1
                player.rp2 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "8":
            if option1 <= player.rp2:
                print(f"火:{player.fire} -> {player.fire + option1}\n五行屬性剩餘點:{player.rp2} -> {player.rp2 - option1}")
                player.fire += option1
                player.rp2 -= option1
            else:
                print("剩餘點數不夠")
        elif option == "9":
            if option1 <= player.rp2:
                print(f"土:{player.earth} -> {player.earth + option1}\n五行屬性剩餘點:{player.rp2} -> {player.rp2 - option1}")
                player.earth += option1
                player.rp2 -= option1
            else:
                print("剩餘點數不夠")
    elif option == "10":
        return
    else:
        print("輸入錯誤")
    attributepage()


def bag():
    option = input("\n要打開素材背包請按1\n要打開裝備背包請按2\n要打開人物裝備欄請按3\n要離開背包介面請按4\n")
    li: list[list[str]] = []
    if option == "1":
        for i in player.material_bag:
            print(f"{i}:{player.material_bag[i]}")
            li.append(i.split("."))
        option1 = input("\n請輸入要選取的素材名稱或編號\n")
        try:
            option1 = int(option1)
            for i in range(len(li)):
                if li[i][0] == option1:
                    print(f"\n你選取了{li[i][0]}.{li[i][1]}，目前有{player.material_bag[f'{li[i][0]}.{li[i][1]}']}個\n")
        except:
            for i in range(len(li)):
                if li[i][1] == option1:
                    print(f"\n你選取了{li[i][0]}.{li[i][1]}，目前有{player.material_bag[f'{li[i][0]}.{li[i][1]}']}個\n")
    elif option == "2":
        for i in player.equipment_bag:
            print(f"{i}:{player.equipment_bag[i]}")
            li.append(i.split("."))
        option1 = input("\n請輸入要選取的裝備名稱或編號\n")
        try:
            option1 = int(option1)
            for i in range(len(li)):
                if li[i][0] == option1:
                    print(f"\n你選取了{li[i][0]}.{li[i][1]}，目前有{player.equipment_bag[f'{li[i][0]}.{li[i][1]}']}個\n")
        except:
            for i in range(len(li)):
                if li[i][1] == option1:
                    print(f"\n你選取了{li[i][0]}.{li[i][1]}，目前有{player.equipment_bag[f'{li[i][0]}.{li[i][1]}']}個\n")
    elif option == "3":
        for i in player.equipment_slot:
            print(f"{i}:{player.equipment_slot[i]}")
            li.append(i.split("."))
        option1 = input("\n請輸入要選取的欄位名稱或編號\n")
        try:
            option1 = int(option1)
            for i in range(len(li)):
                if li[i][0] == option1:
                    print(f"\n你選取了{li[i][0]}.{li[i][1]}，目前裝備是{player.equipment_bag[f'{li[i][0]}.{li[i][1]}']}\n")
        except:
            for i in range(len(li)):
                if li[i][1] == option1:
                    print(f"\n你選取了{li[i][0]}.{li[i][1]}，目前裝備是{player.equipment_bag[f'{li[i][0]}.{li[i][1]}']}\n")
    elif option == "4":
        return
    else:
        print("\n輸入錯誤")
    bag()


def base():
    pass


def generatemap():
    map: list[list[list[int | bool | str]]] = []
    for i in range(999):
        a: list[list[int | bool | str]] = []
        for j in range(999):
            a.append([ri(0, 100), True, "美麗的大自然"])
        map.append(a)
    for i in range(999):
        for j in range(999):
            if map[i][j][0] <= 10:
                map[i][j][1] = "山地"
            elif map[i][j][0] <= 20:
                map[i][j][1] = "河/湖"
            elif map[i][j][0] <= 30:
                map[i][j][2] = "怪物群"
            elif map[i][j][0] <= 40:
                map[i][j][2] = "資源點"
            elif map[i][j][0] <= 50:
                map[i][j][2] = "遺蹟"
            if map[i][j][0] % 2 == 0 and map[i][j][1]:
                map[i][j][1] = "平原"
            elif map[i][j][0] % 2 == 1 and map[i][j][1]:
                map[i][j][1] = "丘陵"
    map[500][500][1] = "平原"
    return map


def goout():
    global map, player
    x, y = player.x + 500, player.y + 500
    print(f"\n你現在的座標是({player.x},{player.y}),ID是{map[x][y][0]},地形是{map[x][y][1]},有{map[x][y][2]}")
    option = input("\n要在地圖上行走請輸入[東西南北]或[ewsn]\n要打開地圖請按1\n要打開背包請按2\n要回家請按3\n")
    if option == "e" or option == "E" or option == "東":
        player.x += 1
    elif option == "w" or option == "W" or option == "西":
        player.x -= 1
    elif option == "s" or option == "S" or option == "南":
        player.y += 1
    elif option == "n" or option == "N" or option == "北":
        player.y -= 1
    x, y = player.x + 500, player.y + 500
    if (
        option == "e"
        or option == "E"
        or option == "東"
        or option == "w"
        or option == "W"
        or option == "西"
        or option == "s"
        or option == "S"
        or option == "南"
        or option == "n"
        or option == "N"
        or option == "北"
    ):
        if map[x][y][1] == "山地":
            option1 = input("\n遇上山地,是否要花費一條繩索爬山\n請輸入(y/n)或(T/F)或(1/2)\n")
            if option1 == "y" or option1 == "Y" or option1 == "t" or option1 == "T" or option1 == "1":
                if player.material_bag["rope"] >= 1:
                    player.material_bag["rope"] -= 1
                    print("你移動了一格")
                else:
                    print("繩索的數量不夠")
                    if option == "e" or option == "E" or option == "東":
                        player.x -= 1
                    elif option == "w" or option == "W" or option == "西":
                        player.x += 1
                    elif option == "s" or option == "S" or option == "南":
                        player.y -= 1
                    elif option == "n" or option == "N" or option == "北":
                        player.y += 1
                    x, y = player.x + 500, player.y + 500
            elif option1 == "n" or option1 == "N" or option1 == "f" or option1 == "F" or option1 == "2":
                print("你留在原地沒有行動")
                if option == "e" or option == "E" or option == "東":
                    player.x -= 1
                elif option == "w" or option == "W" or option == "西":
                    player.x += 1
                elif option == "s" or option == "S" or option == "南":
                    player.y -= 1
                elif option == "n" or option == "N" or option == "北":
                    player.y += 1
                x, y = player.x + 500, player.y + 500
            else:
                print("輸入錯誤")
                if option == "e" or option == "E" or option == "東":
                    player.x -= 1
                elif option == "w" or option == "W" or option == "西":
                    player.x += 1
                elif option == "s" or option == "S" or option == "南":
                    player.y -= 1
                elif option == "n" or option == "N" or option == "北":
                    player.y += 1
                x, y = player.x + 500, player.y + 500
        elif map[x][y][1] == "河/湖":
            option1 = input("\n遇上河/湖,是否要花費一艘船航行\n請輸入(y/n)或(T/F)或(1/2)\n")
            if option1 == "y" or option1 == "Y" or option1 == "t" or option1 == "T" or option1 == "1":
                if player.material_bag["ship"] >= 1:
                    player.material_bag["ship"] -= 1
                    print("你移動了一格")
                else:
                    print("船的數量不夠")
                    if option == "e" or option == "E" or option == "東":
                        player.x -= 1
                    elif option == "w" or option == "W" or option == "西":
                        player.x += 1
                    elif option == "s" or option == "S" or option == "南":
                        player.y -= 1
                    elif option == "n" or option == "N" or option == "北":
                        player.y += 1
                    x, y = player.x + 500, player.y + 500
            elif option1 == option1 == "n" or option1 == "N" or option1 == "f" or option1 == "F" or option1 == "2":
                print("你留在原地沒有行動")
                if option == "e" or option == "E" or option == "東":
                    player.x -= 1
                elif option == "w" or option == "W" or option == "西":
                    player.x += 1
                elif option == "s" or option == "S" or option == "南":
                    player.y -= 1
                elif option == "n" or option == "N" or option == "北":
                    player.y += 1
                x, y = player.x + 500, player.y + 500
            else:
                print("輸入錯誤")
                if option == "e" or option == "E" or option == "東":
                    player.x -= 1
                elif option == "w" or option == "W" or option == "西":
                    player.x += 1
                elif option == "s" or option == "S" or option == "南":
                    player.y -= 1
                elif option == "n" or option == "N" or option == "北":
                    player.y += 1
                x, y = player.x + 500, player.y + 500
        if map[x][y][2] == "怪物群":
            print("你移動了一格,你遇到了怪物群")
            monstergroup()
        elif map[x][y][2] == "資源點":
            print("你移動了一格,你遇到了資源點")
            resourcepoint()
        elif map[x][y][2] == "遺蹟":
            print("你移動了一格,你遇到了遺蹟")
            remains()
        else:
            print("你移動了一格")
    elif option == "1":
        showmap()
    elif option == "2":
        bag()
    elif option == "3":
        return
    else:
        print("輸入錯誤")
    goout()


def help():
    pass


def main():
    while True:
        option = input("\n要出門請按1\n要進入基地請按2\n要開啟角色介面請按3\n要開啟系統請按4\n關閉遊戲請按5\n")
        if option == "1":
            goout()
        elif option == "2":
            base()
        elif option == "3":
            role()
        elif option == "4":
            system()
        elif option == "5":
            print("\n關閉遊戲")
            exit()
        else:
            print("\n輸入錯誤")


def monstergroup():
    monster = summonmonster(player.lv)
    p = {
        "name": player.name,
        "att": player.att,
        "def": player.Def,
        "agi": player.agi,
        "hp": player.hp,
        "metal": player.metal,
        "wood": player.wood,
        "water": player.water,
        "fire": player.fire,
        "earth": player.earth,
    }
    print(monster)
    option = input("\n按1戰鬥\n按2逃跑\n按3打開背包\n")
    if option == "1":
        PvE(monster, p)
        return
    elif option == "2":
        return
    elif option == "3":
        bag()
    else:
        print("輸入錯誤")
    monstergroup()


def nuwgame():
    global player, map  # 吸血,反擊,連擊,閃避,爆擊,擊暈,抗吸血,抗反擊,抗連擊,抗閃避,抗爆擊,抗擊暈
    attribute = {
        "att": 10,
        "Def": 10,
        "agi": 10,
        "hp": 100,
        "metal": 1,
        "wood": 1,
        "water": 1,
        "fire": 1,
        "earth": 1,
        "mb": {"ship": 5, "ship": 5},
        "eb": {},
        "es": {
            "helmet": None,
            "armor": None,
            "leggings": None,
            "shoes": None,
            "cloak": None,
            "gloves": None,
            "bracelets": None,
            "rings": None,
            "footrings": None,
            "mainweapon": None,
            "secondaryweapon": None,
        },
        "rp1": 0,
        "rp2": 0,
        "x": 0,
        "y": 0,
        "bonus": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "lv": 1,
        "exp": 0,
    }
    name = input("\n請輸入玩家名稱:")
    player = playerc(name, attribute)
    map = generatemap()
    main()


def openfile(name: str):
    global player, map
    if not os.access("C:\\__game__\\" + name + ".txt", os.F_OK):
        print("\n檔案不存在")
        return
    if not os.access("C:\\__game__\\" + name + ".txt", os.R_OK):
        print("\n檔案無法讀取")
        return
    f = open("C:\\__game__\\" + name + ".txt", "w+")
    a = f.readlines()
    attribute = eval(a[0])
    map = eval(a[1])
    f.close
    player = playerc(attribute["name"], attribute)
    main()


class playerc:
    def __init__(self, name: str, attribute: dict[str, int | dict[str, int | None] | list[int]]) -> None:
        self.name = name
        self.att: int = attribute["att"]
        self.Def: int = attribute["Def"]
        self.agi: int = attribute["agi"]
        self.hp: int = attribute["hp"]
        self.metal: int = attribute["metal"]
        self.wood: int = attribute["wood"]
        self.water: int = attribute["water"]
        self.fire: int = attribute["fire"]
        self.earth: int = attribute["earth"]
        self.material_bag: dict[str, int] = attribute["mb"]
        self.equipment_bag: dict[str, Any] = attribute["eb"]
        self.equipment_slot: dict[str, None] = attribute["es"]
        self.rp1: int = attribute["rp1"]
        self.rp2: int = attribute["rp2"]
        self.x: int = attribute["x"]
        self.y: int = attribute["y"]
        self.bonus: list[int] = attribute["bonus"]
        self.lv: int = attribute["lv"]
        self.exp: int = attribute["exp"]


def fightbackjudgment(m: dict[str, float | str], p: dict[str, float | str], mn: float, pn: float, s: str) -> str:
    if s == "p":
        fightback = p["bonus"][1] - m["bonus"][7]
        fightback = (0, fightback)[fightback > 0]
        if ri(1, 100) <= fightback:
            atk = p["att"] / (p["att"] + m["def"])
            mn -= atk
            print(f"  {m['name']}受到了來自{p['name']}的{atk}點反擊傷害\n  剩餘血量:{mn}|{round((mn/m['hp'])*100,2)}%")
        return mn
    elif s == "m":
        fightback = m["bonus"][1] - p["bonus"][7]
        fightback = (0, fightback)[fightback > 0]
        if ri(1, 100) <= fightback:
            atk = m["att"] / (m["att"] + p["def"])
            pn -= atk
            print(f"  {p['name']}受到了來自{m['name']}的{atk}點反擊傷害\n  剩餘血量:{pn}|{round((pn/p['hp'])*100,2)}%")
        return pn
    else:
        return ""


def loot(lv: int, type: str):
    TYPE = [
        "普通史萊姆",
        "菁英史萊姆",
        "史萊姆首領",
        "史萊姆王",
        "普通盜賊",
        "菁英盜賊",
        "盜賊隊長",
        "盜賊頭目",
        "普通野牛",
        "菁英野牛",
        "野牛首領",
        "野牛王",
        "普通弓箭手",
        "菁英弓箭手",
        "弓箭手隊長",
        "弓箭手將軍",
        "士兵",
        "伍長",
        "百人隊長",
        "大將軍",
    ]
    loots = [
        "稀釋史萊姆黏液",
        "史萊姆黏液",
        "濃縮史萊姆黏液",
        "低級史萊姆魔核",
        "中級史萊姆魔核",
        "高級史萊姆魔核",
        "盜賊的刀(低級)",
        "盜賊的刀(中級)",
        "盜賊的刀(高級)",
        "盜賊的物資(小)",
        "盜賊的物資(中)",
        "盜賊的物資(大)",
        "低級野牛角",
        "低級野牛肉",
        "中級野牛角",
        "中級野牛肉",
        "高級野牛角",
        "高級野牛肉",
        "初級弓",
        "初級弩",
        "劣質箭矢",
        "中級弓",
        "中級弩",
        "普通箭矢",
        "高級弓",
        "高級弩",
        "優質箭矢",
        "初級軍刀",
        "初級盾",
        "初級盔甲",
        "中級軍刀",
        "中級盾",
        "中級盔甲",
        "高級軍刀",
        "高級盾",
        "高級盔甲",
    ]


def penalty():
    pass


def PvE(
    m: dict[str, float | str], p: dict[str, float | str]
):  # bonus = [吸血,反擊,連擊,閃避,爆擊,擊暈,抗吸血,抗反擊,抗連擊,抗閃避,抗爆擊,抗擊暈]
    pnowhp = p["hp"]
    mnowhp = m["hp"]
    c = ["金", "木", "水", "火", "土"]
    b: list[float] = []
    b.append(m["metal"] / p["metal"])
    b.append(m["wood"] / p["wood"])
    b.append(m["water"] / p["water"])
    b.append(m["fire"] / p["fire"])
    b.append(m["earth"] / p["earth"])
    if ri(1, round(p["agi"] + m["agi"])) <= p["agi"]:
        a = "p"
    else:
        a = "m"
    n = 0
    while True:
        n += 1
        if a == "m":
            element = ri(0, 4)
            print(
                f"{n}:{p['name']}剩餘血量:{pnowhp}|{round((pnowhp/p['hp'])*100,2)}%,{m['name']}剩餘血量:{mnowhp}|{round((mnowhp/m['hp'])*100,2)}%"
            )
            atk = m["att"] / (p["def"] + m["att"]) * b[element]
            f = True
            dodge = p["bonus"][3] - m["bonus"][9]
            dodge = (0, dodge)[dodge > 0]
            crit = m["bonus"][4] - p["bonus"][10]
            crit = (0, crit)[crit > 0]
            combo = m["bonus"][2] - p["bonus"][8]
            combo = (0, combo)[combo > 0]
            suckblood = m["bonus"][0] - p["bonus"][6]
            suckblood = (0, suckblood)[suckblood > 0]
            stun = m["bonus"][5] - p["bonus"][11]
            stun = (0, stun)[stun > 0]
            if ri(1, 100) <= dodge:
                print(f"  {p['name']}躲掉了{m['name']}的攻擊")
                a = "p"
                f = False
                continue
            if ri(1, 100) <= crit:
                atk *= 1.5
                pnowhp -= atk * ri(90, 110) / 100
                print(
                    f"  {p['name']}受到了來自{m['name']}的{atk}點{c[element]}屬性爆擊傷害\n  剩餘血量:{pnowhp}|{round((pnowhp/p['hp'])*100,2)}%"
                )
                mnowhp = fightbackjudgment(m, p, mnowhp, pnowhp, "p")
                f = False
            if ri(1, 100) <= combo:
                pnowhp -= atk * ri(90, 110) / 100
                print(
                    f"  {p['name']}受到了來自{m['name']}的{atk}點{c[element]}屬性連擊傷害\n  剩餘血量:{pnowhp}|{round((pnowhp/p['hp'])*100,2)}%"
                )
                mnowhp = fightbackjudgment(m, p, mnowhp, pnowhp, "p")
                f = False
            if f:
                pnowhp -= atk * ri(90, 110) / 100
                print(
                    f"  {p['name']}受到了來自{m['name']}的{atk}點{c[element]}屬性普攻傷害\n  剩餘血量:{pnowhp}|{round((pnowhp/p['hp'])*100,2)}%"
                )
            if ri(1, 100) <= suckblood:
                mnowhp += round(atk * (suckblood / 100))
                print(
                    f"  {p['name']}被{m['name']}吸血,{m['name']}回復了{round(atk*(suckblood/100))}血\n  剩餘血量:{mnowhp}|{round((mnowhp/m['hp'])*100,2)}%"
                )
            if ri(1, 100) <= stun:
                a = "m"
                print(f"  {p['name']}被{m['name']}擊暈,下回合無法攻擊")
            else:
                a = "p"
            if mnowhp <= 0:
                d = "m"
                break
            elif pnowhp <= 0:
                d = "p"
                break
        elif a == "p":
            element = ri(0, 4)
            print(
                f"{n}:{m['name']}剩餘血量:{mnowhp}|{round((mnowhp/m['hp'])*100,2)}%,{p['name']}剩餘血量:{pnowhp}|{round((pnowhp/p['hp'])*100,2)}%"
            )
            atk = p["att"] / (m["def"] + p["att"]) / b[element]
            f = True
            dodge = m["bonus"][3] - p["bonus"][9]
            dodge = (0, dodge)[dodge > 0]
            crit = p["bonus"][4] - m["bonus"][10]
            crit = (0, crit)[crit > 0]
            combo = p["bonus"][2] - m["bonus"][8]
            combo = (0, combo)[combo > 0]
            suckblood = p["bonus"][0] - m["bonus"][6]
            suckblood = (0, suckblood)[suckblood > 0]
            stun = p["bonus"][5] - m["bonus"][11]
            stun = (0, stun)[stun > 0]
            if ri(1, 100) <= dodge:
                print(f"  {m['name']}躲掉了{p['name']}的攻擊")
                a = "m"
                f = False
                continue
            if ri(1, 100) <= crit:
                atk *= 1.5
                mnowhp -= atk * ri(90, 110) / 100
                print(
                    f"  {m['name']}受到了來自{p['name']}的{atk}點{c[element]}屬性爆擊傷害\n  剩餘血量:{mnowhp}|{round((mnowhp/m['hp'])*100,2)}%"
                )
                pnowhp = fightbackjudgment(m, p, mnowhp, pnowhp, "m")
                f = False
            if ri(1, 100) <= combo:
                mnowhp -= atk * ri(90, 110) / 100
                print(
                    f"  {m['name']}受到了來自{p['name']}的{atk}點{c[element]}屬性連擊傷害\n  剩餘血量:{mnowhp}|{round((mnowhp/m['hp'])*100,2)}%"
                )
                pnowhp = fightbackjudgment(m, p, mnowhp, pnowhp, "m")
                f = False
            if f:
                mnowhp -= atk * ri(90, 110) / 100
                print(
                    f"  {m['name']}受到了來自{p['name']}的{atk}點{c[element]}屬性普攻傷害\n  剩餘血量:{mnowhp}|{round((mnowhp/m['hp'])*100,2)}%"
                )
            if ri(1, 100) <= suckblood:
                pnowhp += round(atk * (suckblood / 100))
                print(
                    f"  {m['name']}被{p['name']}吸血,{p['name']}回復了{round(atk*(suckblood/100))}血\n  剩餘血量:{pnowhp}|{round((pnowhp/p['hp'])*100,2)}%"
                )
            if ri(1, 100) <= stun:
                a = "p"
                print(f"  {m['name']}被{p['name']}擊暈,下回合無法攻擊")
            else:
                a = "m"
            if mnowhp <= 0:
                d = "m"
                break
            elif pnowhp <= 0:
                d = "p"
                break
    if d == "m":
        loot(m["lv"], m["type"])
    elif d == "p":
        penalty()
    return


def remains():
    pass


def resourcepoint():
    pass


def role():
    option = input("\n要打開背包請按1\n要進入角色屬性介面請按2\n要離開角色介面請按3\n")
    if option == "1":
        bag()
    elif option == "2":
        attributepage()
    elif option == "3":
        return
    else:
        print("輸入錯誤")
    role()


def setup():
    option = input("\n進入設定A請按1\n進入設定B請按2\n要離開設定請按3\n要離開遊戲請按4\n")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        return
    elif option == "4":
        print("\n關閉遊戲")
        exit()
    else:
        print("\n輸入錯誤")
    system()


def showmap():
    pass  # pygame


def start():
    option = input("\n開始新遊戲請按1\n開啟舊檔請按2\n離開遊戲請按3\n")
    if option == "1":
        nuwgame()
    elif option == "2":
        name = input("\n請將檔案放至C:\\__game__\\並輸入要開啟的檔案名稱:")
        openfile(name)
    elif option == "3":
        print("\n關閉遊戲")
        exit()
    else:
        print("\n輸入錯誤")
    start()


def summonmonster(lv: int) -> dict[str, float | str]:
    TYPE = [
        "普通史萊姆",
        "菁英史萊姆",
        "史萊姆首領",
        "史萊姆王",
        "普通盜賊",
        "菁英盜賊",
        "盜賊隊長",
        "盜賊頭目",
        "普通野牛",
        "菁英野牛",
        "野牛首領",
        "野牛王",
        "普通弓箭手",
        "菁英弓箭手",
        "弓箭手隊長",
        "弓箭手將軍",
        "士兵",
        "伍長",
        "百人隊長",
        "大將軍",
    ]
    TYPe = {
        "普通史萊姆": 1,
        "菁英史萊姆": 2,
        "史萊姆首領": 3,
        "史萊姆王": 5,
        "普通盜賊": 2,
        "菁英盜賊": 3,
        "盜賊隊長": 5,
        "盜賊頭目": 7,
        "普通野牛": 2,
        "菁英野牛": 3,
        "野牛首領": 5,
        "野牛王": 7,
        "普通弓箭手": 3,
        "菁英弓箭手": 5,
        "弓箭手隊長": 7,
        "弓箭手將軍": 10,
        "士兵": 3,
        "伍長": 5,
        "百人隊長": 7,
        "大將軍": 10,
    }
    elements = ["金", "木", "水", "火", "土"]
    element = elements[ri(0, 4)]
    min, max = lv - 2, lv + 2
    min = (1, min)[min > 1]
    lv = ri(min, max)
    while True:
        type = TYPE[ri(0, 19)]
        if TYPe[type] * 3 >= lv and TYPe[type] <= lv:
            break
    att = 10 * lv * (ri(90, 110) / 100)
    Def = 10 * lv * (ri(90, 110) / 100)
    agi = 10 * lv * (ri(90, 110) / 100)
    hp = 100 * lv * (ri(90, 110) / 100)
    metal = (1, lv * (ri(90, 110) / 100))[element == "金"]
    wood = (1, lv * (ri(90, 110) / 100))[element == "木"]
    water = (1, lv * (ri(90, 110) / 100))[element == "水"]
    fire = (1, lv * (ri(90, 110) / 100))[element == "火"]
    earth = (1, lv * (ri(90, 110) / 100))[element == "土"]
    attribute: dict[str, float | str] = {
        "att": att,
        "def": Def,
        "agi": agi,
        "hp": hp,
        "metal": metal,
        "wood": wood,
        "water": water,
        "fire": fire,
        "earth": earth,
        "element": element,
        "type": type,
        "lv": lv,
        "name": f"Lv.{lv}{element}屬性{type}",
    }
    return attribute


def system():
    option = input("\n需要幫助請按1\n進入檔案功能請按2\n進入設定請按3\n要離開系統請按4\n關閉遊戲請按5\n")
    if option == "1":
        help()
    elif option == "2":
        while True:
            option1 = input("\n儲存遊戲請按1\n開啟舊檔請按2\n離開檔案請按3\n")
            if option1 == "1":
                name = input("\n請在C槽建立資料夾__game__並輸入要儲存的檔案名稱:")
                writefile(name)
                break
            elif option1 == "2":
                name = input("\n請將檔案放至C:\\__game__\\並輸入要開啟的檔案名稱:")
                openfile(name)
                break
            elif option1 == "3":
                break
            else:
                print("\n輸入錯誤")
    elif option == "3":
        setup()
    elif option == "4":
        return
    elif option == "5":
        print("\n關閉遊戲")
        exit()
    else:
        print("\n輸入錯誤")
    system()


def writefile(name: str):
    global player, map
    if not os.access("C:\\__game__\\" + name + ".txt", os.F_OK):
        print("\n此路徑不存在")
        return
    if not os.access("C:\\__game__\\" + name + ".txt", os.W_OK):
        print("\n檔案無法寫入")
        return
    attribute = {}
    attribute["name"] = player.name
    attribute["att"] = player.att
    attribute["Def"] = player.Def
    attribute["agi"] = player.agi
    attribute["hp"] = player.hp
    attribute["metal"] = player.metal
    attribute["wood"] = player.wood
    attribute["water"] = player.water
    attribute["fire"] = player.fire
    attribute["earth"] = player.earth
    attribute["mb"] = player.material_bag
    attribute["eb"] = player.equipment_bag
    attribute["es"] = player.equipment_slot
    attribute["rp1"] = player.rp1
    attribute["rp2"] = player.rp2
    attribute["x"] = player.x
    attribute["y"] = player.y
    attribute["bonus"] = player.bonus
    attribute["lv"] = player.lv
    attribute["exp"] = player.exp
    f = open("C:\\__game__\\" + name + ".txt", "w+")
    f.write(str(attribute))
    f.write(str(map))
    f.close


if __name__ == "__main__":
    start()
