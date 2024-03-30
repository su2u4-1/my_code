n = int(input())
f = [0 for _ in range(n)]
tree = []
for j in range(n):
    a = input()
    if a != "0":
        a = a.split()
        for i in range(len(a)):
            a[i] = int(a[i])
            f[a[i] - 1] = j + 1
        tree.append(a[1:])
    else:
        tree.append([])
s = input()
l = f.index(0) + 1
print("f:", f)
for c in range(len(s)):
    if s[c] == "P":
        if f[l] == 0:
            print(l)
            exit()
        l = f[l - 1]
    elif s[c] == "C":
        i = int(s[c + 1])
        if len(tree[l - 1]) < i:
            print(l)
            exit()
        l = tree[l - 1][i - 1]
    elif s[c] == "R":
        if tree[f[l - 1]].index(l) - 1 in tree[f[l + 1]]:
            l = tree[f[l - 1]][tree[f[l - 1]].index(l) + 1]
        else:
            print(l)
            exit()
    elif s[c] == "L":
        if tree[f[l - 1]].index(l) - 1 in tree[f[l - 1]]:
            l = tree[f[l - 1]][tree[f[l - 1]].index(l) - 1]
        else:
            print(l)
            exit()
print(l)
