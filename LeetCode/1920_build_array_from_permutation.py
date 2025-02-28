# 1920. Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        for i in range(n):
            arr[i] = nums[nums[i]]
        
        return arr
    

# Time complexity: O(n)
# Space complexity: O(n)

