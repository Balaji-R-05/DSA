# 1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        return (nums[-2]-1)*(nums[-1]-1)
    
# Time complexity: O(nlogn)
# Space complexity: O(1)

solution = Solution()
nums = [3, 4, 5, 2] # 12
print(solution.maxProduct(nums))

nums = [1, 5, 4, 5] # 16
print(solution.maxProduct(nums))
