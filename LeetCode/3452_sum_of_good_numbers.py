# 3452. Sum of Good Numbers

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            left = nums[i - k] if i - k >= 0 else float('-inf')
            right = nums[i + k] if i + k < n else float('-inf')
            
            if nums[i] > left and nums[i] > right:
                res += nums[i]
                
        return res

# Time complexity: O(n)
# Space complexity: O(1)


