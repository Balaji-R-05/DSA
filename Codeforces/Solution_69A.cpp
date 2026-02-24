#include<iostream>
 
int main() {
    int N;
    std::cin >> N;
    int sumX = 0, sumY = 0, sumZ = 0;
    int x, y, z;
    while (N-- > 0) {
        std::cin >> x >> y >> z;
        sumX += x;
        sumY += y;
        sumZ += z;
    }
    if (sumX==0 && sumY==0 && sumZ==0) {
        std::cout << "YES";
    } else {
        std::cout << "NO";
    }
    return 0;
}

// Time complexity: O(N)
// Space complexity: O(1)