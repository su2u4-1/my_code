n, m = map(int, input().split())
b = [[[j, 0] for j in map(int, input().split())] for _ in range(n)]

k, q = map(int, input().split())
con = [-1, -1, 0]
dp = 0
for _ in range(k + q):
    t = input()
    if t == "2":
        c = 0
        for i in range(n):
            for j in range(m):
                if con[0] - 1 == i and con[1] - 1 == j:
                    c += b[i][j][0] * b[i][j][1] * int(con[2] * (con[2] + 1) / 2)
                else:
                    c += b[i][j][0] * b[i][j][1]
        print(c - dp)
    else:
        _, x, y = map(int, t.split())
        if con[0] == x and con[1] == y:
            con[2] += 1
        else:
            con = [x, y, 1]
        if 0 < x <= n and 0 < y <= m:
            b[x - 1][y - 1][1] += 1
        else:
            con = [-1, -1, 0]
            if x <= 0:
                dp += 1 - x
            else:
                dp += x - n
            if y <= 0:
                dp += 1 - y
            else:
                dp += y - m
