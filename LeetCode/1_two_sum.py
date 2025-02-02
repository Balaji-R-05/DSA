class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []

# Test cases
solution = Solution()

# Test case 1: Basic case
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]

# Test case 2: No solution
nums = [3, 2, 4]
target = 6
print(solution.twoSum(nums, target))  # Output: []

# Test case 3: Negative numbers
nums = [-1, 0, 1, 2, -1, -4]
target = -1
print(solution.twoSum(nums, target))  # Output: [0, 4]



