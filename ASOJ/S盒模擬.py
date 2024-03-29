n, m = map(int, input().split())
S = [[], [], [], []]
for i in range(4):
    S[i] = input().split()
b = map(int, input().split())
for i in b:
    a = (i & 1) + ((i >> (n - 2)) & 2)
    c = i - a
    print(S, a, c)
    print(S[a][c], end=" ")
