#include <iostream>
#include <vector>
#include <string>
using namespace std;
 
int main() {
    
    
    int n, t;
    cin >> n >> t;
    
    vector<vector<char>> grid(n, vector<char>(n));
    
 
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            grid[i][j] = s[j];
        }
    }
    
 
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    
 
    for(int i=1;i<n+1;i++){
            for(int j=1;j<n+1;j++){
                if(grid[i-1][j-1] =='*'){
                    dp[i][j] = dp[i][j-1] + 1;
                }
                else{
                    dp[i][j] = dp[i][j-1];
                }
            }
        }
        for(int i=1;i<n+1;i++){
            for(int j=1;j<n+1;j++){
                dp[i][j] += dp[i-1][j];
            }
        }
    
    
    for (int i = 0; i < t; i++) {
        int y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;
        
        
        int result = dp[y2][x2] - dp[y1 - 1][x2] - dp[y2][x1 - 1] + dp[y1 - 1][x1 - 1];
        cout << result << "\n";
    }
    
    return 0;
}