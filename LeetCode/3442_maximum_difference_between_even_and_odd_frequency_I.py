# 3442. Maximum Difference Between Even and Odd Frequency I

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        even_freq = []
        odd_freq = []
        for char, count in freq.items():
            if count % 2 == 0:
                even_freq.append(count)
            else:
                odd_freq.append(count)

        max_odd = max(odd_freq) if odd_freq else 0
        min_even = min(even_freq) if even_freq else 0

        return max_odd - min_even
    
# Time complexity: O(n)
# Space complexity: O(n)

