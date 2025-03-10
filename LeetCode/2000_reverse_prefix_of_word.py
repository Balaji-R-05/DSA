# 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = 0
        for i in range(len(word)):
            if word[i]==ch:
                end = i
                break

        return word[0:end+1][::-1]+word[end+1:]
    
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = word.find(ch)  
        if end == -1:
            return word
        return word[:end+1][::-1] + word[end+1:]
    
# Time Complexity: O(n)
# Space Complexity: O(1)