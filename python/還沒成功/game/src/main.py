import os
from classlib import *


def create_role():
    def load_archive():
        path = data_dir + "\\" + input("請輸入存檔名稱(=角色名稱):")
        if os.path.isfile(path):
            f = open(path)
            data = eval(f.read())
            f.close()
            return Player(data["name"])
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


def main():
    print("你好，歡迎遊玩極簡RPG")
    player = create_role()


if __name__ == "__main__":
    data_dir = "\\".join(__file__.split("\\")[:-2] + ["data"])
    main()
