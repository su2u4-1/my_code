n, m = map(int, input().split())
sd = [tuple(map(int, input().split())) for _ in range(n)]
p = list(map(int, input().split()))


def mi(bus: list[int], d: int) -> tuple[int, int]:
    if abs(bus[0] - d) < abs(bus[1] - d) and abs(bus[0] - d) < abs(bus[2] - d):
        return 0, abs(bus[0] - d)
    elif abs(bus[1] - d) < abs(bus[2] - d):
        return 1, abs(bus[1] - d)
    else:
        return 2, abs(bus[2] - d)


ans = 0
bus = [p[0], p[0], p[0]]

for i in sd:
    a, b = mi(bus, p[i[0] - 1])
    bus[a] = p[i[1] - 1]
    ans += b + abs(p[i[1] - 1] - p[i[0] - 1])

print(ans)
