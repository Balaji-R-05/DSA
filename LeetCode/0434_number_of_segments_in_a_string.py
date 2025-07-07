# 434. Number of Segments in a String

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split()
        return len(s)
    
# Time Complexity: O(n) where n is the length of the string s
# Space Complexity: O(n) for storing the segments in the list