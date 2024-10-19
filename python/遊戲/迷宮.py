from random import randint as ri
from os import system
from time import sleep
import keyboard

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]
Y = ("y", "Y", "yes", "Yes", "YES")
POS = tuple[int, int]
MAZE = list[list[int]]


def astar_search(grid: MAZE, start: POS, end: POS) -> list[POS]:
    open_list: list[tuple[int, POS]] = [(0, start)]
    open_list.sort(reverse=True, key=lambda x: x[0])
    closed_list: set[POS] = set()
    came_from: dict[POS, POS] = {}
    g_score: dict[POS, int] = {}
    g_score[start] = 0
    f_score: dict[POS, int] = {}
    f_score[start] = abs(start[0] - end[0]) + abs(start[1] - end[1])
    while open_list:
        current = open_list.pop()[1]
        if current == end:
            path: list[POS] = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        closed_list.add(current)
        for d in range(4):
            new_x, new_y = current[0] + DX[d], current[1] + DY[d]
            neighbor = (new_x, new_y)
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                    if neighbor not in closed_list:
                        open_list.append((f_score[neighbor], neighbor))
                        open_list.sort(reverse=True, key=lambda x: x[0])
    return []


def generatemaze(lx: int = 25, ly: int = 25) -> MAZE:
    s = ((lx - 1) / 2) * ((ly - 1) / 2)
    maze = [[(1 if x % 2 == 0 or y % 2 == 0 else 0) for y in range(ly)] for x in range(lx)]
    a: set[tuple[int, int]] = set(((1, 1),))
    b: list[tuple[int, int, int, int]] = [(2, 1, 1, 0), (1, 2, 0, 1)]
    while len(a) < s:
        i = b.pop(ri(0, len(b) - 1))
        if (i[0] + i[2], i[1] + i[3]) not in a:
            a.add((i[0] + i[2], i[1] + i[3]))
            maze[i[0]][i[1]] = 0
            for e in range(4):
                f = (i[0] + i[2] + DX[e], i[1] + i[3] + DY[e])
                if 0 < f[0] < lx - 1 and 0 < f[1] < ly - 1 and maze[f[0]][f[1]] == 1:
                    b.append((f[0], f[1], DX[e], DY[e]))
    maze[1][1] = 2
    maze[lx - 2][ly - 2] = 3
    return maze


def showmaze(maze: MAZE, player: POS, size: int, f: bool = True) -> None:
    system("cls")
    print("按wasd移動，按e離開，按h作弊")
    if f:
        for i in range(0, size):
            for j in range(0, size):
                if (i, j) == player:
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
                    print("11", end="")
            print()
    else:
        for i in range(max(player[0] - 10, 0), min(player[0] + 10, size)):
            for j in range(max(player[1] - 10, 0), min(player[1] + 10, size)):
                if (i, j) == player:
                    print("人", end="")
                elif maze[i][j] == 1:
                    print("牆", end="")
                elif maze[i][j] == 0:
                    print("  ", end="")
                elif maze[i][j] == 2:
                    print("起", end="")
                elif maze[i][j] == 3:
                    print("終", end="")
            print()


def key_pressed() -> str:
    key = None
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
        elif event.event_type == keyboard.KEY_UP and key is not None:
            return key


def flush_input():
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)  # type: ignore


def main() -> None:
    size = input("歡迎來走迷宮\n請輸入迷宮邊長(只接受大於5的奇數，填錯一率設為25):")
    try:
        size = int(size)
    except:
        size = 25
    if size % 2 == 0 or size < 5:
        size = 25
    maze = generatemaze(size, size)
    px, py = 1, 1

    showmaze(maze, (px, py), size)
    while True:
        if maze[px][py] == 3:
            print("\n你贏了")
            return
        key = key_pressed()
        if key == "w":
            if maze[px - 1][py] != 1:
                px -= 1
                showmaze(maze, (px, py), size)
        elif key == "a":
            if maze[px][py - 1] != 1:
                py -= 1
                showmaze(maze, (px, py), size)
        elif key == "s":
            if maze[px + 1][py] != 1:
                px += 1
                showmaze(maze, (px, py), size)
        elif key == "d":
            if maze[px][py + 1] != 1:
                py += 1
                showmaze(maze, (px, py), size)
        elif key == "e":
            print("\n關閉此局")
            return
        elif key == "h":
            flush_input()
            if input("\n作弊不好喔，確定要作弊嗎(y/n):") in Y:
                for i in astar_search(maze, (1, 1), (size - 2, size - 2)):
                    maze[i[0]][i[1]] = 4
                showmaze(maze, (px, py), size, True)
                print("\n你輸了")
                return
        sleep(0.1)


if __name__ == "__main__":
    while True:
        main()
        flush_input()
        if input("\n要再玩一次嗎(y/n):") not in Y:
            print("離開遊戲")
            break
