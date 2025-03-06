def f(t: list[list[int]]) -> int:
    fl = [True for _ in range(n)]
    an = 0
    for h in range(n):
        if fl[h]:
            a = [h]
            an += 1
            fl[h] = False
            while len(a) > 0:
                i = a.pop()
                for j, v in enumerate(t[i]):
                    if v >= 0 and fl[j]:
                        a.append(j)
                        fl[j] = False
    return an


n, m = map(int, input().split())
mo = [[-1 for _ in range(n)] for _ in range(n)]
mc = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    mo[a - 1][b - 1] = c
    mo[b - 1][a - 1] = c
    if c > mc:
        mc = c
k = int(input())
i = -1
for i in range(mc + 1, -1, -1):
    t = mo.copy()
    for j in t:
        for d in range(n):
            if j[d] >= i:
                j[d] = -1
    if f(t) >= k:
        break
print(i)
