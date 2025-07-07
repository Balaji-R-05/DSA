# 41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        from collections import Counter
        map = Counter(nums)

        ctr = 1
        while True:
            if map[ctr] == 0: return ctr
            ctr+=1

# Time Complexity: O(n)
# Space Complexity: O(n)