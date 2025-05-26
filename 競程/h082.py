# h082 NA 55%
p: list[list[int]] = []
n, m = map(int, input().split())
for i in map(int, input().split()):
    p.append([i])
for i, v in enumerate(map(int, input().split())):
    p[i].append(v)
    p[i].append(0)
sort = list(map(int, input().split()))
while len(sort) > 1:
    loser: list[int] = []
    winner: list[int] = []
    promotion: list[int] = []
    for i in range(0, len(sort), 2):
        if i == len(sort) - 1:
            promotion = [sort[i]]
            continue
        p1 = p[sort[i] - 1]
        p2 = p[sort[i + 1] - 1]
        if p1[0] * p1[1] >= p2[0] * p2[1]:
            p1[0] += (p2[0] * p2[1]) // (2 * p1[1])
            p1[1] += (p2[0] * p2[1]) // (2 * p1[0])
            winner.append(sort[i])
            p2[2] += 1
            if p2[2] < m:
                p2[0] += p2[0] // 2
                p2[1] += p2[1] // 2
                loser.append(sort[i + 1])
        else:
            p2[0] += (p1[0] * p1[1]) // (2 * p2[1])
            p2[1] += (p1[0] * p1[1]) // (2 * p2[0])
            winner.append(sort[i + 1])
            p1[2] += 1
            if p1[2] < m:
                p1[0] += p1[0] // 2
                p1[1] += p1[1] // 2
                loser.append(sort[i])
    sort = winner + promotion + loser
print(sort[0])
