# 3340. Check Balanced String

class Solution:
  def isBalanced(self, num: str) -> bool:
    nums = list(map(int, num))
    return sum(nums[::2]) == sum(nums[1::2])
  
# Time Complexity: O(N)
# Space Complexity: O(N)