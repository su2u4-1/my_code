from random import choices as ch
import random


class EquipGenerate:
    def __init__(
        self,
        lv: int = 0,
        quality: int = 0,
        category: int = 0,
        kind: int = 0,
        type: int = 0,
    ):
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
        self.id = random.random()
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
        for _ in range(lv):
            self.att += random.randint(round(basis[0] / 2), basis[0])
            self.de += random.randint(round(basis[1] / 2), basis[1])
            self.agi += random.randint(round(basis[2] / 2), basis[2])
            self.Hp += random.randint(round(basis[3] / 2), basis[3])


class bag:
    def __init__(self, id: int):
        self.id = id
        self.item: dict[str, int] = {}
        self.equip: dict[str, float] = {}

    def add_item(self, item: str, quantity: int):
        if item in self.item:
            self.item[item] += quantity
        else:
            self.item[item] = quantity

    def add_equip(self, name: str, id: float):
        self.equip[name] = id


class CreateAccount:
    def __init__(self, id: int):
        self.id: int = id
        self.m: int = 1000
        self.x: int = random.randint(-25, 25)
        self.y: int = random.randint(-25, 25)
        self.at: float = 30
        self.de: float = 15
        self.ag: float = 15
        self.hp: float = 300
        self.po: int = 0
        self.lv: int = 0
        self.ar: list[int] = [0, 0, 0, 0, 0]
        self.exp: int = 0


def SummonMods(lv: int, type: str, rank: int) -> tuple[int, int, int, int, str, int, list[int], int, int]:
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
    else:
        basis = [-1, -1, -1, -1]
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
    return (
        round(att),
        round(de),
        round(agi),
        round(Hp),
        f"lv.{lv}{attribute}屬性{type}",
        lv,
        attribute_value,
        k,
        exp,
    )


def fighting(
    monster: tuple[int, int, int, float, str, int, list[int], int, int],
    player: list[float],
    monster_name: str,
    attribute: list[int],
) -> list[str]:
    message: list[str] = []
    message.append(f"你開始跟{monster_name}戰鬥")
    if monster[2] > player[2]:
        if attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75:
            l = 0.5
        elif attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75:
            l = 1.5
        else:
            l = 1
        harm = monster[0] * (player[1] / (monster[0] + player[1])) * l
        message.append(f"{monster_name}率先發動攻擊，造成{round(harm,1)}點傷害")
        player[3] -= round(harm, 1)
    elif player[2] > monster[2]:
        if attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75:
            l = 1.5
        elif attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75:
            l = 0.5
        else:
            l = 1
        harm = player[0] * (monster[1] / (player[0] + monster[1])) * l
        message.append(f"你率先發動攻擊，造成{round(harm,1)}點傷害")
        monster = (
            monster[0],
            monster[1],
            monster[2],
            monster[3] - round(harm, 1),
            monster[4],
            monster[5],
            monster[6],
            monster[7],
            monster[8],
        )
    player_time = player[2]
    monster_time = monster[2]
    a = 0
    while monster[3] > 0 and player[3] > 0:
        a += 1
        if player_time > monster_time:
            if attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75:
                l = 1.5
            elif attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75:
                l = 0.5
            else:
                l = 1
            harm = player[0] * (monster[1] / (player[0] + monster[1])) * l
            message.append(f"你攻擊了{monster_name}，造成{round(harm,1)}點傷害")
            monster = (
                monster[0],
                monster[1],
                monster[2],
                monster[3] - round(harm, 1),
                monster[4],
                monster[5],
                monster[6],
                monster[7],
                monster[8],
            )
            player_time += player[2]
        elif monster_time > player_time:
            if attribute[(monster[7] + 3) % 5] > monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] > monster[6][monster[7]] * 0.75:
                l = 0.5
            elif attribute[(monster[7] + 3) % 5] < monster[6][monster[7]] * 1.25 and attribute[(monster[7] + 2) % 5] < monster[6][monster[7]] * 0.75:
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


F = {
    "111111": ("01", "乾"),
    "000000": ("02", "坤"),
    "100010": ("03", "屯"),
    "010001": ("04", "蒙"),
    "111010": ("05", "需"),
    "010111": ("06", "訟"),
    "010000": ("07", "師"),
    "000010": ("08", "比"),
    "111011": ("09", "小畜"),
    "110111": ("10", "履"),
    "111000": ("11", "泰"),
    "000111": ("12", "否"),
    "101111": ("13", "同人"),
    "111101": ("14", "大有"),
    "001000": ("15", "謙"),
    "000100": ("16", "豫"),
    "100110": ("17", "隨"),
    "011001": ("18", "蠱"),
    "110000": ("19", "臨"),
    "000011": ("20", "觀"),
    "100101": ("21", "噬嗑"),
    "101001": ("22", "賁"),
    "000001": ("23", "剝"),
    "100000": ("24", "復"),
    "100111": ("25", "无妄"),
    "111001": ("26", "大畜"),
    "100001": ("27", "頤"),
    "011110": ("28", "大過"),
    "010010": ("29", "坎"),
    "101101": ("30", "離"),
    "001110": ("31", "咸"),
    "011100": ("32", "恆"),
    "001111": ("33", "遯"),
    "111100": ("34", "大壯"),
    "000101": ("35", "晉"),
    "101000": ("36", "明夷"),
    "101011": ("37", "家人"),
    "110101": ("38", "睽"),
    "001010": ("39", "蹇"),
    "010100": ("40", "解"),
    "110001": ("41", "損"),
    "100011": ("42", "益"),
    "111110": ("43", "夬"),
    "011111": ("44", "姤"),
    "000110": ("45", "萃"),
    "011000": ("46", "升"),
    "010110": ("47", "困"),
    "011010": ("48", "井"),
    "101110": ("49", "革"),
    "011101": ("50", "鼎"),
    "100100": ("51", "震"),
    "001001": ("52", "艮"),
    "001011": ("53", "漸"),
    "110100": ("54", "歸妹"),
    "101100": ("55", "豐"),
    "001101": ("56", "旅"),
    "011011": ("57", "巽"),
    "110110": ("58", "兌"),
    "010011": ("59", "渙"),
    "110010": ("60", "節"),
    "110011": ("61", "中孚"),
    "001100": ("62", "小過"),
    "101010": ("63", "既濟"),
    "010101": ("64", "未濟"),
}
URL1 = "https://zh.wikisource.org/zh-hant/周易/"
URL2 = "https://zhouyipro.com/gua"
URL3 = "https://www.eee-learning.com/book/neweee"
URL4 = "https://www.eee-learning.com/simple64/"


def divination(text: str):
    d = ""
    e = ""
    for _ in range(6):
        # 一變39,43
        a = ch((39, 43), (11, 36))[0]
        # 二變31,35,39
        if a == 39:
            a -= ch((3, 7), (10, 9))[0] + 1
        elif a == 43:
            a -= ch((3, 7), (11, 10))[0] + 1
        # 三變24,28,32,36
        if a == 31:
            a -= ch((3, 7), (8, 7))[0]
        elif a == 35:
            a -= ch((3, 7), (9, 8))[0]
        elif a == 39:
            a -= ch((3, 7), (10, 9))[0]
        d += str(a % 8)
        e += str(0 if a > 30 else 1)
    if len(text) < 1:
        s = ""
    else:
        s = f"占卜「{text}」"
    if d == e:
        return s + f"占卜到了【{F[d][1]}】\n解釋:\n{URL2}{F[d][0]}.html\n{URL4}{F[d][0]}\n原文:\n{URL1}{F[d][1]}\n詳細解釋:\n{URL3}{F[d][0]}"
    else:
        return (
            s
            + f"占卜到了【{F[d][1]}之{F[e][1]}】\n解釋:\n{URL2}{F[d][0]}-{F[e][0]}.html\n{URL4}{F[d][0]}\n{URL4}{F[e][0]}\n原文:\n{URL1}{F[d][1]}\n{URL1}{F[e][1]}\n詳細解釋:\n{URL3}{F[d][0]}\n{URL3}{F[e][0]}"
        )
