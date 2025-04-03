# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for i in s:
            if i == "R":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count
    
# Time complexity: O(n)
# Space complexity: O(1)