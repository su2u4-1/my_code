link = "python\\data\\"
print("正在讀取質數")
f = open(link + "質數.txt", "r")
a = []
ab = f.readlines()
for i in ab:
    a.append(int(i))
f.close()
print("質數讀取完畢")
print(a[-1])


def func1(b):
    for i in a:
        if b % i == 0:
            break
    else:
        return True
    return False


def func(c, b, f):
    n = []
    for i in range(c - (c % 6), b + (6 - b % 6), 6):
        if func1(i + 1):
            a.append(i + 1)
            f.write(str(i + 1) + "\n")
        if func1(i + 5):
            a.append(i + 5)
            f.write(str(i + 5) + "\n")


def abc(n):
    try:
        n = int(n)
    except:
        return {"error": "須為正整數"}
    if n <= 0:
        return {"error": "須為正整數"}
    if n == 1:
        return {1: 1}
    if n > a[-1]:
        print("正在計算新質數")
        f = open(link + "質數.txt", "a+")
        func(a[-1] + 1, n + 1, f)
        f.close()
        print("新質數記錄完畢")
    if n in a:
        return {n: 1}
    b = {}
    while n > 1:
        for i in a:
            if i > n:
                break
            if n % i == 0:
                if i in b:
                    b[i] += 1
                else:
                    b[i] = 1
                n /= i
    return b


print(abc(input("要計算的數:")))
