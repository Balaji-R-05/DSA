#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, L, R;
    cin >> N >> L >> R;

    int bestScore = -1;
    int bestID = -1;

    for (int i = 1; i <= N; i++) {
        int p;
        cin >> p;

        if (p >= L && p <= R) {
            if (p > bestScore) {
                bestScore = p;
                bestID = i;
            }
        }
    }

    cout << bestID << endl;
    return 0;
}

// Time Complexity: O(N)
// Space Complexity: O(1)