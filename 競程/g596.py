# g596 NA 70%
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m, n, h = map(int, input().split())
s = [[0 for _ in range(n)] for _ in range(m)]
msu = 0
for i in range(h):
    r, c, t = map(int, input().split())
    if t == 0:
        s[r][c] = 1
        for d in range(4):
            x, y = r, c
            f = False
            t = []
            while True:
                x += dx[d]
                y += dy[d]
                if x < 0 or x >= m or y < 0 or y >= n:
                    break
                elif s[x][y] == 1:
                    f = t
                    break
                else:
                    t.append((x, y))
            if f:
                for i in f:
                    if s[i[0]][i[1]] != 2 and (d == 0 or d == 1):
                        s[i[0]][i[1]] += 2
                    elif s[i[0]][i[1]] != 3 and (d == 2 or d == 3):
                        s[i[0]][i[1]] += 3
    elif t == 1:
        s[r][c] = 0
        for d in range(4):
            x, y = r, c
            f = False
            t = []
            while True:
                x += dx[d]
                y += dy[d]
                if x < 0 or x >= m or y < 0 or y >= n:
                    break
                elif s[x][y] == 1:
                    f = t
                    break
                else:
                    t.append((x, y))
            if f:
                for i in f:
                    if d == 0 or d == 1:
                        s[i[0]][i[1]] -= 2
                    elif d == 2 or d == 3:
                        s[i[0]][i[1]] -= 3
    su = 0
    for i in s:
        for j in i:
            if j != 0:
                su += 1
    if su > msu:
        msu = su
print(msu)
print(su)
