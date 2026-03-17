#include <iostream>
#include <string>
#include <algorithm>
 
int main() {
    std::string s;
    std::cin >> s;
    int maxC = 1;
    int curr = 1;
    for(int i = 0; i < s.length() - 1; i++) {
        if(s[i] == s[i+1]) {
            curr++;
        } else {
            maxC = std::max(maxC, curr);
            curr = 1;
        }
    }
    maxC = std::max(maxC, curr);
    if(maxC >= 7)
        std::cout << "YES";
    else
        std::cout << "NO";
    return 0;
}

// Time complexity: O(N)
// Space complexity: O(1)
