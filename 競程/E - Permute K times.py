# 範測3沒過 https://atcoder.jp/contests/abc367/tasks/abc367_e
n, k = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

if k == 0:
    print(*a)
else:
    p: list[list[int]] = []
    for i in x:
        tt: list[int] = []
        t = i
        tt.append(t)
        t = x[t - 1]
        # 問題出在這
        while t not in tt:
            tt.append(t)
            t = x[t - 1]
            if tt[-1] == tt[-2] == 7:
                exit()
        tt.reverse()
        p.append(tt)
    pp: list[int] = []
    for i in range(n):
        if len(p[i]) < k:
            pp[i] = a[p[i][k % len(p[i]) - 1] - 1]
        else:
            pp[i] = a[p[i][len(p[i]) % k - 1] - 1]
    print(*pp)
