n, m = map(int, input().split())
t, k, r = map(int, input().split())
s = input()
h = [list(map(int, input().split())) for _ in range(n)]
z = [list(map(int, input().split())) for _ in range(n)]
net = [[[0, 0, 0, 0, 0, 1] for _ in range(m)] for _ in range(n)]

for i in range(t):
    for x in range(n):
        for y in range(m):
            if s[i] == "S":
                if net[x][y][4] == 0:
                    net[x][y][4] = 2
                else:
                    net[x][y][4] = 0
            if net[x][y][5] == 1:
                net[x][y][net[x][y][4]] += h[x][y]
                net[x][y][net[x][y][4] + 1] = net[x][y][net[x][y][4]] // k
                if net[x][y][1] >= r and net[x][y][3] >= r:
                    net[x][y][5] = 0
            h[x][y] += z[x][y]
            if h[x][y] < 0:
                h[x][y] = 0
ans1 = 1
ans2 = 0
for x in range(n):
    for y in range(m):
        if net[x][y][1] > (2 * r):
            ans2 += 1
        if net[x][y][3] > (2 * r):
            ans2 += 1
        if ans1 and net[x][y][5] == 1:
            ans1 = 0
print(ans1, ans2)
