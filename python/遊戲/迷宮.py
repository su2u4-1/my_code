import os, random


def astar_search(grid, start, end):
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

            if (
                0 <= new_x < len(grid)
                and 0 <= new_y < len(grid[0])
                and grid[new_x][new_y] != 1
            ):
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = (
                        g_score[neighbor]
                        + abs(neighbor[0] - end[0])
                        + abs(neighbor[1] - end[1])
                    )

                    if neighbor not in closed_list:
                        open_list.append((f_score[neighbor], neighbor))
                        open_list.sort(key=lambda x: x[0])

    return None


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
        i = b[random.randint(0, len(b) - 1)]
        if a.count([i[0] + i[2], i[1] + i[3]]) == 0:
            a.append([i[0] + i[2], i[1] + i[3]])
            b.remove(i)
            maze[i[0]][i[1]] = 0
            for e in range(4):
                f = [i[0] + i[2] + c[e], i[1] + i[3] + d[e]]
                if f[0] <= lx - 2 and f[0] >= 1 and f[1] <= ly - 2 and f[1] >= 1:
                    if maze[i[0] + i[2] + c[e]][i[1] + i[3] + d[e]] == 1:
                        b.append([i[0] + i[2] + c[e], i[1] + i[3] + d[e], c[e], d[e]])
        else:
            b.remove(i)
        for x in range(lx):
            for y in range(ly):
                if a.count([x, y]) > 1:
                    a.remove([x, y])
        if len(a) == ((lx - 1) / 2) * ((ly - 1) / 2):
            maze[1][1] = 2
            maze[lx - 2][ly - 2] = 3
            return maze


def main():
    os.system("cls")
    size = input("歡迎來走迷宮\n請輸入迷宮邊長(只接受大於5的奇數，填錯一率設為25):")
    c = size
    cheating = False
    try:
        size = int(size)
    except:
        size = 25
    if size % 2 == 0 or size < 5:
        size = 25
    maze = generatemaze(size, size)
    px, py = 1, 1

    while True:
        os.system("cls")
        print(f"歡迎來走迷宮\n請輸入迷宮邊長(只接受大於5的奇數，填錯一率設為25):{c}\n")
        for i in range(size):
            for j in range(size):
                if i == px and j == py:
                    print("人", end="")
                elif maze[i][j] == 1:
                    print("牆", end="")
                elif maze[i][j] == 0:
                    print("  ", end="")
                elif maze[i][j] == 2:
                    print("起", end="")
                elif maze[i][j] == 3:
                    print("終", end="")
                elif maze[i][j] == 4:
                    print("▉", end="")
            print()
        if maze[px][py] == 3:
            print("\n你贏了")
            break
        if cheating:
            print("\n你輸了")
            break
        walk = input("\n要往哪走(請用wasd):")
        if walk == "w" or walk == "W":
            if maze[px - 1][py] != 1:
                px -= 1
        elif walk == "a" or walk == "A":
            if maze[px][py - 1] != 1:
                py -= 1
        elif walk == "s" or walk == "S":
            if maze[px + 1][py] != 1:
                px += 1
        elif walk == "d" or walk == "D":
            if maze[px][py + 1] != 1:
                py += 1
        elif walk == "exit":
            print("\n離開遊戲")
            return
        elif walk == "help":
            ch = input("\n作弊不好喔，確定要作弊嗎(y/n):")
            if ch == "y" or ch == "Y" or ch == "yes" or ch == "Yes" or ch == "YES":
                path = astar_search(maze, (1, 1), (size - 2, size - 2))
                for i in path:
                    maze[i[0]][i[1]] = 4
                cheating = True
    ch = input("\n要再玩一次嗎(y/n):")
    if ch == "y" or ch == "Y" or ch == "yes" or ch == "Yes" or ch == "YES":
        main()
    else:
        return


if __name__ == "__main__":
    main()
