# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
    
solution = Solution()
print(solution.multiply(num1="3", num2="2"))

print(solution.multiply(num1 = "123", num2 = "456"))