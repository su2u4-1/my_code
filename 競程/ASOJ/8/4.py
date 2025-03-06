# def f(a, b):
#     mx = max(h[a], h[b])
#     for i in range(a + 1, b):
#         if h[i] > mx:
#             return False
#     return True


# n = int(input())
# h = tuple(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if j - i == 1:
#             ans += 1
#         elif j - i == 2:
#             if h[j - 1] < h[j] or h[j - 1] < h[i]:
#                 ans += 1
#         elif f(i, j):
#             ans += 1
# print(ans)


def f(l: int, r: int) -> int:
    if l < 0:
        l = 0
    if r > n:
        r = n
    if l >= r:
        return 0
    t = max(h[l:r], key=lambda x: x[1])
    return (t[0] - l) + (r - t[0] - 1) + f(l, t[0]) + f(t[0] + 1, r)


n = int(input())
h = tuple(enumerate(map(int, input().split())))
print(f(0, n))
