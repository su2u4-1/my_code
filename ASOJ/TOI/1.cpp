#include <iostream>
#include <vector>
#include <utility>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::pair<std::pair<int, int>, int>> times;
    
    for(int i = 0; i < n; ++i) {
        std::string h, m;
        std::cin >> h >> m;
        times.emplace_back(std::make_pair(h, m), int(h) * 60 + int(m));
    }

    int target_h, target_m;
    std::cin >> target_h >> target_m;
    int target_time = target_h * 60 + target_m + 20;

    bool found = false;
    for (const auto &time : times) {
        if (time.second >= target_time) {
            std::cout << time.first.first << " " << time.first.second << std::endl;
            found = true;
            break;
        }
    }

    if (!found) {
        std::cout << "Too Late" << std::endl;
    }

    return 0;
}