n = int(input())
l = [str(i + 1) for i in range(n)]
for i in range(n):
    m = input()
    if m != "0":
        for j in m.split()[1:]:
            if l.index(j) > l.index(str(i + 1)):
                l.remove(j)
                l.insert(l.index(str(i + 1)), j)
print(" ".join(l))
