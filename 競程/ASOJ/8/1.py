n = int(input())
m = [[], [], []]
for i in range(1, n + 1):
    t, r, s = map(int, input().split())
    if t == 2:
        m[0].append((i, t, r, s))
    elif t == 1:
        m[1].append((i, t, r, s))
    elif t == 0:
        m[2].append((i, t, r, s))
m[0].sort(key=lambda x: x[3] * 1000 + x[2], reverse=True)
m[1].sort(key=lambda x: x[3] * 1000 + x[2], reverse=True)
m[2].sort(key=lambda x: x[3] * 1000 + x[2], reverse=True)
for i in m:
    for j in i:
        print(*j)
