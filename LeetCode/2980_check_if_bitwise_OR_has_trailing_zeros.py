# 2980. Check if Bitwise OR Has Trailing Zeros

from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(1+i,n):
                if (nums[i] | nums[j]) & 1 == 0:
                    return True
        return False
    
# Time complexity: O(n^2)
# Space complexity: O(1)


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i]&1==0:
                count+=1
            if count==2:
                return True
        
        return False
    
# Time complexity: O(n)
# Space complexity: O(1)