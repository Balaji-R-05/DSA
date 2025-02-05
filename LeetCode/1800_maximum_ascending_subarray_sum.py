# 1800. Maximum Ascending Subarray Sum

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = 0
        curr_sum = nums[0] 

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  
                curr_sum += nums[i]
            else:  
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]  

        return max(max_sum, curr_sum)  
    
solution = Solution()
print(solution.maxAscendingSum([10, 20, 30, 5, 10, 50]))  # 65
print(solution.maxAscendingSum([10, 20, 30, 40, 50]))  # 150
print(solution.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))  # 33