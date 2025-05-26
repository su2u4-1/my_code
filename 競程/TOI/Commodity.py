_, n = map(int, input().split())
d: dict[str, int] = {}
for i in input().split():
    d[i] = d.get(i, 0) + 1
input()
mi, mt = -1, 1000000
for i in range(n):
    t = sum(map(lambda x: d.get(x, 0), input().split()))
    if t < mt:
        mi, mt = i + 1, t
print(max(d, key=lambda x: d.get(x, 0)), mi)
