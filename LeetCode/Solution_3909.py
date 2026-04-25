# 3909. Compare Sums of Bitonic Parts

class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        peak = -1
        for i in range(1,n-1):
            if nums[i] > nums[i-1] and nums[i] >  nums[i+1]:
                peak = i
        asd = nums[0:peak+1]
        des = nums[peak:]
        asd_sum = sum(nums[0:peak+1])
        des_sum = sum(nums[peak:])
        print(f"{asd_sum} -- {des_sum}")
        print(f"{asd} -- {des}")
        if asd_sum > des_sum: return 0
        if des_sum > asd_sum: return 1
        return -1
    
# Time complexity: O(n)
# Space complexity: O(n)