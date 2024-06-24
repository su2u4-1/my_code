from random import randint as ri

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

POS = tuple[int, int]
MAZE = list[list[int]]
ST = tuple[str, str, str, str, str, str]


def astar_search(grid: MAZE, start: POS, end: POS) -> list[POS]:
    open_list = []
    open_list.append((0, start))
    open_list.sort(key=lambda x: x[0])
    closed_list = []
    came_from = {}
    g_score = {pos: float("inf") for row in grid for pos in row}
    g_score[start] = 0
    f_score = {pos: float("inf") for row in grid for pos in row}
    f_score[start] = abs(start[0] - end[0]) + abs(start[1] - end[1])
    while open_list:
        current = open_list.pop(0)[1]
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        closed_list.append(current)
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current[0] + d[0], current[1] + d[1]
            neighbor = (new_x, new_y)
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                    if neighbor not in closed_list:
                        open_list.append((f_score[neighbor], neighbor))
                        open_list.sort(key=lambda x: x[0])


def show(maze: MAZE, symbol_table: ST = (" ", "1", "3", "N", "S", "E"), start: POS = (1, 1), end: POS = (1, 1)) -> None:
    for x in maze:
        for y in x:
            if start == (x, y):
                print(symbol_table[4], end="")
            elif end == (x, y):
                print(symbol_table[5], end="")
            elif y == 0:
                print(symbol_table[0], end="")
            elif y == 1:
                print(symbol_table[1], end="")
            elif y == 2:
                print(symbol_table[2], end="")
            else:
                print(symbol_table[3], end="")
        print()


def generatemaze(lx: int = 25, ly: int = 25) -> MAZE:
    s = ((lx - 1) / 2) * ((ly - 1) / 2)
    maze = [[(1 if x % 2 == 0 or y % 2 == 0 else 0) for y in range(ly)] for x in range(lx)]
    a, b = [], []
    a.append([1, 1])
    b.append([2, 1, 1, 0])
    b.append([1, 2, 0, 1])
    while len(a) < s:
        i = b[ri(0, len(b) - 1)]
        if [i[0] + i[2], i[1] + i[3]] not in a:
            a.append([i[0] + i[2], i[1] + i[3]])
            b.remove(i)
            maze[i[0]][i[1]] = 0
            for e in range(4):
                f = [i[0] + i[2] + DX[e], i[1] + i[3] + DY[e]]
                if 0 < f[0] < lx - 1 and 0 < f[1] < ly - 1:
                    if maze[f[0]][f[1]] == 1:
                        b.append([f[0], f[1], DX[e], DY[e]])
        else:
            b.remove(i)
        for x in range(lx):
            for y in range(ly):
                if a.count([x, y]) > 1:
                    a.remove([x, y])
    return maze


size = 25
maze = generatemaze(size, size)
start: POS = (1, 1)
end: POS = (size - 2, size - 2)
show(maze, ("  ", "牆", "路", "NN", "起", "終"), start, end)
path = astar_search(maze, start, end)
print()
for i in path:
    maze[i[0]][i[1]] = 2
show(maze, ("  ", "牆", "路", "NN", "起", "終"), start, end)
