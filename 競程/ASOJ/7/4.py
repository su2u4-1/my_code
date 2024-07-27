def f(a, b):
    if a == 0:
        return True
    elif a < 0 and (b < 0 or b == 0):
        return True
    elif a > 0 and (b > 0 or b == 0):
        return True
    return False


def f1():
    ans = 0
    c = 0
    for i in range(n - 1):
        if p0[i][0] < p1[i] and f(c, p0[i][1]):
            ans += p0[i][0]
            c = p0[i][1]
        else:
            ans += p1[i]
            c = 0
    return ans


def f2():
    ans = 0
    c = 0
    flag = False
    for i in range(n - 1):
        if flag:
            flag = False
            ans += p1[i]
            c = 0
        elif p0[i][0] < p1[i] and f(c, p0[i][1]):
            ans += p0[i][0]
            c = p0[i][1]
        else:
            flag = True
            ans += p1[i]
            c = 0
    return ans


n = int(input())
h = list(map(int, input().split()))
p0 = []
p1 = []
t = h[0]
for i in h[1:]:
    p0.append((abs(i - t), i - t))
    p1.append(max(i, t))
    t = i

print(min(f1(), f2()))

from typing import Callable, Any


class defaultdict(dict):
    def __init__(self, default: Callable, *args, **kwargs) -> None:
        self.default = default
        super().__init__(args, kwargs)

    def __getitem__(self, key: Any) -> int:
        if key not in self:
            super().__setitem__(key, self.default())
        return super().__getitem__(key)
