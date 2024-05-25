def f(i, j, k):
    for l in fri:
        if max(min(k - (abs(i - l[0]) + abs(j - l[1])) + ma[l[0]][l[1]], 50), 0) != l[2]:
            break
    else:
        return (i, j, k)
    for i in range(n):
        for j in range(m):
            for k in range(1, 51):
                for l in fri:
                    if max(min(k - (abs(i - l[0]) + abs(j - l[1])) + ma[l[0]][l[1]], 50), 0) != l[2]:
                        break
                else:
                    return (i, j, k)


n, m, N, Q = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]
mb = [[-1 for _ in range(m)] for _ in range(n)]
fri = []
for _ in range(N):
    x, y, mi = map(int, input().split())
    fri.append((x, y, mi))
i, j, k = f(*fri[0])
for _ in range(Q):
    x, y = map(int, input().split())
    print(max(min(k - (abs(x - i) + abs(y - j)) + ma[x][y], 50), 0))
