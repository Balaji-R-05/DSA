# 1752. Check if array is Rotated and Sorted

class Solution:
    def check(self, nums: list[int]) -> bool:
        nums_length = len(nums)
        count = 0
        for i in range(0,nums_length-1):
            if nums[i]>nums[i+1]:
                count+=1
        if nums[0]<nums[nums_length-1]:
            count+=1
        return count<=1
    
# Time complexity: O(n)
# Space complexity: O(1)

Solution().check([3,4,5,1,2]) # True
Solution().check([2,1,3,4]) # False