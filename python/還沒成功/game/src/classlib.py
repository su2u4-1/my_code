class Player:
    def __init__(self, TEXT, name: str = "player"):
        self.name = name
        self.location = TEXT["home"]
        self.stage_lv = 0  # 關卡等級
        self.lv = 0  # 人物等級
        self.language = "zh-tw"
        self.money = 100


class my_dict(dict):
    def __init__(self, *dicts, default=None):
        super().__init__()
        self.dicts = dicts
        self.default = default

    def __getitem__(self, key):
        for dictionary in self.dicts:
            if key in dictionary:
                return dictionary[key]
        if self.default is None:
            return f"text ['{key}'] not found"
        return self.default
