from random import choice, randint


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!.,0123456789 "


def f(a: float, b: float, c: float, ans: str) -> int:
    def score(s: str, ans: str) -> float:
        sc = 0
        for i in range(max(len(s), len(ans))):
            if i >= len(s) or i >= len(ans):
                sc -= a
            elif s[i] == ans[i]:
                sc += b
            else:
                sc -= c
        return sc

    now = "".join(choice(alphabet) for _ in range(randint(len(ans), len(ans) * 3)))

    s = score(now, ans)
    y = 0
    while now != ans:
        y += 1
        for _ in range(10):
            t = list(c for c in now)
            for j in range(len(now)):
                if randint(0, 99) < 5:
                    t[j] = choice(alphabet)
            if randint(0, 99) < 1 and len(t) > 0:
                t.pop(randint(0, len(t) - 1))
            if randint(0, 99) < 1:
                t.insert(randint(0, len(t)), choice(alphabet))
            t = "".join(t)
            ts = score(t, ans)
            if ts > s:
                now = t
                s = ts
        if y > 5000:
            break
    return y


class P:
    def __init__(self, a: float, b: float, c: float):
        a += randint(-20, 20) / 10
        b += randint(-20, 20) / 10
        c += randint(-20, 20) / 10
        self.a = a if a >= 1 else 1.0
        self.b = b if b >= 1 else 1.0
        self.c = c if c >= 1 else 1.0
        self.result = -1

    def dd(self) -> "P":
        return P(self.a, self.b, self.c)


log: list[str] = []
p_list: list[P] = [P(8.4, 5.7, 6.9) for _ in range(20)]

while True:
    ans = "".join(choice(alphabet) for _ in range(10))
    for i in p_list:
        i.result = f(i.a, i.b, i.c, ans) + f(i.a, i.b, i.c, ans) + f(i.a, i.b, i.c, ans)
        print(f"{i.a:.2} {i.b:.2} {i.c:.2} {ans}")
        print(i.result)
        with open("9_log.txt", "a", encoding="utf-8") as file:
            file.write(f"{i.result:04} <- {i.a:.2} {i.b:.2} {i.c:.2} {ans}\n")
    p_list.sort(key=lambda x: x.result)
    p_list = [p.dd() for p in p_list[:2] for _ in range(10)]
