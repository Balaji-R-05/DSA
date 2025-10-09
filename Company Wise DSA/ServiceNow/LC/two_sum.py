from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in map:
                return [i, map[res]]
            map[nums[i]] = i
        return []