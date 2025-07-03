// RE

#include <iostream>

using namespace std;

int DFS(int tree[][20001], int n, int a, int b, bool visited[]) {
    if (a == b) {
        return 0;
    }
    visited[a] = true;
    for (int i = 1; i <= n; i++) {
        if (tree[a][i] && !visited[i]) {
            int res = DFS(tree, n, i, b, visited);
            if (res != -1) {
                return res + 1;
            }
        }
    }
    return -1;
}

int main() {
    int n, q;
    cin >> n >> q;
    int tree[n + 1][20001] = {false};
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        tree[a][b] = true;
        tree[b][a] = true;
    }
    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        bool visited[] = {false};
        cout << DFS(tree, n, a, b, visited) << endl;
    }
    return 0;
}