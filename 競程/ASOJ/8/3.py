def f(a: int) -> bool:
    m = [a - 2]
    i = n - 2
    while i > 0:
        if len(m) <= 0:
            return False
        t = m[-1]
        if t % 2 == 0 and t // 2 - 1 >= k:
            m[-1] = t // 2 - 1
            m.append(t // 2)
        elif t % 2 == 1 and t // 2 >= k:
            m[-1] = t // 2
            m.append(t // 2)
        else:
            i += 1
            m.pop()
        m.sort()
        i -= 1
    return True


n, k = map(int, input().split())
if k == 1:
    print(n * 2 - 1)
else:
    l, r = 3, 10000000000
    while l < r:
        m = (l + r) // 2
        if f(m):
            r = m
        else:
            l = m + 1
    print(l)
