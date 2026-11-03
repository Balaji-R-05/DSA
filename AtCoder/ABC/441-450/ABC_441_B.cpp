#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    string S, T;
    cin >> S >> T;

    int Q;
    cin >> Q;

    set<char> setS(S.begin(), S.end());
    set<char> setT(T.begin(), T.end());

    while (Q--) {
        string w;
        cin >> w;
        bool canS = true;
        bool canT = true;
        for (char c : w) {
            if (!setS.count(c)) canS = false;
            if (!setT.count(c)) canT = false;
        }

        if (canS && !canT) {
            cout << "Takahashi\n";
        } else if (!canS && canT) {
            cout << "Aoki\n";
        } else {
            cout << "Unknown\n";
        }
    }
    return 0;
}

// Time Complexity: O(Q * N)
// Space Complexity: O(N)