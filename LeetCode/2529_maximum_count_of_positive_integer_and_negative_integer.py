# 2529. Maximum Count of Positive Integer and Negative Integer

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = pos = 0
        for i in nums:
            if i<0: neg+=1
            elif i>0: pos+=1
            
        return max(neg, pos)

# Time complexity: O(n)
# Space complexity: O(1)


# ----------------------------------------------------------------------------------------------------

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        neg = left

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1

        pos = len(nums) - left  

        return max(neg, pos)
    
# Time complexity: O(log(n))
# Space complexity: O(1)