# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s)-1
        while(start<end):
            while (start<end) and not self.isVowel(s[start]) :
                start+=1
            while (start < end) and not self.isVowel(s[end]):
                end-=1
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        
        return "".join(s)

    def isVowel(self,ch):
        return ch in ['a','e','i','o','u','A','E','I','O','U']
    
# Time complexity: O(n)
# Space complexity: O(1)


print(Solution().reverseVowels("hello")) # "holle"
print(Solution().reverseVowels("leetcode")) # "leotcede"