# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        temp = x
        res = 0
        while temp>0:
            res = res*10 + temp%10
            temp//=10
        return res == x
    
# Time complexity: O(log(x))
# Space complexity: O(1)

# Testcase
solution = Solution()

print(solution.isPalindrome(121)) # True
print(solution.isPalindrome(10)) # False
print(solution.isPalindrome(-121)) # False