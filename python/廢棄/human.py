from random import choice
from random import randint as ri
from time import strftime, localtime
from typing import Optional


def random_str(length: int, use_uppercase: bool, use_lowercase: bool, use_digits: bool, use_punctuation: bool):
    chars = ""
    if use_uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lowercase:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if use_digits:
        chars += "0123456789"
    if use_punctuation:
        chars += "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    return "".join(choice(chars) for _ in range(length))


class Human:
    def __init__(self, h1: Optional["Human"], h2: Optional["Human"]):
        self.age = 0
        self.gender = ri(1, 2)
        self.health = 100
        self.charm = 100
        if h1 is not None and h2 is not None:
            self.health = ri(((h1.health + h2.health) // 2) - 5, ((h1.health + h2.health) // 2) + 5)
            self.charm = ri(((h1.charm + h2.charm) // 2) - 5, ((h1.charm + h2.charm) // 2) + 5)
        self.health = min(max(self.health, 0), 100)
        self.charm = min(max(self.charm, 0), 100)
        self.marriage = ""
        self.id = random_str(10, True, True, True, False)
        self.father: str = ""
        self.mother: str = ""
        if h1 is not None:
            self.father: str = h1.id
        if h2 is not None:
            self.mother: str = h2.id

    def __getitem__(self, key: int) -> int | Optional[str]:
        if key == 0:
            return self.age
        elif key == 1:
            return self.gender
        elif key == 2:
            return self.health
        elif key == 3:
            return self.charm
        elif key == 4:
            return self.marriage
        elif key == 5:
            return self.id
        elif key == 6:
            return self.father
        elif key == 7:
            return self.mother


# ["年紀","性別","健康","魅力","婚姻","編號","父","母"]
# {"0000000000":[100,2,100,100,"ZZZZZZZZZZ","0000000000","",""]}
human: dict[str, Human] = {}
human_list: list[str] = []
dead: list[Human] = []
year = 0


for _ in range(1000):
    f1 = Human(None, None)
    f1.age = 20
    f1.gender = 1
    f1.health = 100
    f1.charm = 100
    f1.marriage = "ZZZZZZZZZZ"
    f1.id = "0000000000"
    f2 = Human(None, None)
    f2.age = 20
    f2.gender = 2
    f2.health = 100
    f2.charm = 100
    f2.marriage = "0000000000"
    f2.id = "ZZZZZZZZZZ"
    b = Human(f1, f2)
    human_list.append(b.id)
    human[b.id] = b

while True:
    now_born = 0
    now_dead = 0
    marryM: list[str] = []
    marryF: list[str] = []
    for i in human_list:
        try:
            human[i].age += 1
        except:
            pass
    for i in human_list:
        if human[i].age > 20 and human[i].age < 50 and human[i].marriage == "":
            if human[i][1] == 1:
                marryM.append(human[i].id)
            if human[i][1] == 2:
                marryF.append(human[i].id)
    for i in marryM:
        a = human[i]
        for _ in range(3):
            b = human[choice(marryF)]
            if a.charm > ri(1, 100) and b.charm > ri(1, 100):
                a.marriage = b.id
                b.marriage = a.id
                human[a.id] = a
                human[b.id] = b
                marryM.remove(i)
                marryF.remove(b.id)
                break
    for i in marryF:
        a = human[i]
        for _ in range(3):
            b = human[choice(marryM)]
            if a.charm > ri(1, 100) and b.charm > ri(1, 100):
                a.marriage = b.id
                b.marriage = a.id
                human[a.id] = a
                human[b.id] = b
                marryF.remove(i)
                marryM.remove(b.id)
                break
    for i in human_list:
        if human[i].health - human[i].age < ri(1, 80):
            dead.append(human[i])
            human.pop(i)
            human_list.remove(i)
            now_dead += 1
    for i in human_list:
        if human[i].health + human[human[i].marriage].health > ri(1, 100):
            b = Human(human[i], human[human[i].marriage])
            human_list.append(b.id)
            human[b.id] = b
            now_born += 1
    year += 1
    print("年分", year)
    print("人口數", len(human))
    print("年出生數", now_born)
    print("年死亡數", now_dead)
    print("未婚男", len(marryM))
    print("未婚女", len(marryF))
    if len(human) == 0:
        a = input("所有人類死亡,輸入det查看詳細資料,按enter鍵結束程式")
        if a == "det":
            if len(dead) > 10000:
                f = strftime("data%Y-%m-%d-%H-%M-%S", localtime())
                with open("%s.txt" % (f), "w+") as g:
                    g.write(f"年分{year}\n人口{human}\n編號{human_list}\n年出生數{now_born}\n年死亡數{now_dead}\n未婚男{marryM}\n未婚女{marryF}\n已死亡{dead}")
                print("由於資料太多,所以已經把資料儲存在%s.txt" % (f))
            else:
                print("年分", year)
                print("已死亡", dead)
            a = input("按enter鍵結束程式")
        break
    else:
        a = input("輸入det查看詳細資料,輸入off關閉程式,按enter鍵進入下一年")
        if a == "det":
            if len(human) > 10000:
                f = strftime("data%Y-%m-%d-%H-%M-%S", localtime())
                with open("%s.txt" % (f), "w+") as g:
                    g.write(f"年分{year}\n人口{human}\n編號{human_list}\n年出生數{now_born}\n年死亡數{now_dead}\n未婚男{marryM}\n未婚女{marryF}\n已死亡{dead}")
                print("由於資料太多,所以已經把資料儲存在%s.txt" % (f))
            else:
                print("年分", year)
                print("人口", human)
                print("編號", human_list)
                print("年出生數", now_born)
                print("年死亡數", now_dead)
                print("未婚男", marryM)
                print("未婚女", marryF)
                print("已死亡", dead)
            a = input("輸入off關閉程式,按enter鍵進入下一年")
            if a == "off":
                break
