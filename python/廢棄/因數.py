a = int(input())
for i in range(1, round(a / 2) + 1):
    if a % i == 0:
        if i > a / i:
            break
        print(i, int(a / i))
