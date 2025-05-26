n = int(input())
m0: list[tuple[int, int, int, int]] = []
m1: list[tuple[int, int, int, int]] = []
m2: list[tuple[int, int, int, int]] = []
for i in range(1, n + 1):
    t, r, s = map(int, input().split())
    if t == 2:
        m0.append((i, t, r, s))
    elif t == 1:
        m1.append((i, t, r, s))
    elif t == 0:
        m2.append((i, t, r, s))
m0.sort(key=lambda x: x[3] * 1000 + x[2], reverse=True)
m1.sort(key=lambda x: x[3] * 1000 + x[2], reverse=True)
m2.sort(key=lambda x: x[3] * 1000 + x[2], reverse=True)
for i in m0:
    print(*i)
for i in m1:
    print(*i)
for i in m2:
    print(*i)
