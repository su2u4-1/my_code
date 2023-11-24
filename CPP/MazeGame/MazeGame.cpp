#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <unordered_map>
#include <limits>
#include <string>

namespace std
{
    template <>
    struct hash<std::tuple<int, int>>
    {
        size_t operator()(const std::tuple<int, int> &t) const
        {
            return std::hash<int>()(std::get<0>(t)) ^ std::hash<int>()(std::get<1>(t));
        }
    };
}

std::vector<std::tuple<int, int>> astar_search(std::vector<std::vector<int>> grid, std::tuple<int, int> start, std::tuple<int, int> end)
{
    std::vector<std::tuple<double, std::tuple<int, int>>> open_list;
    open_list.push_back({0, start});
    std::sort(open_list.begin(), open_list.end(), [](const auto &a, const auto &b)
              { return std::get<0>(a) < std::get<0>(b); });
    std::vector<std::tuple<int, int>> closed_list;
    std::unordered_map<std::tuple<int, int>, std::tuple<int, int>> came_from;
    std::unordered_map<std::tuple<int, int>, double> g_score;
    std::unordered_map<std::tuple<int, int>, double> f_score;
    for (const auto &row : grid)
    {
        for (const auto &pos : row)
        {
            g_score[std::make_tuple(pos, pos)] = std::numeric_limits<double>::infinity();
            f_score[std::make_tuple(pos, pos)] = std::numeric_limits<double>::infinity();
        }
    }
    g_score[start] = 0.0;
    f_score[start] = abs(std::get<0>(start) - std::get<0>(end)) + abs(std::get<1>(start) - std::get<1>(end));
    while (open_list.size() > 0)
    {
        std::tuple<int, int> current = std::get<1>(open_list[0]);
        open_list.erase(open_list.begin());
        if (current == end)
        {
            std::vector<std::tuple<int, int>> path;
            while (came_from.find(current) != came_from.end())
            {
                path.push_back(current);
                current = came_from[current];
            }
            path.push_back(start);
            std::reverse(path.begin(), path.end());
            return path;
        }
        closed_list.push_back(current);
        std::vector<std::tuple<int, int>> d = {std::make_tuple(0, 1), std::make_tuple(0, -1), std::make_tuple(1, 0), std::make_tuple(-1, 0)};
        for (int i = 0; i < 4; i++)
        {
            int new_x = std::get<0>(current) + std::get<0>(d[i]);
            int new_y = std::get<1>(current) + std::get<1>(d[i]);
            std::tuple<int, int> neighbor = std::make_tuple(new_x, new_y);
            if (0 <= new_x && new_x < grid.size() && 0 <= new_y && new_y < grid[0].size() && grid[new_x][new_y] != 1)
            {
                double tentative_g_score = g_score[current] + 1;
                double n = std::numeric_limits<double>::infinity();
                if (g_score.find(neighbor) != g_score.end())
                {
                    n = g_score[neighbor];
                }
                if (tentative_g_score < n)
                {
                    came_from[neighbor] = current;
                    g_score[neighbor] = tentative_g_score;
                    f_score[neighbor] = g_score[neighbor] + abs(std::get<0>(neighbor) - std::get<0>(end)) + abs(std::get<1>(neighbor) - std::get<1>(end));
                    if (std::find(closed_list.begin(), closed_list.end(), neighbor) == closed_list.end())
                    {
                        open_list.push_back(std::make_tuple(f_score[neighbor], neighbor));
                        std::sort(open_list.begin(), open_list.end(), [](const auto &a, const auto &b)
                                  { return std::get<0>(a) < std::get<0>(b); });
                    }
                }
            }
        }
    }
    std::vector<std::tuple<int, int>> path;
    return path;
}

std::vector<std::vector<int>> generatemaze(int size)
{
    std::vector<std::vector<int>> maze(size, std::vector<int>(size, 0));
    for (int x = 0; x < size; x++)
    {
        for (int y = 0; y < size; y++)
        {
            if (x % 2 == 0 || y % 2 == 0)
            {
                maze[x][y] = 1;
            }
            else
            {
                maze[x][y] = 0;
            }
        }
    }
    std::vector<std::vector<int>> a;
    std::vector<std::vector<int>> b;
    a.push_back({1, 1});
    b.push_back({2, 1, 1, 0});
    b.push_back({1, 2, 0, 1});
    int c[4] = {0, 1, 0, -1};
    int d[4] = {1, 0, -1, 0};
    srand(time(NULL));
    while (true)
    {
        int x = rand() % (b.size());
        std::vector<int> i = b[x];
        if (std::count(a.begin(), a.end(), std::vector<int>{i[0] + i[2], i[1] + i[3]}) == 0)
        {
            a.push_back({i[0] + i[2], i[1] + i[3]});
            b.erase(b.begin() + x);
            maze[i[0]][i[1]] = 0;
            for (int e = 0; e < 4; e++)
            {
                int f[2] = {i[0] + i[2] + c[e], i[1] + i[3] + d[e]};
                if (f[0] <= size - 2 && f[0] >= 1 && f[1] <= size - 2 && f[1] >= 1)
                {
                    if (maze[i[0] + i[2] + c[e]][i[1] + i[3] + d[e]] == 1)
                    {
                        b.push_back({i[0] + i[2] + c[e], i[1] + i[3] + d[e], c[e], d[e]});
                    }
                }
            }
        }
        else
        {
            b.erase(std::remove(b.begin(), b.end(), i), b.end());
        }
        for (int x = 0; x < size; x++)
        {
            for (int y = 0; y < size; y++)
            {
                if (std::count(a.begin(), a.end(), std::vector<int>{x, y}) > 1)
                {
                    a.erase(std::remove(a.begin(), a.end(), std::vector<int>{x, y}), a.end());
                }
            }
        }
        if (a.size() == ((size - 1) / 2) * ((size - 1) / 2))
        {
            maze[1][1] = 2;
            maze[size - 2][size - 2] = 3;
            return maze;
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    system("clear");
    std::string c;
    int maze_size = 25;
    int px = 1;
    int py = 1;
    bool cheating = false;
    std::string walk;
    std::cout << "歡迎來走迷宮\n請輸入迷宮邊長(只接受大於5的奇數，填錯一率設為25):";
    std::cin >> c;
    try
    {
        maze_size = std::stoi(c);
    }
    catch (...)
    {
        maze_size = 25;
        c = "25";
    }
    if (maze_size % 2 == 0 || maze_size < 5)
    {
        maze_size = 25;
        c = "25";
    }
    std::vector<std::vector<int>> maze = generatemaze(maze_size);
    while (true)
    {
        system("clear");
        std::cout << "歡迎來走迷宮\n請輸入迷宮邊長(只接受大於5的奇數，填錯一率設為25):" << c << std::endl
                  << std::endl;
        for (int i = 0; i < maze_size; i++)
        {
            for (int j = 0; j < maze_size; j++)
            {
                if (i == px && j == py)
                {
                    std::cout << "人";
                }
                else if (maze[i][j] == 1)
                {
                    std::cout << "牆";
                }
                else if (maze[i][j] == 0)
                {
                    std::cout << "  ";
                }
                else if (maze[i][j] == 2)
                {
                    std::cout << "起";
                }
                else if (maze[i][j] == 3)
                {
                    std::cout << "終";
                }
                else if (maze[i][j] == 4)
                {
                    std::cout << "▉";
                }
            }
            std::cout << std::endl;
        }
        if (maze[px][py] == 3)
        {
            std::cout << "\n你贏了" << std::endl;
            break;
        }
        if (cheating)
        {
            std::cout << "\n你輸了" << std::endl;
            break;
        }
        std::cout << "\n要往哪走(請用wasd):";
        std::cin >> walk;
        if (walk == "w" || walk == "W")
        {
            if (maze[px - 1][py] != 1)
            {
                px -= 1;
            }
        }
        else if (walk == "a" || walk == "A")
        {
            if (maze[px][py - 1] != 1)
            {
                py -= 1;
            }
        }
        else if (walk == "s" || walk == "S")
        {
            if (maze[px + 1][py] != 1)
            {
                px += 1;
            }
        }
        else if (walk == "d" || walk == "D")
        {
            if (maze[px][py + 1] != 1)
            {
                py += 1;
            }
        }
        else if (walk == "exit")
        {
            std::cout << "\n離開遊戲" << std::endl;
            return 0;
        }
        else if (walk == "help")
        {
            std::string ch;
            std::cout << "\n作弊不好喔，確定要作弊嗎(y/n):";
            std::cin >> ch;
            if (ch == "y" || ch == "Y" || ch == "yes" || ch == "Yes" || ch == "YES")
            {
                std::vector<std::tuple<int, int>> path;
                path = astar_search(maze, {1, 1}, {maze_size - 2, maze_size - 2});
                for (int i = 0; i < path.size(); i++)
                {
                    maze[std::get<0>(path[i])][std::get<1>(path[i])] = 4;
                }
                cheating = true;
            }
        }
    }
    std::string ch;
    std::cout << "\n要再玩一次嗎(y/n):";
    std::cin >> ch;
    if (ch == "y" || ch == "Y" || ch == "yes" || ch == "Yes" || ch == "YES")
    {
        main();
    }
    else
    {
        return 0;
    }
}
