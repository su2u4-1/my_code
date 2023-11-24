from random import randint as ri


def show(maze):
    for x in maze:
        for y in x:
            if y == 1:
                print("1", end="")
            elif y == 0:
                print(" ", end="")
        print(end="\n")


def generatemaze(lx, ly):
    maze = []
    for x in range(lx):
        a = []
        for y in range(ly):
            if x % 2 == 0 or y % 2 == 0:
                a.append(1)
            else:
                a.append(0)
        maze.append(a)
    a, b = [], []
    a.append([1, 1])
    b.append([2, 1, 1, 0])
    b.append([1, 2, 0, 1])
    c = [0, 1, 0, -1]
    d = [1, 0, -1, 0]
    while True:
        i = b[ri(0, len(b) - 1)]
        if a.count([i[0] + i[2], i[1] + i[3]]) == 0:
            a.append([i[0] + i[2], i[1] + i[3]])
            b.remove(i)
            maze[i[0]][i[1]] = 0
            for e in range(4):
                f = [i[0] + i[2] + c[e], i[1] + i[3] + d[e]]
                if f[0] <= lx - 2 and f[0] >= 1 and f[1] <= ly - 2 and f[1] >= 1:
                    if maze[i[0] + i[2] + c[e]][i[1] + i[3] + d[e]] == 1:
                        b.append([i[0] + i[2] + c[e], i[1] + i[3] + d[e], c[e], d[e]])
        for x in range(lx):
            for y in range(ly):
                if a.count([x, y]) > 1:
                    a.remove([x, y])
        if len(a) == ((lx - 1) / 2) * ((ly - 1) / 2):
            return maze


maze = generatemaze(25, 25)
show(maze)
