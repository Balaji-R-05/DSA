# 896. Monotonic Array

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_decreasing = False
            if nums[i] > nums[i + 1]:
                is_increasing = False
        
        return is_increasing or is_decreasing

 
# Time complexity: O(n)
# Space complexity: O(1)

solution = Solution()
print(solution.isMonotonic([1,2,2,3]))
print(solution.isMonotonic([1,3,2]))