# 2824. Count Pairs Whose Sum is Less than Target

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() 
        count = 0 
        left = 0 
        right = len(nums)-1 
        while(left < right): 
            if(nums[left] + nums[right] < target):
                count += right-left 
                left += 1 
            else:
                right -= 1 
        return count 
    
# Time complexity: O(nlogn)
# Space complexity: O(1)

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] < target:
                    count+=1
        return count
    
# Time complexity: O(n^2)
# Space complexity: O(1)

