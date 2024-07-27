n, k, c = map(int, input().split())
r = list(map(int, input().split()))
ans = 0
while True:
    ans += 1
    r[0] -= c
    a = r[0]
    b = r[0]
    for i in range(1, n):
        r[i] -= c
        a = max(r[i], a + r[i])
        if a > b:
            b = a
    if b < k:
        print(ans)
        break
