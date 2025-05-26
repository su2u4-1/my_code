# from random import randint

# def f(m):
#     t = list(zip(*m))
#     t.reverse()
#     return t

# def ff(n, k, t):
#     m = []
#     for _ in range(4):
#         m.append(t)
#         t = f(t)
#     a = 0
#     d = 0
#     for i, ki in enumerate(k):
#         a += m[d][i // n][i % n]
#         if ki == "0":
#             d += 1
#             if d >= 4:
#                 d -= 4
#         else:
#             d -= 1
#             if d < 0:
#                 d += 4
#     a += m[d][-1][-1]
#     print(a)

# for _ in range(100):
#     for s in range(2, 101):
#         print(s, end=" ans: ")
#         n = s
#         k = [randint(0, 1) for _ in range(s*s-1)]
#         t = [[randint(1, 100) for _ in range(s)] for _ in range(s)]
#         ff(n, k, t)


def f(m: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    t = list(zip(*m))
    t.reverse()
    return t


n = int(input())
k = input().split()
t = [tuple(map(int, input().split())) for _ in range(n)]

m: list[list[tuple[int, ...]]] = []
for _ in range(4):
    m.append(t)
    t = f(t)
a = 0
d = 0
for i, ki in enumerate(k):
    a += m[d][i // n][i % n]
    if ki == "0":
        d += 1
        if d >= 4:
            d -= 4
    else:
        d -= 1
        if d < 0:
            d += 4
a += m[d][-1][-1]
print(a)
