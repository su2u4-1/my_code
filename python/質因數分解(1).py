def f2(b: int):
    if b == 2:
        return True
    for i in range(3, b // 2 + 2, 2):
        if b % i == 0:
            return False
    else:
        return True


try:
    n = int(input("要計算的數:"))
except:
    print("錯誤: 輸入須為正整數")
    exit()
if n <= 0:
    print("錯誤: 輸入須為正整數")
if n == 1:
    print(1)
    exit()
i = 2
f: dict[int, int] = {}
while n > 1:
    while n % i == 0:
        n /= i
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    i += 1
    while not f2(i):
        i += 1
if len(f) == 1:
    print("是質數")
else:
    # print("*".join(str(k) if v == 1 else f"{k}^{v}" for k, v in f.items()))
    l: list[str] = []
    for i in f:
        if f[i] == 1:
            l.append(str(i))
        else:
            l.append(f"{i}^{f[i]}")
    print("*".join(l))
