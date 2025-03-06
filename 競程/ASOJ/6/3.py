n, m = map(int, input().split())
c = map(int, input().split())
tree = [list(map(int, input().split()))[1:] for _ in range(n)]
x = list(map(int, input().split()))
f = [True for _ in range(n)]
nu: list[int] = []

nue: list[int] = [0]
t = 0
while True in f:
    ue = nue
    nue = []
    for j in ue:
        for i in tree[j]:
            if f[i - 1]:
                f[i - 1] = False
                t += x[i - 1]
                nue.append(i - 1)
    nu.append(t)

for i in c:
    j = -1
    for j, v in enumerate(nu):
        if v > i:
            print(j)
            break
    else:
        print(j + 1)
