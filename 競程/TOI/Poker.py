d: dict[str, int] = dict((str(i), 0) for i in range(1, 53))
input()
for i in input().split():
    d[i] += 1
ma = max(d.values())
print(min(d.values()), sum(map(lambda x: ma - x, d.values())))
