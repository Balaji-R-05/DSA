# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count+=1 if num == candidate else -1
        return candidate

# Time complexity: O(n)
# Space complexity: O(1)