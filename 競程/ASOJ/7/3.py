def f(t: int) -> int:
    a = R[0] - (C * t)
    b = R[0] - (C * t)
    for i in range(1, N):
        a = max(R[i] - (C * t), a + R[i] - (C * t))
        if a >= K:
            return K
        if a > b:
            b = a
    return b


N, K, C = map(int, input().split())
R = tuple(map(int, input().split()))
l, r = 0, max(R)
while l < r:
    m = (l + r) // 2
    if f(m) < K:
        r = m
    else:
        l = m + 1
print(l)
