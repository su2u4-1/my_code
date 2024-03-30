n = int(input())
f = [0 for _ in range(n)]
tree = []
for j in range(n):
    a = input()
    if a != "0":
        a = a.split()
        for i in range(len(a)):
            a[i] = int(a[i])
            f[a[i]] = j + 1
        tree.append(a[1:])
    else:
        tree.append([])
s = input()
l = f.index(0)+1
for c in range(len(s)):
    if s[c] == "P":
        if f[l] == 0:
            print(l)
            exit()
        l = f[l]
    elif s[c] == "C":
        i = int(s[c + 1])
        if len(tree[l - 1]) < i:
            print(l)
            exit()
        l = tree[l - 1][i - 1]
    elif s[c] == "R":
        for j in range(len(tree)):
            if l in tree[j]:
                try:
                    l = tree[j][tree[j].index(l) + 1]
                except:
                    print(l)
                    exit()
                break
    elif s[c] == "L":
        for j in range(len(tree)):
            if l in tree[j]:
                try:
                    l = tree[j][tree[j].index(l) - 1]
                except:
                    print(l)
                    exit()
                break
print(l)
