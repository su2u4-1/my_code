# b938 MLE 50%
n, m = map(int, input().split())
pl = [i + 1 for i in range(n)]
for i in map(int, input().split()):
    if i in pl:
        ix = pl.index(i)
        if ix == len(pl) - 1:
            print("0u0 ...... ?")
        else:
            print(pl.pop(ix + 1))
    else:
        print("0u0 ...... ?")
