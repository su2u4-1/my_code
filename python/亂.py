from pickle import dump, load  # type: ignore
from random import randint as ri
from typing import Literal, Optional


def rv(va: int, vb: int, mx: int = 100, mi: int = 0) -> int:
    return ri(max((va + vb) // 2 - (mx - mi) // 10, mi), min((va + vb) // 2 + (mx - mi) // 10, mx))


class Human:
    def __init__(self, ID: str, gender: Literal["male", "female"], age: int, charm: int, health: int, fertility: int):
        self.ID = ID
        self.gender = gender
        self.age = age
        self.is_alive = True
        self.partner: Optional[Human] = None
        self.children: list[Human] = []
        self.parents: tuple[Optional[Human], Optional[Human]] = (None, None)
        self.charm = charm  # 魅力值，影響結婚機率
        self.health = health  # 健康值，影響死亡機率
        self.fertility = fertility  # 生育率，影響生子機率

    def age_one_year(self) -> None:
        self.age += 1
        if self.age >= 60:
            self.charm = ri(int(self.charm * 0.75), int(self.charm * 0.9))
        elif self.age >= 50:
            self.charm = ri(int(self.charm * 0.75), int(self.charm * 0.9))
        elif self.age >= 40:
            self.charm = ri(int(self.charm * 0.75), int(self.charm * 0.9))
        elif self.age >= 30:
            self.charm = ri(int(self.charm * 0.75), int(self.charm * 0.9))
        self.health -= ri(1, ri(1, ri(1, 5)))  # 每年健康值下降
        # if ri(1, 50) > self.health:  # 健康值影響死亡機率
        if self.health <= 0:  # 隨機死亡年齡或健康值耗盡
            self.is_alive = False
            if self.partner is not None:
                self.partner.partner = None
                log[self.partner.ID].append(f"{year} 年 '{self.partner.ID}' {self.partner.age} 歲: 喪偶")
            log[self.ID].append(f"{year} 年 '{self.ID}' {self.age} 歲: 死亡")

    def try_to_marry(self, other: "Human") -> None:
        if other.is_alive and self.partner is None and other.partner is None:
            if self.gender != other.gender and ri(1, 100) < self.charm and ri(1, 100) < other.charm:  # 魅力值影響結婚機率
                self.partner = other
                other.partner = self
                log[self.ID].append(f"{year} 年, '{self.ID}' {self.age} 歲: 與 {other.age} 歲的 {other.ID} 結婚")
                log[other.ID].append(f"{year} 年, '{other.ID}' {other.age} 歲: 與 {self.age} 歲的 {self.ID} 結婚")

    def try_to_have_children(self) -> None:
        global population_ID
        if self.partner is not None and self.partner.is_alive and self.gender == "female":
            if ri(2, 200) < self.fertility + self.partner.fertility:  # 生育率影響生子機率
                child_gender = ("male", "female")[ri(0, 1)]
                child_ID = f"{population_ID}({self.partner.ID}, {self.ID})"
                population_ID += 1
                child = Human(child_ID, child_gender, 0, rv(self.charm, self.partner.charm), rv(self.health, self.partner.health), rv(self.fertility, self.partner.fertility))
                self.children.append(child)
                self.partner.children.append(child)
                child.parents = (self.partner, self)
                new_population.append(child)
                log[self.ID].append(f"{year} 年, '{self.ID}' {self.age} 歲: 生下 {child_ID}")
                log[self.partner.ID].append(f"{year} 年, '{self.partner.ID}' {self.partner.age} 歲: 生下 {child_ID}")
                log[child_ID] = [f"{child.gender}, {child.charm}, {child.health}, {child.fertility}", f"{year} 年, '{child_ID}' {child.age} 歲: 出生"]


# 初始化
population_ID = 3
population: list[Human] = [Human("1", "male", 20, 100, 100, 100), Human("2", "female", 20, 100, 100, 100)]
log: dict[str, list[str]] = {"1": ["male, 100, 100, 100", "-20 年, '1' 0 歲: 出生"], "2": ["female, 100, 100, 100", "-20 年 '2' 0 歲: 出生"]}
log_text = "模擬開始\n"


years_to_simulate = 100
for year in range(years_to_simulate):
    new_population: list[Human] = []
    for human in population:
        human.age_one_year()
    for human in population:
        if human.is_alive and human.age > 18:
            for other in population:
                if human != other and other.is_alive and other.age >= 18:
                    human.try_to_marry(other)
            human.try_to_have_children()
    # 移除死亡的人類
    population = [human for human in population if human.is_alive]
    population.extend(new_population)
    log_text += f"Year {year + 1}: {len(population)} 人存活。\n"
    print(f"Year {year + 1}: {len(population)} 人存活。")
    if len(population) <= 0:
        log_text += "所有人類已死亡，模擬結束。\n"
        print("所有人類已死亡，模擬結束。")
        break

# 結果輸出
log_text += f"模擬結束，共有 {len(population)} 人存活。\n"
# print(f"模擬結束，共有 {len(population)} 人存活。")
for k, v in log.items():
    if len(v) > 3 or (len(v) == 3 and not v[2].endswith("死亡")):
        log_text += f"{k}:\n"
        # print(f"{k}:")
        for i in v:
            log_text += f"    {i}\n"
            # print(f"    {i}")

with open("simulation_log.txt", "w", encoding="utf-8") as f:
    f.write(log_text)

with open("simulation_log.pkl", "wb") as f:
    dump(log, f)

# with open("simulation_log.pkl", "rb") as f:
#     loaded_log = load(f)


def process():
    import re

    def f0(s: str) -> str:
        return re.sub(r"\d+", lambda m: f'"{m.group(0)}"', s)

    def f1(s: str) -> str:
        # 反覆處理，直到沒有不含內層大括號的 {} 為止
        while True:
            # 匹配最內層的大括號：`{` 內部不包含 `{` 或 `}` 的內容
            new_s, count = re.subn(r"\{([^{}t]*)\}", r"[\1t]", s)
            if count == 0:
                break
            s = new_s
        return s.replace("t", "")

    def parse_t_name(line: str) -> str:
        return line.replace("\n", "").replace("(", ":(").replace("(", "{").replace(")", "}")

    txt = []
    with open("all_name.txt") as f:
        txt = f.readlines()

    result: list[str] = []
    for i in txt:
        # result.append(parse_t_name(i.replace("(1, 2)", "")))
        result.append(parse_t_name(i))

    e = ",\n".join(result)
    e = f1(e)
    e = f0(e)
    e = e.replace('["1", "2"]', "[]")
    # e = e.replace('{"3":[], "4":[]}', '"3,4"')
    # e = e.replace('{"7":[], "5":[]}', '"7,5"')
    # e = e.replace('{"11":[], "6":[]}', '"11,6"')
    # e = e.replace('{"15":[], "9":[]}', '"15,9"')
    # e = e.replace('{"14":[], "10":[]}', '"14,10"')
    # e = e.replace('{"13":[], "8":[]}', '"13,8"')
    # e = e.replace('{"17":[], "12":[]}', '"17,12"')
    # e = e.replace('{"21":[], "16":[]}', '"21,16"')
    # e = e.replace("[]", '"1,2"')
    e = e.replace('"1"', '"1": "god"')
    e = e.replace('"2"', '"2": "god"')

    # 將結果保存為JSON文件
    with open("parsed_names.json", "w", encoding="utf-8") as f:
        f.write("{" + e + "}")
