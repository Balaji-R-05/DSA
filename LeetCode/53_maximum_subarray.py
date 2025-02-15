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

# Approach - Kadane's Algorithm
# 1. Initialize max with negative infinity and sumOfArray with 0.
# 2. Iterate through the array.
# 3. Add the current element to sumOfArray.
# 4. If sumOfArray is greater than max, update max.
# 5. If sumOfArray is less than 0, reset sumOfArray to 0.
# 6. Return max.


# Test cases
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([1])) # 1
print(s.maxSubArray([5,4,-1,7,8])) # 23
