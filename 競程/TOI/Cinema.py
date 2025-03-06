t: list[tuple[str, str, int]] = []
for _ in range(int(input())):
    h, m = input().split()
    t.append((h, m, int(h) * 60 + int(m)))
h, m = input().split()
mt = (h, m, int(h) * 60 + int(m))
for i in t:
    if i[2] >= mt[2] + 20:
        print(i[0], i[1])
        break
else:
    print("Too Late")
