import random, randomstr, time

# ["年紀","性別","健康","魅力","婚姻","編號","父","母"]
# {'0000000000':[100,2,100,100,'ZZZZZZZZZZ',None,None]}
human = {}
humanlist = []
marryM = []
marryF = []
dead = []
year = 0


def summonhuman(h1, h2):
    nowhuman = ["年紀", "性別", "健康", "魅力", "婚姻", "編號", "父", "母"]
    nowhuman[0] = 0
    nowhuman[1] = random.randint(1, 2)
    nowhuman[2] = random.randint(((h1[2] + h2[2]) / 2) - 5, ((h1[2] + h2[2]) / 2) + 5)
    nowhuman[3] = random.randint(((h1[3] + h2[3]) / 2) - 5, ((h1[3] + h2[3]) / 2) + 5)
    if nowhuman[2] > 100:
        nowhuman[2] = 100
    if nowhuman[2] < 0:
        nowhuman[2] = 0
    if nowhuman[3] > 100:
        nowhuman[3] = 100
    if nowhuman[3] < 0:
        nowhuman[3] = 0
    nowhuman[4] = 0
    nowhuman[5] = randomstr.randomstr(10, True, True, True, False)
    nowhuman[6] = h1[5]
    nowhuman[7] = h2[5]
    return nowhuman


a = 0
while a != 1000:
    b = summonhuman(
        [20, 1, 100, 100, "ZZZZZZZZZZ", "0000000000", None, None],
        [20, 2, 100, 100, "0000000000", "ZZZZZZZZZZ", None, None],
    )
    humanlist.append(b[5])
    human[b[5]] = b
    a += 1
while True:
    nowborn = 0
    nowdead = 0
    marryM = []
    marryF = []
    for i in range(0, len(humanlist)):
        try:
            human[humanlist[i]][0] += 1
        except:
            pass
    for i in range(0, len(humanlist)):
        try:
            if (
                human[humanlist[i]][0] > 20
                and human[humanlist[i]][0] < 50
                and human[humanlist[i]][4] == 0
            ):
                if human[humanlist[i]][1] == 1:
                    marryM.append(human[humanlist[i]][5])
                if human[humanlist[i]][1] == 2:
                    marryF.append(human[humanlist[i]][5])
        except:
            pass
    for i in range(0, len(marryM)):
        try:
            a = human[marryM[i]]
            d = 0
            while d != 3:
                c = random.randint(0, len(marryF))
                d += 1
                if a[3] > random.randint(1, 100) and b[3] > random.randint(1, 100):
                    a[4] = b[5]
                    b[4] = a[5]
                    human[a[5]] = a
                    human[b[5]] = b
                    del marryM[i]
                    del marryF[c]
                    break
        except:
            pass
    for i in range(0, len(marryF)):
        try:
            a = human[marryF[i]]
            d = 0
            while d != 3:
                c = random.randint(0, len(marryM))
                b = human[marryM[c]]
                d += 1
                if a[3] > random.randint(1, 100) and b[3] > random.randint(1, 100):
                    a[4] = b[5]
                    b[4] = a[5]
                    human[a[5]] = a
                    human[b[5]] = b
                    del marryF[i]
                    del marryM[c]
                    break
        except:
            pass
    for i in range(0, len(humanlist)):
        try:
            if human[humanlist[i]][2] - human[humanlist[i]][0] < random.randint(1, 80):
                dead.append(human[humanlist[i]])
                del human[humanlist[i]]
                del humanlist[i]
                nowdead += 1
        except:
            pass
    for i in range(0, len(humanlist)):
        try:
            if human[humanlist[i]][2] + human[human[humanlist[i]][4]][
                2
            ] > random.randint(1, 100):
                b = summonhuman(human[humanlist[i]], human[human[humanlist[i]][4]])
                humanlist.append(b[5])
                human[b[5]] = b
                nowborn += 1
        except:
            pass
    year += 1
    print("年分", year)
    print("人口數", len(human))
    print("年出生數", nowborn)
    print("年死亡數", nowdead)
    print("未婚男", len(marryM))
    print("未婚女", len(marryF))
    if len(human) == 0:
        a = input("所有人類死亡,輸入det查看詳細資料,按enter鍵結束程式")
        if a == "det":
            if len(dead) > 10000:
                f = time.strftime("data%Y-%m-%d-%H-%M-%S", time.localtime())
                with open("C:\\Users\\User\\Desktop\\%s.txt" % (f), "w+") as g:
                    g.write(
                        f"年分{year}\n人口{human}\n編號{humanlist}\n年出生數{nowborn}\n年死亡數{nowdead}\n未婚男{marryM}\n未婚女{marryF}\n已死亡{dead}"
                    )
                print("由於資料太多,所以已經把資料儲存在桌面的%s.txt" % (f))
            else:
                print("年分", year)
                print("已死亡", dead)
            a = input("按enter鍵結束程式")
        break
    else:
        a = input("輸入det查看詳細資料,輸入off關閉程式,按enter鍵進入下一年")
        if a == "det":
            if len(human) > 10000:
                f = time.strftime("data%Y-%m-%d-%H-%M-%S", time.localtime())
                with open("C:\\Users\\User\\Desktop\\%s.txt" % (f), "w+") as g:
                    g.write(
                        f"年分{year}\n人口{human}\n編號{humanlist}\n年出生數{nowborn}\n年死亡數{nowdead}\n未婚男{marryM}\n未婚女{marryF}\n已死亡{dead}"
                    )
                print("由於資料太多,所以已經把資料儲存在桌面的%s.txt" % (f))
            elif a == "off":
                break
            else:
                print("年分", year)
                print("人口", human)
                print("編號", humanlist)
                print("年出生數", nowborn)
                print("年死亡數", nowdead)
                print("未婚男", marryM)
                print("未婚女", marryF)
                print("已死亡", dead)
            a = input("輸入off關閉程式,按enter鍵進入下一年")
            if a == "off":
                break
