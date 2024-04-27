def f(t: list[list[int]]) -> int:
    # 計算競爭集群數量，這部分我不會寫，隨便寫了其中兩種狀況，希望可以拿到一些分
    s = 0
    fl = False
    for i in t:
        e = i.count(-1)
        if e == n:
            s += 1
        elif e == n - 1:
            for j in range(len(i)):
                if i[j] != -1:
                    break
            if t[j].count(-1) == n - 1:
                s += 1
            else:
                fl = True
        else:
            fl = True
    if fl:
        s += 1
    return s


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
for i in range(mc + 1, -1, -1):
    t = mo.copy()
    for j in t:
        for d in range(n):
            if j[d] >= i:
                j[d] = -1
    if f(t) >= k:
        break
print(i)

# 橘子寫的解
import sys

sys.setrecursionlimit(100000)
n, m = map(int, input().split())
con = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    con[a - 1].append((b - 1, c))
    con[b - 1].append((a - 1, c))
k = int(input())
l = 0
r = 10**9
while l < r:
    x = l + r + 1 >> 1
    vis = [0 for _ in range(n)]
    cur = 0

    def dfs(i):
        vis[i] = 1
        for j, v in con[i]:
            if v < x and not vis[j]:
                dfs(j)

    for i in range(n):
        if not vis[i]:
            cur += 1
            dfs(i)
    if cur >= k:
        l = x
    else:
        r = x - 1
print(l)
