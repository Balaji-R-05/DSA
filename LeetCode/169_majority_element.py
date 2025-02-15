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

# Approach -> Boyer-Moore Voting Algorithm

# The algorithm maintains a count and a candidate for the majority element.
# Initially, the count is 0 and the candidate is None.
# For each element in the array, we update the count and candidate.
# If the count becomes 0, we update the candidate to the current element.
# The candidate is the majority element in the array.
# The algorithm returns the candidate as the majority element.

solution = Solution()
print(solution.majorityElement([3,2,3])) # 3
print(solution.majorityElement([2,2,1,1,1,2,2])) # 2