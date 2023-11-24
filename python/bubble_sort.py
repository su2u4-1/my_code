from random import randint as ri

a = []
for _ in range(1000):
    a.append(ri(0, 1000))

print(a)
for i in range(len(a)):
    for n in range(len(a) - i - 1):
        if a[n] > a[n + 1]:
            a[n], a[n + 1] = a[n + 1], a[n]
print(a)
