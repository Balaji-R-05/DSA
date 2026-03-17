#include<iostream>
#include<string>
 
int main() {
    std::string s, t;
    std::cin >> s >> t;
    if (s.length() != t.length()) {
        std::cout << "NO";
        return 0;
    }
    int n = s.length();
    for(int i=0; i<n; i++) {
        if (s[i] != t[n-1-i]) {
            std::cout << "NO";
            return 0;
        }
    }
    std::cout << "YES";
    return 0;
}


// Time complexity: O(N)
// Space complexity: O(1)



// #include <iostream>
// #include <string>
// #include <algorithm>

// int main() {
//     std::string s,t;
//     std::cin>>s>>t;
//     reverse(s.begin(),s.end());
//     std::cout<<(s==t?"YES":"NO");
// }

// Time complexity: O(N)
// Space complexity: O(1)