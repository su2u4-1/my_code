from random import randint as ri


class Point:
    def __init__(self, n, p):
        self.name = n
        self.p = p


def findPath(plist, s, e):
    path = [s]
    pb = []
    for _ in range(len(plist)):
        pb.append(False)
    pb[0] = True
    while len(path > 0) and path[-1] != e:
        pass


point_list = []
for i in range(10):
    t = set()
    for _ in range(ri(1, 5)):
        t.add(ri(0, 9))
    point_list.append(Point(i, t))

findPath(point_list, point_list[0], point_list[-1])
