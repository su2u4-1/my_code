n, k = map(int, input().split())
p = [(i[0], int(i[1:])) for i in input().split()]
l = 0
ans = 0
for j in range(len(p)):
    i = p[j]
    if i[1] >= 65 or i[1] <= 12 or (i[0] == "F" and 35 <= i[1] <= 45):
        ans += j - l
        l += 1
    if l >= k:
        break
print(ans)
