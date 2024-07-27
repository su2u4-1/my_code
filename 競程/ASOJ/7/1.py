n = int(input())
m = {}
for _ in range(n):
    t = input().split()
    m[t[0]] = (t[1], t[2])
input()
s = input()
c = s[0]
for i in s[1:]:
    if m[c][1] == m[i][0]:
        print(1)
    else:
        print(0)
    c = i
