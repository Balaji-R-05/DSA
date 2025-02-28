# 1832. Check if the Sentence Is Pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = [0]*26
        for ch in sentence:
            arr[ord(ch)-ord('a')] = 1
        
        return all(arr)
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return (len(set(sentence)))==26
    
# Time Complexity: O(n)
# Space Complexity: O(1)