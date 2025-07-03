// https://vjudge.net/contest/707812#problem/A
// TLE

#include <iostream>

using namespace std;

int gcd(int a, int b) {
    while (a %= b)
        swap(a, b);
    return a;
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int G, L;
        cin >> G >> L;
        bool notfind = true;
        for (int j = G; j <= L; j += G) {
            for (int k = j; k <= L; k += G) {
                if (gcd(j, k) == G && lcm(j, k) == L) {
                    cout << j << " " << k << endl;
                    notfind = false;
                    break;
                }
            }
            if (!notfind) {
                break;
            }
        }
        if (notfind) {
            cout << -1 << endl;
        }
    }
}