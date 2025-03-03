from os import path, system
from random import randint as ri
from sys import platform
from time import time


class BuildRoles:
    def __init__(self, name: str):
        self.name = name
        self.atk = 0
        self.Def = 0
        self.hp = 0
        self.agi = 0
        self.luck = 0
        self.location = ["一個空空的白色房間"]
        self.x = 0
        self.y = 0
        self.lv = 1
        self.bag: dict[str, int] = {}
        self.bag_list: list[str] = []

    def display(self):
        print(f"\n------{self.name}的基本資料------")
        print(f"姓名:{self.name}")
        print(f"地點:{self.location}")
        print(f"攻擊:{self.atk}")
        print(f"防禦:{self.Def}")
        print(f"血量:{self.hp}")
        print(f"速度:{self.agi}")
        print(f"幸運:{self.luck}")

    def locat(self, place: str):
        global locat_time
        self.location.append(place)
        locat_time = time()

    def previous(self, n: int = 1):
        for _ in range(n):
            self.location.pop()

    def save_file(self, p: str = path.dirname(path.realpath(__file__))):
        f = open(p + f"\\{self.name}.txt", "w+", encoding="utf-8")
        d: dict[str, str | list[str] | int] = {
            "name": self.name,
            "location": self.location,
            "atk": self.atk,
            "Def": self.Def,
            "hp": self.hp,
            "agi": self.agi,
            "luck": self.luck,
        }
        print(d)
        print(str(d))
        f.writelines(
            [
                "ability:",
                str(d),
                "\nlocation:",
                str(self.location),
                "\nbag:",
                str(self.bag),
                "\nbag_list:",
                str(self.bag_list),
            ]
        )

    def show_bag(self):
        for i in self.bag_list:
            if i not in self.bag:
                self.bag_list.remove(i)
        if len(self.bag) == 0:
            print("你的背包空空的")
        else:
            for i in range(0, len(self.bag_list) - 1):
                print(f"{i+1:<2}:{self.bag_list[i]:10}x{self.bag[self.bag_list[i]]}")


def choose_option(text: str | list[str] | tuple[str, ...], n: int = 1) -> int:
    if type(text) == str:
        option = input(text)
    elif type(text) == list or type(text) == tuple:
        t = ""
        n = len(text)
        for i in range(n):
            t = t + f"{i+1}.{text[i]} "
        t = t + ":"
        option = input(t)
    else:
        print("\n輸入錯誤，請重新選擇")
        option = choose_option(text, n)
    if option == "clear" or option == "c":
        if platform == "win32" or platform == "cygwin":
            system("cls")
        elif platform == "linux":
            system("clear")
        option = choose_option(text, n)
    try:
        option = int(option)
        if option > n or option <= 0:
            print("\n輸入錯誤，請重新選擇")
            option = choose_option(text, n)
    except:
        print("\n輸入錯誤，請重新選擇")
        option = choose_option(text, n)
    return option


def fighting(p: BuildRoles, e: BuildRoles):
    php = p.hp
    ehp = e.hp
    t = 0
    i = 0
    while php > 0 and ehp > 0:
        t += 1
        if t % p.agi == 0:
            atk = p.atk - e.Def
            if atk <= 0:
                print(f"\n{p.name}無法對{e.name}造成傷害")
                i += 1
            else:
                ehp -= atk
                print(f"\n{p.name}對{e.name}造成{atk}點傷害，{e.name}剩餘血量為{ehp}")
        if t % e.agi == 0:
            atk = e.atk - p.Def
            if atk <= 0:
                print(f"\n{e.name}無法對{p.name}造成傷害")
                i += 1
            else:
                php -= atk
                print(f"\n{e.name}對{p.name}造成{atk}點傷害，{p.name}剩餘血量為{php}")
        if i >= 100:
            print(f"\n{p.name}和{e.name}都無法對對方造成傷害")
            return "tie"
    if php <= 0 and ehp <= 0:
        print(f"\n{p.name}和{e.name}同時倒地了")
        return "tie"
    elif php <= 0:
        print(f"\n{e.name}打贏{p.name}了")
        return "lose"
    elif ehp <= 0:
        print(f"\n{p.name}打贏{e.name}了")
        return "win"


def loot_table(lv: int, lv_gap: int):
    item = {
        0: ["無"],
        1: ["金屬性粉末(小)", "木屬性粉末(小)", "水屬性粉末(小)", "火屬性粉末(小)", "土屬性粉末(小)"],
        2: ["金屬性粉末(中)", "木屬性粉末(中)", "水屬性粉末(中)", "火屬性粉末(中)", "土屬性粉末(中)"],
        3: ["金屬性粉末(大)", "木屬性粉末(大)", "水屬性粉末(大)", "火屬性粉末(大)", "土屬性粉末(大)"],
        4: ["金屬性碎片(小)", "木屬性碎片(小)", "水屬性碎片(小)", "火屬性碎片(小)", "土屬性碎片(小)"],
        5: ["金屬性碎片(中)", "木屬性碎片(中)", "水屬性碎片(中)", "火屬性碎片(中)", "土屬性碎片(中)"],
        6: ["金屬性碎片(大)", "木屬性碎片(大)", "水屬性碎片(大)", "火屬性碎片(大)", "土屬性碎片(大)"],
        7: ["金屬性結晶(小)", "木屬性結晶(小)", "水屬性結晶(小)", "火屬性結晶(小)", "土屬性結晶(小)"],
        8: ["金屬性結晶(中)", "木屬性結晶(中)", "水屬性結晶(中)", "火屬性結晶(中)", "土屬性結晶(中)"],
        9: ["金屬性結晶(大)", "木屬性結晶(大)", "水屬性結晶(大)", "火屬性結晶(大)", "土屬性結晶(大)"],
    }
    loot_list: list[str] = []
    if lv_gap <= 0:
        lv_gap = 1
    for _ in range(ri(1, lv_gap)):
        loot_list.append(item[lv][ri(0, len(item[lv]) - 1)])
    return loot_list


print("歡迎遊玩文字遊戲")
while True:
    name = input("\n請輸入角色名字:")
    print(f"\n你的名字是{name}")
    a0 = input("\n確定要用這個名字了嗎 (y)/(n):")
    if a0 == "y" or a0 == "Y" or a0 == "yes" or a0 == "Yes":
        start_time = time()
        locat_time = time()
        player = BuildRoles(name)
        break
print("\n接下來請分配你的角色能力值")
print("角色的能力值共有5種，分別是攻擊、防禦、血量、速度和幸運")
print("你可分配的點數有25點，分配方式是分別把要加給5種能力值的點數數量分別用空白鍵分開")
print("例如:5 5 5 5 5")
print("此例即是平均分配")
while True:
    t = input("\n請輸入要分配的能力值:").split()
    ability: list[int] = [0, 0, 0, 0, 0]
    try:
        for i in range(5):
            ability[i] = int(t[i])
    except:
        print("\n你的輸入有誤，請重新分配")
        continue
    a1 = ability[0] + ability[1] + ability[2] + ability[3] + ability[4]
    if a1 > 25:
        print("\n你分配的點數超過你擁有的可分配點數，請重新分配")
    elif a1 < 25:
        a0 = input("\n你可分配的點數還有剩下的，請問要重新分配嗎? (y)/(n):")
        if a0 == "n" or a0 == "N" or a0 == "no" or a0 == "No":
            break
    else:
        print(f"\n你的能力值\n攻擊:{ability[0]*2}\n防禦:{ability[1]*2}\n血量:{ability[2]*20}\n速度:{ability[3]*20}\n幸運:{ability[4]*10}")
        a0 = input("\n確定要用這種分配了嗎 (y)/(n):")
        if a0 == "y" or a0 == "Y" or a0 == "yes" or a0 == "Yes":
            player.atk = ability[0] * 2
            player.Def = ability[1]
            player.hp = ability[2] * 20
            player.agi = ability[3] * 20
            player.luck = ability[4] * 10
            break

print("\n輸入clear或c就可以清除文字")
player.locat("起始鎮口")
print("\n歡迎來到...")
player.display()

while True:
    while player.location[-1] == "系統介面":
        print("\n系統選項")
        option = choose_option(["角色展示", "打開背包", "保存遊戲", "離開", "關閉遊戲"])
        match option:
            case 1:
                player.display()
            case 2:
                player.show_bag()
            case 3:
                player.save_file()
            case 4:
                player.previous()
            case 5:
                a0 = input("\n關閉遊戲前請記得存檔,是否要關閉遊戲 (y)/(n):")
                if a0 == "y" or a0 == "Y" or a0 == "yes" or a0 == "Yes":
                    print("\n關閉遊戲")
                    exit()
            case _:
                pass

    while player.location[-1] == "起始鎮口":
        option = choose_option(["逛逛村子", "出去打怪", "打開系統"], 3)
        l = ["起始鎮內", "起始鎮外", "系統介面"]
        for i in range(1, len(l) + 1):
            if option == i:
                player.locat(l[i - 1])

    while player.location[-1] == "起始鎮內":
        print("\n歡迎來到起始鎮")
        option = choose_option(["村長家", "雜貨舖", "鐵匠鋪", "草藥鋪", "銀行", "布告欄", "離開", "系統"])
        l = [
            "起始鎮-鎮長家",
            "起始鎮-雜貨舖",
            "起始鎮-鐵匠鋪",
            "起始鎮-草藥鋪",
            "起始鎮-銀行",
            "起始鎮-布告欄",
            "起始鎮外",
            "系統介面",
        ]
        for i in range(1, len(l) + 1):
            if option == i:
                player.locat(l[i - 1])
                print("還沒做好")
                player.previous()

    while player.location[-1] == "起始鎮外":
        print("\n你在起始鎮外，要往哪裡走")
        option = choose_option(["往東走", "往西走", "往南走", "往北走", "回鎮上", "系統"])
        match option:
            case 1 | 2 | 3 | 4 as direction:
                match direction:
                    case 1:
                        player.x += 1
                    case 2:
                        player.x -= 1
                    case 3:
                        player.y += 1
                    case 4:
                        player.y -= 1
                print(f"\n你來到了座標({player.x},{player.y})")
                if ri(1, 100) <= player.luck:
                    a0 = ri(0, 1)
                    print("\n你遇到了...")
                    if a0:
                        lv = player.lv + ri(-1, 1)
                        if lv <= 0:
                            lv = 1
                        print(f"\nLv.{lv}的資源點!")
                    else:
                        lv = player.lv + ri(-1, 1)
                        monster = BuildRoles(f"lv.{lv}monster")
                        monster.atk = ri(8, 12)
                        monster.Def = ri(4, 6)
                        monster.hp = ri(80, 120)
                        monster.agi = ri(80, 120)
                        monster.luck = ri(40, 60)
                        monster.lv = lv
                        monster.location.append(f"起始鎮外({player.x},{player.y})")
                        monster.x = player.x
                        monster.y = player.y
                        for i in range(lv):
                            monster.atk += ri(0, 1)
                            monster.Def += ri(0, 1)
                            monster.hp += ri(0, 10)
                            monster.agi += ri(0, 10)
                            monster.luck += ri(0, 5)
                        print(f"\nLv.{lv}的怪物!")
                        player.locat("戰鬥場")
                else:
                    print("\n你什麼都沒遇到")
            case 5:
                player.locat("起始鎮內")
            case 6:
                player.locat("系統介面")
            case _:
                pass

    while player.location[-1] == "戰鬥場":
        print("\n面對怪物，你決定")
        option = choose_option(["戰鬥", "觀察敵人", "逃跑", "系統"])
        match option:
            case 1:
                result = fighting(player, monster)  # type: ignore
                match result:
                    case "win":
                        loot_list = loot_table(monster.lv, monster.lv - player.lv)  # type: ignore
                        if loot_list == ["無"]:
                            print("\n你什麼都沒拿到")
                        else:
                            print("\n你獲得了:")
                            for i in loot_list:
                                print(i)
                                if i in player.bag:
                                    player.bag[i] += 1
                                else:
                                    player.bag[i] = 1
                                    player.bag_list.append(i)
                    case "lose":
                        pass
                    case "tie":
                        pass
                    case _:
                        pass
                player.previous()
            case 2:
                monster.display()  # type: ignore
            case 3:
                player.previous()
            case 4:
                player.locat("系統介面")
            case _:
                pass
