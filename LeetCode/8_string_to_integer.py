# 

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:  # If the string is empty after stripping
            return 0

        isNegative = False
        index = 0

        # Check for sign
        if s[index] == '-':
            isNegative = True
            index += 1
        elif s[index] == '+':
            index += 1

        # Convert digits to an integer
        ns = 0
        while index < len(s) and s[index].isdigit():
            ns = ns * 10 + int(s[index])
            index += 1

        # Apply sign
        if isNegative:
            ns = -ns

        # Handle overflow
        if ns < -2**31:
            return -2**31
        if ns > 2**31 - 1:
            return 2**31 - 1

        return ns
    
# Time complexity: O(n)
# Space complexity: O(1)

# The algorithm converts a string to an integer.
# The algorithm removes leading and trailing whitespace from the string.
# The algorithm initializes a flag to track the sign of the integer.
# The algorithm initializes an index to iterate over the string.
# The algorithm checks for the sign of the integer.
# The algorithm converts the digits to an integer.
# The algorithm applies the sign to the integer.
# The algorithm handles overflow by returning the maximum or minimum integer value.

solution = Solution()
print(solution.myAtoi("42")) # 42
print(solution.myAtoi("   -42")) # -42
print(solution.myAtoi("4193 with words")) # 4193
print(solution.myAtoi("words and 987")) # 0