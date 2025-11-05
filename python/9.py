from random import choice, randint


def score(s: str, ans: str) -> int:
    sc = 0
    for i in range(max(len(s), len(ans))):
        if i >= len(s) or i >= len(ans):
            sc -= 1
        elif s[i] == ans[i]:
            sc += 1
        else:
            sc -= 1
    return sc


def output(s: str) -> None:
    print(s)
    log.append(s)


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!.,0123456789 "
ans = "Yzu 1141519"
now = "".join(choice(alphabet) for _ in range(randint(max(len(ans) + 100, 0), len(ans) + 100)))

log: list[str] = []

s = score(now, ans)
y = 0
while now != ans:
    y += 1
    output(f"year: {y}")
    for i in range(max(s * 10, 10)):
        t = list(c for c in now)
        for j in range(len(now)):
            if randint(0, 99) < 5:
                t[j] = choice(alphabet)
        if randint(0, 99) < 1:
            t.pop(randint(0, len(t) - 1))
        if randint(0, 99) < 1:
            t.insert(randint(0, len(t)), choice(alphabet))
        t = "".join(t)
        ts = score(t, ans)
        if t != now:
            output(f'score: {ts:4}, len: {len(t):4}, str: "{t}"')
        if ts > s:
            now = t
            s = ts

with open("9_log.txt", "w") as f:
    f.write("\n".join(log))

output(f"Answer found in year {y}: {now}")
