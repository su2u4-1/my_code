n = int(input())
wire = [[False for _ in range(n)] for _ in range(n)]
flag = [True for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    wire[a - 1][b - 1] = True
    wire[b - 1][a - 1] = True
cost = list(map(int, input().split()))

ans = 0
while True in flag:
    t: list[int] = [-2147483648, -1]
    for i in range(n):
        if flag[i]:
            t0 = -cost[i] * 2
            for j in range(n):
                if wire[i][j] and flag[j]:
                    t0 += cost[j]
            if t0 > t[0]:
                t[0] = t0
                t[1] = i
    ans += cost[t[1]]
    flag[t[1]] = False
    for i in range(n):
        if wire[t[1]][i]:
            flag[i] = False
print(ans)
