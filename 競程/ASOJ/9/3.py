bingo: dict[int, tuple[int, int]] = {}
ans: dict[int, str] = {}
n, m = map(int, input().split())
tree = [[False for _ in range(n + m)] for _ in range(n + m)]
win = [-1 for _ in range(n + m)]

for _ in range(n + m - 1):
    a, b = map(int, input().split())
    tree[a - 1][b - 1] = True
    tree[b - 1][a - 1] = True
for _ in range(m):
    t = int(input())
    t0, t1 = ["", "", ""], ["", "", ""]
    aa: list[str] = []
    for i in range(3):
        ta = input()
        aa.append(ta)
        for j in ta.split():
            t0[i] = t0[i] + j
            t1[2 - i] = j + t1[2 - i]
    ans[t - 1] = "\n".join(aa)
    bingo[t - 1] = (int("".join(t0)), int("".join(t1)))
    win[t - 1] = t - 1


def dfs(now: int, d: int):
    c: list[int] = []
    win[now] = -2
    for i in range(n + m):
        if tree[now][i]:
            if win[i] == -1:
                dfs(i, d + 1)
            if win[i] >= 0:
                c.append(win[i])
    win[now] = max(c, key=lambda x: bingo[x][d % 2])


dfs(0, 1)
winner = win[0]
print(winner + 1)
print(ans[winner])
