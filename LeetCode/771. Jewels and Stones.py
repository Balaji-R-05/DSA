# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(jewels)
        for i in stones:
            if i in jewels:
                count+=1
        return count        
    
# Time complexity: O(n)
# Space complexity: O(n)