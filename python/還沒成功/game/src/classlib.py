class Player:
    def __init__(self, TEXT, name: str = "player"):
        self.name = name
        self.location = TEXT["home"]
        self.level = 0  # 關卡等級
        self.lv = 0  # 人物等級
        self.language = "zh-tw"
