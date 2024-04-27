#b938 MLE 50%
'''n, m = map(int, input().split())
pl = [i + 1 for i in range(n)]
for i in map(int, input().split()):
    if i in pl:
        ix = pl.index(i)
        if ix == len(pl) - 1:
            print("0u0 ...... ?")
        else:
            print(pl.pop(ix + 1))
    else:
        print("0u0 ...... ?")'''

#k731 WA 65%
'''x, y = 0, 0
d = 90
s = [0, 0, 0]
for _ in range(int(input())):
    px, py = map(int, input().split())
    if px > x:
        nd = 90
    elif px < x:
        nd = 270
    elif py > y:
        nd = 0
    elif py < y:
        nd = 180
    t = d - nd
    x, y = px, py
    d = nd
    if abs(t) == 180:
        s[2] += 1
    elif t < 0:
        s[1] += 1
    elif t > 0:
        s[0] += 1
print(*s)'''
