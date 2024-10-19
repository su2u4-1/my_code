from typing import TextIO

link = "python\\data\\"
print("正在讀取質數")
with open(link + "質數.txt", "r") as f:
    a = list(map(int, f.readlines()))
print("質數讀取完畢")
print(a[-1])


def f2(b: int):
    for i in a:
        if b % i == 0:
            return False
    else:
        return True


def f1(c: int, b: int, f: TextIO):
    for i in range(c - (c % 6), b + (6 - b % 6), 6):
        if f2(i + 1):
            a.append(i + 1)
            f.write(str(i + 1) + "\n")
        if f2(i + 5):
            a.append(i + 5)
            f.write(str(i + 5) + "\n")


def f0(c: str) -> dict[int, int] | str:
    try:
        n = int(c)
    except:
        return "error: 須為正整數"
    if n <= 0:
        return "error: 須為正整數"
    if n == 1:
        return {1: 1}
    if n > a[-1]:
        print("正在計算新質數")
        f = open(link + "質數.txt", "a+")
        f1(a[-1] + 1, n + 1, f)
        f.close()
        print("新質數記錄完畢")
    if n in a:
        return {n: 1}
    b: dict[int, int] = {}
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


print(f0(input("要計算的數:")))
