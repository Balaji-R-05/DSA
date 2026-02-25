#include<iostream>
 
int main() {
    int x;
    std::cin >> x;
    int res = 0;
    res += (x/5) + (x%5!=0 ? 1 : 0);
    std::cout << res;
    return 0;
}

// Time complexity: O(1)
// Space complexity: O(1)