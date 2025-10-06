#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> arr(n);
    for (int i = 0; i < n; i++) std::cin >> arr[i];

    long long moves = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            moves += (arr[i - 1] - arr[i]);
            arr[i] = arr[i - 1];
        }
    }

    std::cout << moves;
    return 0;
}

// Time Complexity: O(N)
// Space Complexity: O(1)