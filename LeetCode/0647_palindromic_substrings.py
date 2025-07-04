# 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[0]*N for _ in range(N)]
        ans = 0

        for i in range(N):
            dp[i][i] = 1
            ans += 1

        for i in range(N-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                ans += 1

        for length in range(3, N+1):
            for start in range(N - length + 1):
                end = start + length - 1
                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = 1
                    ans += 1
        return ans