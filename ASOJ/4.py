n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    if i == 1:
        print(len(a) % 998244353, end=" ")
    elif sum(a) < i:
        print(0, end=" ")
    else:
        pass
