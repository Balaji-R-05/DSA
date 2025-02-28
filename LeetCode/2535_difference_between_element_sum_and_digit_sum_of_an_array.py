# 2535. Difference Between Element Sum and Digit Sum of an Array

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digitSum(n:int) -> int:
            s = 0
            while(n>0):
                s += n%10
                n//=10
            return s

        element_sum = sum(nums)
        digit_sum  = 0
        for i in nums:
            if i>9:
                digit_sum += digitSum(i)
            else:
                digit_sum += i
            
        return abs(element_sum - digit_sum)