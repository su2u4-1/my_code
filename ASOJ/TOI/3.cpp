#include <iostream>
#include <map>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>

int main() {
    // 創建一個字典對應
    std::map<std::string, int> d;
    for (int i = 1; i <= 52; ++i) {
        d[std::to_string(i)] = 0;
    }

    // 假設之前的第一行輸入已經被消耗掉了，因為是不必要的
    std::string line;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Skip first line
    getline(std::cin, line); // 現在讀取第二行
    std::istringstream iss(line);
    std::string number;
    
    // 統計每個數字出現的次數
    while (iss >> number) {
        d[number]++;
    }

    // 找到出現次數最多和最少的數字
    int ma = std::max_element(d.begin(), d.end(), 
        [](const std::pair<std::string, int>& p1, const std::pair<std::string, int>& p2) {
            return p1.second < p2.second; })->second;
    
    auto mi = std::min_element(d.begin(), d.end(), 
        [](const std::pair<std::string, int>& p1, const std::pair<std::string, int>& p2) {
            return p1.second < p2.second; })->second;
    
    int sum = std::accumulate(d.begin(), d.end(), 0, 
        [ma](int acc, const std::pair<std::string, int>& p) {
            return acc + (ma - p.second);
        });

    // 打印結果
    std::cout << mi << ' ' << sum << std::endl;
    
    return 0;
}