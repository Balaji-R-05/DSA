# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if len(s) == 0 :
            return True
        if len(t) == 0 :
            return False
        while(i<len(s) and j<len(t)):
            if t[j]==s[i]:
                i+=1
            j+=1
        
        return i==len(s)
    
Solution = Solution()
print(Solution.isSubsequence("abc","ahbgdc"))
print(Solution.isSubsequence("axc","ahbgdc"))