n, m = map(int, input().split())
s = input()
h = list(map(int, input().split()))
t = list(map(int, input().split()))
ha: list[int] = []
ht: list[int] = []
ans = 0
for i in s:
    if i == "W":
        i = 0
    elif i == "M":
        i = 1
    else:  # L
        i = 2
    ha.append(h[i])
    ht.append(t[i])
    r: list[int] = []
    for j in range(len(ht)):
        ht[j] -= 1
        if ht[j] <= 0:
            r.append(j)
    r.sort(reverse=True)
    for j in r:
        ht.pop(j)
        ha.pop(j)
    if sum(ha) > m:
        ans += 1
print(ans)

# 數學家的解
n, m = map(int, input().split())
s = input()
a = dict(zip("WML", map(int, input().split())))
b = dict(zip("WML", map(int, input().split())))

xs = [0] * n
h = 0
cnt = 0
for t, c in enumerate(s):
    h += a[c]
    if t + b[c] - 1 < n:
        xs[t + b[c] - 1] += a[c]
    cnt += h > m
    h -= xs[t]

print(cnt)
