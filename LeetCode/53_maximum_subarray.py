from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float("-inf")
        sumOfArray = 0
        for j in nums:
            sumOfArray += j
            if sumOfArray>max:
                max = sumOfArray
            if sumOfArray<0:
                sumOfArray = 0
        
        return max
    
# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([1])) # 1
print(s.maxSubArray([5,4,-1,7,8])) # 23
