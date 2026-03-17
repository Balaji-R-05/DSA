#include<iostream>
 
int main() {
    int N, res=0, p, q;
    std::cin >> N;
    while (N-- > 0) {
        std::cin >> p >> q;
        if (q-p >= 2) {
            res++;
        }
    }
    std::cout << res;
    return 0;
    
}

// Time Complexity: O(N)
// Space Complexity: O(1)