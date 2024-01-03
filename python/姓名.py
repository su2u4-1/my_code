import pickle


def rf(filename):
    with open(f"python\\data\\{filename}.txt", "rb") as f:
        return pickle.load(f)


def sf(filename, data):
    with open(f"python\\data\\{filename}.txt", "wb") as f:
        pickle.dump(data, f)


sn = rf("surname")
n1 = rf("name_1")
n2 = rf("name_2")
n1a2 = rf("name_1and2")


def record_name(surname, name):
    if surname in sn:
        sn[surname] += 1
    else:
        sn[surname] = 1
    if name[0] in n1:
        n1[name[0]] += 1
    else:
        n1[name[0]] = 1
    if len(name) > 1:
        if name[1] in n2:
            n2[name[1]] += 1
        else:
            n2[name[1]] = 1
        if (name[0], name[1]) in n1a2:
            n1a2[(name[0], name[1])] += 1
        else:
            n1a2[(name[0], name[1])] = 1
    else:
        if "No" in n2:
            n2["No"] += 1
        else:
            n2["No"] = 1
        if (name[0], "No") in n1a2:
            n1a2[(name[0], "No")] += 1
        else:
            n1a2[(name[0], "No")] = 1


while True:
    a = input("姓名:").split()
    if a[0] == "exit":
        break
    elif a[0] == "print":
        if len(a) > 1:
            match a[1]:
                case "sn" | "surname" | "姓氏" | "姓":
                    print(sn)
                case "n1" | "name1" | "name_1" | "名1":
                    print(n1)
                case "n2" | "name2" | "name_2" | "名2":
                    print(n2)
                case "名" | "名字" | "name" | "n1a2" | "name_1and2" | "name1and2" | "n1and2":
                    print(n1a2)
        else:
            print(sn)
            print(n1)
            print(n2)
            print(n1a2)
    elif a[0] == "clear":
        sn = {}
        n1 = {}
        n2 = {}
        n1a2 = {}
    elif a[0] == "file":
        if len(a) > 1:
            with open(f"python\\data\\{a[1]}.txt", "r") as f:
                text = eval(f.read())
            for i in text:
                a = i.split(" ")
                try:
                    record_name(a[0], a[1])
                except:
                    print(a)
        else:
            print("輸入錯誤")
    elif len(a) > 1:
        record_name(a[0], a[1])
    else:
        print("輸入錯誤")

sf("surname", sn)
sf("name_1", n1)
sf("name_2", n2)
sf("name_1and2", n1a2)
