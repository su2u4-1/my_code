import random


class EquipGenerate:
    def __init__(self, lv=int, quality=int, category=int, kind=int, type=int):
        self.lv = lv
        if quality == 0:
            self.quality = "垃圾"
        elif quality == 1:
            self.quality = "普通"
        elif quality == 2:
            self.quality = "高級"
        elif quality == 3:
            self.quality = "稀有"
        elif quality == 4:
            self.quality = "精良"
        elif quality == 5:
            self.quality = "史詩"
        elif quality == 6:
            self.quality = "傳說"
        elif quality == 7:
            self.quality = "神聖"
        name = "檀梧桐樺楠柳梨楓松柏雕碉隕殞冽飛仙魔神鬼天地陰陽古魚龍鯛虎豹麟龜鯨狼鹿貂燕雁鳥鶯鸚鷹鳳凰雀鵲鴻蜂螳蝶蜘蛛蜈蚣蛇蟒蟾蟬纓嬰瑛一二三四五六七八九十百千萬億兆霸王帝皇狂冷絕明暗艷熱焰炎焱焰纖嬋玉淑聖盛勝烈列大重巨寬無有騰剛柔太連羅獵蘿籮鏍武鬥戰想動靜凈濁灼翔祥降隱飲引飄漂極追感趕敢消銷霄宵蕭囂硝逍凝寧斷踏馭禦駕破毀怨恨希望願忘妄靈巧溫文秀細風雲雨月雪日語破卷卷圈遙金銀銅鐵錫鋼木藤藤根幹枝芽葉花草蕊絲綢緞縷水油泉波浪冰晶月雲霞露霧霖血淚珠火炎焱焰焰星雷電霆日土玉石巖琉璃硫瘤牙沙砂塵光影音氤韻蘊醞韻韞鱗爪皮革甲布羽毛片目眼睛精神空仙魔神鬼天地陰陽男女鳳凰皇帝王風笑嘯樂腸血靈魂魄骨肉筋腦毒闕軟硬長短寬窄廣狹輕重佛魔妖仙神奇寶破粗細紅赤朱血火緋橙橘黃金綠碧青清藍靛紫玄闇暗黑白光素雪粉銀虹彩艷紋鱗形花樣貌如似影音吟吻舌尾首神牙刀槍鎗劍戟斧戎弓環圈琴瑟鼓刺勾鉤鉤爪抓撾拳掌腿箭鏢刃杖棍棒鏟鈀尺匕筆叉轟雷殳針鞭鐗弩矛盾釽鉞功法手訣勁經咒藥丸散膠湯丹茶酒露果粉脂粥糕膏飲草蜜香精箭鏢匕毒鏢針劍刀爪吻舌花鱗環符咒珠鈴蠱羽釘芒石砂沙煞殺痧硝銷鎖根水油草芽膽葵玉髓蛻退藤藤絮火涎綾翎絲皮木目晶睛瞳線炭金星蕊刺莿液齒牙爪酮醇殼礦骨糊瑚弧壺帽盔冠頂帶巾襟幗絲帕簪翎綾莎紗裳衣裝鎧甲衫縷披風氅羅裙褲氈褂袍靴鞋履屐輪踏扣鈴牌指扳佩咒法術方門操氣閃破敗界結體避閉畢壁碧鋒封定禁狂爆暴息寧生隱飛襲障瘴毒流派道魔功奪"
        id1 = random.randint(0, len(name) - 1)
        id2 = random.randint(0, len(name) - 1)
        random.seed(f"{id1}{id2}{quality}{category}{type}{kind}")
        self.id = random.random
        basis = [0, 0, 0, 0]
        if category == 1:
            self.category = "武器"
        elif category == 2:
            self.category = "防裝"
        if kind == 1:
            self.kind = "劍"
            basis[0] += 10
        if type == 1:
            self.type = "單手"
            basis[0] -= 2
            basis[2] += 5
        self.name = name[id1] + name[id2]
        self.name = f"{lv}級【{self.quality}】{self.type}{self.kind}[{self.name}]"
        self.att = 0
        self.de = 0
        self.agi = 0
        self.Hp = 0
        for i in range(lv):
            self.att += random.randint(round(basis[0] / 2), basis[0])
            self.de += random.randint(round(basis[1] / 2), basis[1])
            self.agi += random.randint(round(basis[2] / 2), basis[2])
            self.Hp += random.randint(round(basis[3] / 2), basis[3])


class bag:
    def __init__(self, id):
        self.id = id
        self.item = {}
        self.equip = {}

    def add_item(self, item, quantity):
        if item in self.item:
            self.item[item] += quantity
        else:
            self.item[item] = quantity

    def add_equip(self, name, id):
        self.equip[name] = id


class CreateAccount:
    def __init__(self, id):
        self.id = id
        self.m = 1000
        self.x = random.randint(-25, 25)
        self.y = random.randint(-25, 25)
        self.at = 30
        self.de = 15
        self.ag = 15
        self.hp = 300
        self.po = 0
        self.lv = 0
        self.ar = [0, 0, 0, 0, 0]
        self.exp = 0


def SummonMods(lv, type, rank):
    att = 0
    de = 0
    agi = 0
    Hp = 0
    attribute_list = ["金", "水", "木", "火", "土"]
    k = random.randint(0, 4)
    attribute = attribute_list[k]
    attribute_value = [0, 0, 0, 0, 0]
    if type == "殭屍":
        basis = [10, 5, 3, 110]
    elif type == "骷髏":
        basis = [10, 3, 7, 100]
    elif type == "蜘蛛":
        basis = [10, 5, 8, 100]
    elif type == "巨人":
        basis = [10, 7, 3, 110]
    for _ in range(lv):
        att += random.randint(round(basis[0] / 2), basis[0])
        de += random.randint(round(basis[1] / 2), basis[1])
        agi += random.randint(round(basis[2] / 2), basis[2])
        Hp += random.randint(round(basis[3] / 2), basis[3])
        for i in range(5):
            attribute_value[i] += random.randint(1, 3)
        attribute_value[k] += 2
        attribute_value[(k + 1) % 5] += 1
        attribute_value[(k + 2) % 5] -= 1
    if rank == 1:
        att += att * 0.1
        de += de * 0.1
        agi += agi * 0.1
        Hp += Hp * 0.1
        type = "菁英" + type
    elif rank == 2:
        att += att * 0.5
        de += de * 0.5
        agi += agi * 0.5
        Hp += Hp * 0.5
        type = type + "首領"
    else:
        type = "普通" + type
    exp = round(att + de + agi + Hp)
    return [
        round(att),
        round(de),
        round(agi),
        round(Hp),
        f"lv.{lv}{attribute}屬性{type}",
        lv,
        attribute_value,
        k,
        exp,
    ]


def fighting(monster, player, monster_name, attribute):
    message = []
    message.append(f"你開始跟{monster_name}戰鬥")
    if monster[2] > player[2]:
        if (
            attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25
            and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75
        ):
            l = 0.5
        elif (
            attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25
            and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75
        ):
            l = 1.5
        else:
            l = 1
        harm = monster[0] * (player[1] / (monster[0] + player[1])) * l
        message.append(f"{monster_name}率先發動攻擊，造成{round(harm,1)}點傷害")
        player[3] -= round(harm, 1)
    elif player[2] > monster[2]:
        if (
            attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25
            and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75
        ):
            l = 1.5
        elif (
            attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25
            and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75
        ):
            l = 0.5
        else:
            l = 1
        harm = player[0] * (monster[1] / (player[0] + monster[1])) * l
        message.append(f"你率先發動攻擊，造成{round(harm,1)}點傷害")
        monster[3] -= round(harm, 1)
    player_time = player[2]
    monster_time = monster[2]
    a = 0
    while monster[3] > 0 and player[3] > 0:
        a += 1
        if player_time > monster_time:
            if (
                attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25
                and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75
            ):
                l = 1.5
            elif (
                attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25
                and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75
            ):
                l = 0.5
            else:
                l = 1
            harm = player[0] * (monster[1] / (player[0] + monster[1])) * l
            message.append(f"你攻擊了{monster_name}，造成{round(harm,1)}點傷害")
            monster[3] -= round(harm, 1)
            player_time += player[2]
        elif monster_time > player_time:
            if (
                attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25
                and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75
            ):
                l = 0.5
            elif (
                attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25
                and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75
            ):
                l = 1.5
            else:
                l = 1
            harm = monster[0] * (player[1] / (monster[0] + player[1])) * l
            message.append(f"{monster_name}攻擊了你，造成{round(harm,1)}點傷害")
            player[3] -= round(harm, 1)
            monster_time += monster[2]
        if a >= 100:
            break
    if monster[3] <= 0:
        message.append(f"你打贏了{monster_name}")
    elif player[3] <= 0:
        message.append(f"{monster_name}打敗你了")
    return message


def divination(text=""):
    f = {
        "111111": "乾",
        "000000": "坤",
        "100010": "屯",
        "010001": "蒙",
        "111010": "需",
        "010111": "訟",
        "010000": "師",
        "000010": "比",
        "111011": "小畜",
        "110111": "履",
        "111000": "泰",
        "000111": "否",
        "101111": "同人",
        "111101": "大有",
        "001000": "謙",
        "000100": "豫",
        "100110": "隨",
        "011001": "蠱",
        "110000": "臨",
        "000011": "觀",
        "100101": "噬嗑",
        "101001": "賁",
        "000001": "剝",
        "100000": "復",
        "100111": "无妄",
        "111001": "大畜",
        "100001": "頤",
        "011110": "大過",
        "010010": "坎",
        "101101": "離",
        "001110": "咸",
        "011100": "恆",
        "001111": "遯",
        "111100": "大壯",
        "000101": "晉",
        "101000": "明夷",
        "101011": "家人",
        "110101": "睽",
        "001010": "蹇",
        "010100": "解",
        "110001": "損",
        "100011": "益",
        "111110": "夬",
        "011111": "姤",
        "000110": "萃",
        "011000": "升",
        "010110": "困",
        "011010": "井",
        "101110": "革",
        "011101": "鼎",
        "100100": "震",
        "001001": "艮",
        "001011": "漸",
        "110100": "歸妹",
        "101100": "豐",
        "001101": "旅",
        "011011": "巽",
        "110110": "兌",
        "010011": "渙",
        "110010": "節",
        "110011": "中孚",
        "001100": "小過",
        "101010": "既濟",
        "010101": "未濟",
    }
    f1 = {
        "111111": 1,
        "000000": 2,
        "100010": 3,
        "010001": 4,
        "111010": 5,
        "010111": 6,
        "010000": 7,
        "000010": 8,
        "111011": 9,
        "110111": 10,
        "111000": 11,
        "000111": 12,
        "101111": 13,
        "111101": 14,
        "001000": 15,
        "000100": 16,
        "100110": 17,
        "011001": 18,
        "110000": 19,
        "000011": 20,
        "100101": 21,
        "101001": 22,
        "000001": 23,
        "100000": 24,
        "100111": 25,
        "111001": 26,
        "100001": 27,
        "011110": 28,
        "010010": 29,
        "101101": 30,
        "001110": 31,
        "011100": 32,
        "001111": 33,
        "111100": 34,
        "000101": 35,
        "101000": 36,
        "101011": 37,
        "110101": 38,
        "001010": 39,
        "010100": 40,
        "110001": 41,
        "100011": 42,
        "111110": 43,
        "011111": 44,
        "000110": 45,
        "011000": 46,
        "010110": 47,
        "011010": 48,
        "101110": 49,
        "011101": 50,
        "100100": 51,
        "001001": 52,
        "001011": 53,
        "110100": 54,
        "101100": 55,
        "001101": 56,
        "011011": 57,
        "110110": 58,
        "010011": 59,
        "110010": 60,
        "110011": 61,
        "001100": 62,
        "101010": 63,
        "010101": 64,
    }
    url1 = "https://zh.wikisource.org/zh-hant/周易/"
    url2 = "https://zhouyipro.com/gua"
    url3 = "https://www.eee-learning.com/book/neweee"
    url4 = "https://www.eee-learning.com/simple64/"
    c = []
    d = ""
    e = ""
    for _ in range(6):
        b = [
            39,
            39,
            39,
            39,
            39,
            39,
            39,
            39,
            39,
            39,
            39,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
            43,
        ]
        a = b[random.randint(0, len(b) - 1)]  # 一變39,43
        if a == 39:
            b = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        elif a == 43:
            b = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        a -= b[random.randint(0, len(b) - 1)] + 1  # 二變31,35,39
        if a == 31:
            b = [3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7]
        elif a == 35:
            b = [3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7]
        elif a == 39:
            b = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        a -= b[random.randint(0, len(b) - 1)]  # 三變24,28,32,36
        c.append(a / 4)
    for i in c:
        if i == 6:  # .--
            d += "0"
            e += "1"
        elif i == 7:  # -
            d += "1"
            e += "1"
        elif i == 8:  # --
            d += "0"
            e += "0"
        elif i == 9:  # -.
            d += "1"
            e += "0"
    if len(str(f1[d])) == 1:
        g = "0" + str(f1[d])
    else:
        g = str(f1[d])
    if len(str(f1[e])) == 1:
        h = "0" + str(f1[e])
    else:
        h = str(f1[e])
    if d != e:
        if len(text) >= 1:
            return f"占卜{text}占卜到了{f[d]}之{f[e]}\n解釋:\n{url2}{f1[d]}-{f1[e]}.html\n{url4}{f1[d]}\n{url4}{f1[e]}\n原文:\n{url1}{f[d]}\n{url1}{f[e]}\n詳細解釋:\n{url3}{g}\n{url3}{h}"
        else:
            return f"占卜到了{f[d]}之{f[e]}\n解釋:\n{url2}{f1[d]}-{f1[e]}.html\n{url4}{f1[d]}\n{url4}{f1[e]}\n原文:\n{url1}{f[d]}\n{url1}{f[e]}\n詳細解釋:\n{url3}{g}\n{url3}{h}"
    else:
        if len(text) >= 1:
            return f"占卜{text}占卜到了{f[d]}\n解釋:\n{url2}{f1[d]}.html\n{url4}{f1[d]}\n原文:\n{url1}{f[d]}\n詳細解釋:\n{url3}{g}"
        else:
            return f"占卜到了{f[d]}\n解釋:{url2}{f1[d]}.html\n{url4}{f1[d]}\n原文:\n{url1}{f[d]}\n詳細解釋:\n{url3}{g}"
