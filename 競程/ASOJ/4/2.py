md = ["ABCDEFGH", "IJKLMNOP", "QRSTUVWX", "YZabcdef", "ghijklmn", "opqrstuv", "wxyz0123", "456789+/"]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(int(input())):
    s, t, n = input().split()
    d = 1
    t = int(t)
    for i in range(len(md)):
        if s in md[i]:
            x = md[i].index(s)
            y = i
            break
    x, y = -1, -1
    for _ in range(int(n)):
        x += dx[t % 8] * d
        y += dy[t % 8] * d
        d += 1
        t += 1
    print(md[y % 8][x % 8])
