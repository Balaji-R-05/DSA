# 2125. Number of Laser Beams in a Bank

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = []
        for row in bank:
            r = row.count("1") 
            if r!=0:
                res.append(r)

        ans = 0
        for i in range(len(res)-1):
            ans += res[i]*res[i+1]

        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)

