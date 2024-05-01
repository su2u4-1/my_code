ps, ns = 0, 0
pt, nt = 0, 0
for _ in range(int(input())):
    p, n = map(int, input().split())
    if p > n:
        pt += 1
    else:
        nt += 1
    ps += p
    ns += n
if pt == nt:
    if ps > ns:
        w = "Positive side"
    else:
        w = "Negative side"
else:
    if pt > nt:
        w = "Positive side"
    else:
        w = "Negative side"
print(w)
print(pt, nt)
print(ps, ns)
