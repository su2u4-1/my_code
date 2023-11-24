from random import randint as ri
import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_search(grid, start, end):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0, start))
    came_from = {}

    g_score = {pos: float("inf") for row in grid for pos in row}
    g_score[start] = 0

    f_score = {pos: float("inf") for row in grid for pos in row}
    f_score[start] = heuristic(start, end)

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current[0] + dx, current[1] + dy
            neighbor = (new_x, new_y)

            if (
                0 <= new_x < len(grid)
                and 0 <= new_y < len(grid[0])
                and grid[new_x][new_y] != 1
            ):
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                    if neighbor not in closed_set:
                        heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found


def show(maze):
    for x in maze:
        for y in x:
            if y == 1:
                print("1", end="")
            elif y == 0:
                print(" ", end="")
            elif y == 2:
                print("3", end="")
            else:
                print("N", end="")
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


size = 25
maze = generatemaze(size, size)
start = (1, 1)
end = (size - 2, size - 2)
path = astar_search(maze, start, end)
show(maze)
print()
for i in path:
    maze[i[0]][i[1]] = 2
show(maze)
