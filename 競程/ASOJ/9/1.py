d = {"A+": 43, "A": 40, "A-": 37, "B+": 33, "B": 30, "B-": 27, "C+": 23, "C": 20, "C-": 17, "D": 10, "E": 0, "X": 0}

n = int(input())
dc: dict[str, float] = {}
for _ in range(n):
    x, cp = input().split()
    dc[x] = d[cp]

print(sum(dc.values()) / 10)
