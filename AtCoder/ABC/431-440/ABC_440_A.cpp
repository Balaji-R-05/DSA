#include <iostream>

using namespace std;

int main() {
    int x,y;
    cin >> x >> y;
    while (y-- > 0) {
        x *= 2;
    }
    cout << x;
    return 0;
}

// Time Complexity: O(y)
// Space Complexity: O(1)
