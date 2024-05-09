import os, json
from classlib import *


def create_role():
    def load_archive():
        path = data_dir + "\\" + input("請輸入存檔名稱(=角色名稱):") + ".json"
        if os.path.isfile(path):
            player = Player()
            f = open(path, "r")
            data = json.load(f.read())
            player.__dict__ = data
            f.close()
            return player
        else:
            print("檔案不存在")
            return load_archive()

    option = input("1.載入存檔\t2.建立角色:")
    if option == "1":
        return load_archive()
    elif option == "2":
        return Player(input("請輸入角色名稱:"))
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
    print("你好，歡迎遊玩極簡RPG")
    player = create_role()
    print("player name:", player.name)
    while True:
        print("current location:", player.location)
        if player.location == HOME:
            option = input("1.出門\t2.素材商店\t3.道具商店\t4.打鐵舖\t5.銀行\t6.道館\t7.任務牆\t8.設定")
            match option:
                case "1":
                    player.location = LV + "0"
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
            option = input("1.回家\t2.探索\t3.進入下一關\t4.設定")
            match option:
                case "1":
                    player.location = HOME
                case "2":
                    explore()
                case "3":
                    next_lv(int(player.location[len(LV) :]))
                case "4":
                    setting()
                case _:
                    print("輸入錯誤")


if __name__ == "__main__":
    data_dir = "\\".join(__file__.split("\\")[:-2] + ["data"])
    main()
