n = int(input())
w = [i + 1 for i in range(n)]
tree = []
for _ in range(n):
    a = input()
    if a != "0":
        a = a.split()
        for i in range(len(a)):
            a[i] = int(a[i])
            if i != 0 and a[i] in w:
                w.remove(a[i])
        tree.append(a[1:])
    else:
        tree.append([])
s = input()
l = w[0]
for c in range(len(s)):
    if s[c] == "P":
        if l == w[0]:
            print(l)
            exit()
        for j in range(len(tree)):
            if l in tree[j]:
                l = j + 1
                break
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
