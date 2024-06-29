_, m = map(int, input().split())
a = map(int, input().split())
k = [tuple(map(int, input().split())) for _ in range(int(input()))]
ans = 0
for i in a:
    for j in k:
        if j[0] <= i <= j[1]:
            ans += j[2]
            break
    else:
        ans += m
print(ans)
