# 3895. Count Digit Appearances

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = 0
        for num in nums:
            while num > 0:
                rem = num % 10
                num //= 10
                if rem == digit:
                    res += 1
        return res
    
# Time complexity: O(n * log(m)), where n is the length of nums and m is the maximum number in nums
# Space complexity: O(1)