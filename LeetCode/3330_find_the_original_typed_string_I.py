class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(0, len(word)-1):
            if word[i] == word[i+1]:
                count += 1
        return count
    
# Time Complexity: O(n)
# Space Complexity: O(1)