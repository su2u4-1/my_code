import os, json
from classlib import *


def switch_language(language):
    global TEXT
    f = open(lan_dir + "\\" + language + ".json", "r")
    data = json.load(f)
    f.close()
    TEXT = data


def create_role():
    def load_archive():
        path = data_dir + "\\" + input("請輸入存檔名稱(=角色名稱):") + ".json"
        if os.path.isfile(path):
            player = Player(TEXT)
            f = open(path, "r")
            data = json.load(f)
            player.__dict__ = data
            f.close()
            switch_language(player.language)
            return player
        else:
            print("檔案不存在")
            return load_archive()

    option = input("1.載入存檔\t2.建立角色:")
    if option == "1":
        return load_archive()
    elif option == "2":
        return Player(TEXT, input("請輸入角色名稱:"))
    else:
        print("輸入錯誤")
        return create_role()


def save_archive(player: Player, path=None):
    if path is None:
        path = data_dir + f"\\{player.name}.json"
    if os.path.isfile(path):
        inp = input("檔案已存在\t1.重命名\t2.覆蓋\t3.取消:")
        match inp:
            case "1":
                path = data_dir + "\\" + input("請輸入存檔名稱:") + ".json"
                save_archive(player, path)
                return
            case "2":
                pass
            case _:
                return
    f = open(path, "w+")
    f.write(json.dumps(player))
    f.close()


def material_shop():
    pass


def prop_shop():
    pass


def blacksmith_shop():
    pass


def bank():
    pass


def gym():
    pass


def task_wall():
    pass


def setting():
    pass


def explore():
    pass


def next_lv(lv: int):
    pass


def main():
    print(TEXT["hello_message"])
    player = create_role()
    print(TEXT["player_name"], player.name)
    while True:
        print(TEXT["current_location"], player.location)
        if player.location == TEXT["home"]:
            option = input(
                f"1.{TEXT['ot_001']}\t2.{TEXT['ot_002']}\t3.{TEXT['ot_003']}\t4.{TEXT['ot_004']}\t5.{TEXT['ot_005']}\t6.{TEXT['ot_006']}\t7.{TEXT['ot_007']}\t8.{TEXT['ot_008']}:"
            )
            match option:
                case "1":
                    player.location = TEXT["lv"] + str(player.level)
                case "2":
                    material_shop()
                case "3":
                    prop_shop()
                case "4":
                    blacksmith_shop()
                case "5":
                    bank()
                case "6":
                    gym()
                case "7":
                    task_wall()
                case "8":
                    setting()
                case _:
                    print("輸入錯誤")
        else:
            option = input(f"1.{TEXT['ot_011']}\t2.{TEXT['ot_012']}\t3.{TEXT['ot_013']}\t4.{TEXT['ot_014']}:")
            match option:
                case "1":
                    player.location = TEXT["home"]
                case "2":
                    explore()
                case "3":
                    next_lv(player.level)
                case "4":
                    setting()
                case _:
                    print("輸入錯誤")


if __name__ == "__main__":
    data_dir = "\\".join(__file__.split("\\")[:-2] + ["data"])
    lan_dir = "\\".join(__file__.split("\\")[:-2] + ["language"])
    switch_language("zh-tw")
    main()
