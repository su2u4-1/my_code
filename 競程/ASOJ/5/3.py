_, k, t = map(int, input().split())
p = 0
d: list[float] = []
for i in map(int, input().split()):
    d.append(i - p)
    p = i
d.append(t - p)
for _ in range(k):
    x = d.index(min(d))
    if x > 0:
        d0 = d[x] + d[x - 1]
    else:
        d0 = float("inf")
    if x < len(d) - 1:
        d1 = d[x + 1] + d[x]
    else:
        d1 = float("inf")
    if d0 > d1:
        d[x + 1] = d1
        d.pop(x)
    else:
        d.pop(x)
        d[x - 1] = d0
print(min(d))
