#include <iostream>

using namespace std;

int main() {
    int P, Q, X, Y;
    cin >> P >> Q;
    cin >> X >> Y;
    if (P <= X && X <= P + 99 && Q <= Y && Y <= Q + 99) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}

// Time Complexity: O(1)
// Space Complexity: O(1)