# 15/69 WA https://tioj.ck.tp.edu.tw/problems/2340
n, m = map(int, input().split())
s, t = map(int, input().split())
su, sd = False, False
tu, td = False, False
f = [0 for _ in range(m)]
for i in range(n):
    ts = input()
    if ts[0] == "1":
        if i < s:
            su = True
        elif i > s:
            sd = True
    if ts[-1] == "1":
        if i < t:
            tu = True
        elif i > t:
            td = True

if su and sd:
    print("No")
elif tu and td:
    print("No")
elif su and td and not (m % 2 == 1):
    print("No")
elif sd and tu and not (m % 2 == 1):
    print("No")
elif su and tu and (m % 2 == 1):
    print("No")
elif sd and td and (m % 2 == 1):
    print("No")
else:
    print("Yes")
