#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string s;
    cin >> s;
    int lcount = 0, ucount = 0;

    for(char c : s) {
        if(islower(c))
            lcount++;
        else if(isupper(c))
            ucount++;
    }

    if(lcount >= ucount) {
        for(int i = 0; i < s.length(); i++)
            s[i] = tolower(s[i]);
    }
    else {
        for(int i = 0; i < s.length(); i++)
            s[i] = toupper(s[i]);
    }
    cout << s;
    return 0;
}

// Time complexity: O(N)
// Space complexity: O(1).