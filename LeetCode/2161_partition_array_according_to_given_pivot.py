# 2161. Partition Array According to Given Pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        p = []
        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])
            else:
                p.append(nums[i])

        return left+p+right
    
# Time complexity: O(n)
# Space complexity: O(n)

