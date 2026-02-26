#include<iostream>
 
int main() {
    int num, n;
    std::cin >> num >> n;
    while (n-- > 0) {
        if (num%10 == 0) {
            num /= 10;
        } else {
            num -= 1;
        }
        
    }
    std::cout << num;
    return 0;
}

// Time complexity: O(N)
// Space complexity: O(1)