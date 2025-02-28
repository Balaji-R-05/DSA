# 2859. Sum of Values at Indices With K Set Bits

from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def bitCount(n):
            count = 0
            while(n>0):
                count += n&1
                n>>=1
            return count

        sum = 0
        for i in range(len(nums)):
            if bitCount(i)==k:
                sum += nums[i]

        return sum
    
# Time complexity: O(n)
# Space complexity: O(1)

# ------------------------------------------------------------------------------------------------------------------------

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            a=i.bit_count()
            if a==k:
                ans+=nums[i]
        return ans
    
# Time complexity: O(n)
# Space complexity: O(1)
