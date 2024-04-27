n, m = map(int, input().split())
s = input()
h = list(map(int, input().split()))
t = list(map(int, input().split()))
ha = []
ht = []
ans = 0
for i in s:
    if i == "W":
        i = 0
    elif i == "M":
        i = 1
    elif i == "L":
        i = 2
    ha.append(h[i])
    ht.append(t[i])
    r = []
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