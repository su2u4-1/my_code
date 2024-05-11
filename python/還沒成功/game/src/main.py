import os, json
from classlib import *


def switch_language(language):
    global TEXT
    f = open(lan_dir + "\\" + language + ".json", "r")
    data = json.load(f)
    f.close()
    if language != default_language:
        f = open(lan_dir + "\\" + default_language + ".json", "r")
        TEXT = my_dict(data, json.load(f))
        f.close()
    else:
        TEXT = my_dict(data)


def create_role():
    def load_archive():
        path = data_dir + "\\" + input(TEXT["create_role_0"]) + ".json"
        if os.path.isfile(path):
            player = Player(TEXT)
            f = open(path, "r")
            data = json.load(f)
            player.__dict__ = data
            f.close()
            switch_language(player.language)
            return player
        else:
            print(TEXT["create_role_1"])
            return load_archive()

    option = input(f"1.{TEXT['create_role_2']}\t2.{TEXT['create_role_3']}:")
    if option == "1":
        return load_archive()
    elif option == "2":
        return Player(TEXT, input(TEXT["create_role_4"]))
    else:
        print(TEXT["input_error"])
        return create_role()


def save_archive(player: Player, path=None):
    if path is None:
        path = data_dir + f"\\{player.name}.json"
    if os.path.isfile(path):
        inp = input(f"{TEXT['save_archive_0']}\t1.{TEXT['save_archive_1']}\t2.{TEXT['save_archive_2']}\t3.{TEXT['save_archive_3']}:")
        match inp:
            case "1":
                path = data_dir + "\\" + input(TEXT["save_archive_4"]) + ".json"
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
    player.location = "material_shop"
    print("歡迎來到素材商店")
    while True:
        option = input("1.買東西\t2.賣東西\t3.離開:")
        match option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                break
            case _:
                print(TEXT["input_error"])


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
    global player
    print(TEXT["hello_message"])
    player = create_role()
    print(TEXT["player_name"], player.name)
    while True:
        if player.location == "lv":
            print(TEXT["current_location"], TEXT[player.location] + str(player.stage_lv))
        else:
            print(TEXT["current_location"], TEXT[player.location])
        if player.location == "home":
            option = input(
                f"1.{TEXT['go_out']}\t2.{TEXT['material_shop']}\t3.{TEXT['prop_shop']}\t4.{TEXT['blacksmith_shop']}\t5.{TEXT['bank']}\t6.{TEXT['gym']}\t7.{TEXT['task_wall']}\t8.{TEXT['setting']}:"
            )
            match option:
                case "1":
                    player.location = "lv"
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
                    print(TEXT["input_error"])
        else:
            option = input(f"1.{TEXT['go_home']}\t2.{TEXT['explore']}\t3.{TEXT['next_lv']}\t4.{TEXT['setting']}:")
            match option:
                case "1":
                    player.location = "home"
                case "2":
                    explore()
                case "3":
                    next_lv(player.stage_lv)
                case "4":
                    setting()
                case _:
                    print(TEXT["input_error"])


if __name__ == "__main__":
    data_dir = "\\".join(__file__.split("\\")[:-2] + ["data"])
    lan_dir = "\\".join(__file__.split("\\")[:-2] + ["language"])
    default_language = "zh-tw"
    switch_language(default_language)
    main()
