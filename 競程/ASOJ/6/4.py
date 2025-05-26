n, k = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]


def f1() -> int:
    f = [True for _ in range(n)]
    c, p = 0, 0
    count = 0

    while True:
        mx = ((0, -1), -1)
        for i, v in enumerate(a):
            if f[i] and v[0] > mx[0][0]:
                mx = (v, i)
        if mx[1] == -1:
            break
        f[mx[1]] = False
        c += mx[0][0]
        p += mx[0][1]
        count += 1
        if count >= k:
            break

    for _ in range(k - count):
        mx = ((-1, 0), -1)
        for i, v in enumerate(a):
            if f[i] and v[1] > mx[0][1]:
                mx = (v, i)
        f[mx[1]] = False
        if c + mx[0][0] >= 0:
            c += mx[0][0]
            p += mx[0][1]
        else:
            break
    return p


def f2() -> int:
    f = [True for _ in range(n)]

    mx = ((0, -1), -1)
    for i, v in enumerate(a):
        if v[0] > mx[0][0]:
            mx = (v, i)
    f[mx[1]] = False
    c = mx[0][0]
    p = mx[0][1]

    for _ in range(k - 1):
        mx = ((-1, 0), -1)
        for i, v in enumerate(a):
            if f[i] and v[1] > mx[0][1]:
                mx = (v, i)
        f[mx[1]] = False
        if c + mx[0][0] >= 0:
            c += mx[0][0]
            p += mx[0][1]
        else:
            break
    return p


print(max(f1(), f2()))
