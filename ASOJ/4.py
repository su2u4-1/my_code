def mul(p, n, k):
    q = [0] * (n + 1)
    q[0] = p[0]
    for i in range(1, k + 1):
        q[i] = q[i - 1] + p[i]
    for i in range(k + 1, n + 1):
        q[i] = q[i - 1] + p[i] - p[i - k - 1]
    return q


n, m = map(int, input().split())
a = map(int, input().split())
p = [1] + [0] * n
for i in a:
    p = mul(p, n, i)
print(*p[1:])
