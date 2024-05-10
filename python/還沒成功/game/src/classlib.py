HOME = "home"
LV = "lv."


class Player:
    def __init__(self, name: str = "player"):
        self.name = name
        self.location = HOME
        self.level = 0 # 關卡等級
        self.lv = 0 # 人物等級
