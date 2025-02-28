# 2114. Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            sentence = sentence.split()
            res = max(res, len(sentence))
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)
