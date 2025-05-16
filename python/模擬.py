from random import randint as ri
from random import choice as rc
from typing import Literal, Optional
import json


class Person:
    def __init__(
        self, id: str, age: int, father: Optional["Person"], mother: Optional["Person"], gender: Literal["male", "female"], luck: int = -1, spouse: Optional["Person"] = None
    ) -> None:
        self.id = id
        self.age = age
        self.father = father
        self.mother = mother
        self.gender = gender
        if luck == -1:
            luck = ri(0, 99)
        self.luck = luck
        self.spouse = spouse
        self.children: list[Person] = []
        if father is not None:
            father.children.append(self)
        if mother is not None:
            mother.children.append(self)
        self.log: list[tuple[int, int, str]] = [
            (year, 0, "出生, 父親: " + (father.id if father is not None else "無") + ", 母親: " + (mother.id if mother is not None else "無") + ", 性別: " + self.gender)
        ]

    def __repr__(self) -> str:
        return f"(ID: {self.id}, 年齡: {self.age}, 父親: {self.father.id if self.father is not None else '無'}, 母親: {self.mother.id if self.mother is not None else '無'}, 性別: {self.gender}, 幸運值: {self.luck}, 配偶: {self.spouse.id if self.spouse is not None else '無'}, 小孩: {[i.id for i in self.children]})"


people: list[Person] = []
f_tree: dict[str, list[str]] = {}
m_tree: dict[str, list[str]] = {}

year = 0
people_id = 2

# for _ in range(100):
#     people.append(Person(str(people_id), 0, None, None, ("male", "female")[ri(0, 1)]))
#     people_id += 1

people.append(Person("0", 0, None, None, "male", 100))
people.append(Person("1", 0, None, None, "female", 100))
f_tree["0"] = []
m_tree["1"] = []

a, b = 0, 0
total_die: list[Person] = []
log: list[str] = []
loop = 100
while True:
    for _ in range(loop):
        # 新生兒, 結婚, 離婚, 死亡, 夭折, 未成年, 壯年人口, 老年人口
        statistics: list[int] = [0, 0, 0, 0, 0, 0, 0, 0]
        year += 1

        for i in people:
            i.age += 1
            if i.age < 18:
                statistics[5] += 1
            elif i.age < 75:
                statistics[6] += 1
            else:
                statistics[7] += 1

        for i in people:
            if i.spouse is not None:
                if i.luck + i.spouse.luck > ri(0, 1600) and i.age < ri(50, 75) and i.spouse.age < ri(50, 75):
                    if i.gender == "male":
                        people.append(Person(str(people_id), 0, i, i.spouse, ("male", "female")[ri(0, 1)], ((i.luck + i.spouse.luck) // 2, -1)[ri(0, 1)]))
                    else:
                        people.append(Person(str(people_id), 0, i.spouse, i, ("male", "female")[ri(0, 1)], ((i.luck + i.spouse.luck) // 2, -1)[ri(0, 1)]))
                    if people[-1].gender == "male":
                        i.log.append((year, i.age, "小孩出生, ID: " + people[-1].id + ", 性別: male"))
                        i.spouse.log.append((year, i.spouse.age, "小孩出生, ID: " + people[-1].id + ", 性別: male"))
                        f_tree[people[-1].id] = []
                    else:
                        i.log.append((year, i.age, "小孩出生, ID: " + people[-1].id + ", 性別: female"))
                        i.spouse.log.append((year, i.spouse.age, "小孩出生, ID: " + people[-1].id + ", 性別: female"))
                        m_tree[people[-1].id] = []
                    if people[-1].father is not None:
                        f_tree[people[-1].father.id].append(people[-1].id)
                    if people[-1].mother is not None:
                        m_tree[people[-1].mother.id].append(people[-1].id)
                    people_id += 1
                    statistics[0] += 1

        for i in people:
            if i.age >= 18:
                if i.spouse is None and i.luck > ri(0, 50):
                    j = rc(people)
                    if j != i and j.gender != i.gender and j.age >= 18 and j.spouse is None:
                        if j.luck > ri(0, 50) and i.luck + j.luck > ri(0, abs(i.age - j.age) * 10):
                            print("雙方年齡差: " + str(abs(i.age - j.age)))
                            a += abs(i.age - j.age)
                            b += 1
                            if i.father == j or i.mother == j or j.father == i or j.mother == i:
                                input(i.id + ", " + j.id)
                            i.log.append((year, i.age, "結婚, 配偶: " + j.id))
                            j.log.append((year, j.age, "結婚, 配偶: " + i.id))
                            i.spouse = j
                            j.spouse = i
                            statistics[1] += 1

        for i in people:
            if i.spouse is not None:
                if i.luck + i.spouse.luck < ri(0, 50):
                    i.log.append((year, i.age, "離婚, 配偶: " + i.spouse.id))
                    i.spouse.log.append((year, i.spouse.age, "離婚, 配偶: " + i.id))
                    i.spouse.spouse = None
                    i.spouse = None
                    statistics[2] += 1

        die: list[Person] = []
        for i in people:
            if ri(0, i.age) > i.luck:
                statistics[3] += 1
                if i.age < 18:
                    i.log.append((year, i.age, "早夭, 享年: " + str(i.age)))
                    statistics[4] += 1
                else:
                    i.log.append((year, i.age, "去世, 享年: " + str(i.age)))
                die.append(i)
                if i.spouse is not None:
                    i.spouse.log.append((year, i.spouse.age, "喪偶, 配偶: " + i.id))
                    i.spouse.spouse = None
                    i.spouse = None
                    statistics[2] += 1

        for i in die:
            people.remove(i)
        total_die.extend(die)

        if len(people) == 0:
            print(f"{year}年，所有人都去世了")
            break

        n = sum(len(i.children) for i in people)
        m = sum(1 if i.spouse is not None else 0 for i in people) // 2
        m = 0 if m == 0 else n / m
        l = len(total_die)
        l = 0 if l == 0 else sum(i.age for i in total_die) / l

        report = f"\n{year}年\n新生兒：{statistics[0]}人\n結婚：{statistics[1]}對\n離婚：{statistics[2]}對\n死亡：{statistics[3]}人\n夭折：{statistics[4]}人\n未成年：{statistics[5]}人\n壯年人口：{statistics[6]}人\n老年人口：{statistics[7]}人\n總人口：{len(people)}人\n總死亡人數：{len(total_die)}人\n出生率：{statistics[0]/len(people)*100:.2f}%\n結婚率：{statistics[1]/len(people)*100:.2f}%\n離婚率：{statistics[2]/len(people)*100:.2f}%\n死亡率：{statistics[3]/len(people)*100:.2f}%\n夭折率：{statistics[4]/len(people)*100:.2f}%\n平均小孩數：{n/len(people):.2f}\n每對夫妻平均後代數量：{m:.2f}\n平均年齡：{sum(i.age for i in people)/len(people):.2f}\n平均壽命：{l:.2f}"
        print(report)
        log.append(report)

    if len(people) == 0:
        print(f"{year}年，所有人都去世了")
        break

    if input(f"\n是否繼續下個{loop}年？(Y/n)") in ("n", "N", "no", "No", "NO"):
        print("模擬結束")
        break

with open("./python/data/log.txt", "w", encoding="utf-8") as f:
    for i in log:
        f.write(i + "\n")

with open("./python/data/all_log.txt", "w", encoding="utf-8") as f:
    t = total_die + people
    t.sort(key=lambda x: int(x.id))
    for i in t:
        f.write(i.id + ":\n")
        for j in i.log:
            f.write(f"    {j[0]}年({j[1]}歲): {j[2]}\n")
        f.write("\n")

with open("./python/data/f_tree.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(f_tree))
with open("./python/data/m_tree.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(m_tree))
