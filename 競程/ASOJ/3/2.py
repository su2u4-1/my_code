d1 = [0, 1, 1, 0, -1, -1, -1, 1]
d2 = [1, 1, 0, -1, -1, 0, 1, -1]
n, m, r = map(int, input().split())
c: list[list[list[float]]] = []
for i in range(n):
    c.append([[j, 0] for j in map(int, input().split())])
for i in range(len(c)):
    for j in range(len(c[i])):
        t: list[float] = []
        for d in range(8):
            if 0 <= i + d1[d] < n and 0 <= j + d2[d] < m:
                t.append(c[i + d1[d]][j + d2[d]][0])
        for t1 in range(len(t)):
            for t2 in range(len(t)):
                if t1 == t2:
                    break
                if (t[t1] + t[t2]) % r == c[i][j][0]:
                    c[i][j][1] += 0.5
s = 0
for i in range(len(c)):
    for j in range(len(c[i])):
        for d in range(8):
            if 0 <= i + d1[d] < n and 0 <= j + d2[d] < m:
                if c[i][j][1] == c[i + d1[d]][j + d2[d]][1]:
                    s += 1
print(int(s / 2))
