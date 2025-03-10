# 1313. Decompress Run-Length Encoded List

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        i=0
        while i<n:
            res.extend([nums[i+1]]*nums[i])
            i+=2
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        i=0
        while i<n:
            for _ in range(nums[i]):
                res.append(nums[i+1])
            i+=2
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)