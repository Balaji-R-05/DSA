# 2545. Sort the Students by Their Kth Score

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)
    
# Time complexity: O(nlogn)
# Space complexity: O(1)

# ------------------------------------------------------------------------------------------------------------------------