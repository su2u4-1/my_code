#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>
#include <limits>
#include <iterator>
#include <vector>
#include <algorithm>
#include <numeric> 

int main() {
    int m, n;
    std::cin >> m >> n;
    std::unordered_map<std::string, int> d;
    
    std::string temp;
    for (int i = 0; i < n; ++i) {
        std::cin >> temp;
        ++d[temp];
    }

    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Skip third line
    
    int mi = -1, mt = 1000000;
    std::string line;
    for (int i = 0; i < n; ++i) {
        std::getline(std::cin, line);
        std::istringstream iss(line);
        std::vector<std::string> tokens{std::istream_iterator<std::string>{iss}, std::istream_iterator<std::string>{}};
                                        
        int t = std::accumulate(tokens.begin(), tokens.end(), 0, [&d](int acc, const std::string& x){ return acc + d[x]; });
        
        if(t < mt) {
            mi = i + 1;
            mt = t;
        }
    }

    std::pair<std::string, int> max_elem = *std::max_element(d.begin(), d.end(), 
                                 [](const std::pair<std::string, int>& a, const std::pair<std::string, int>& b) -> bool {
                                     return a.second < b.second;
                                 });

    std::cout << max_elem.first << " " << mi << std::endl;
    
    return 0;
}