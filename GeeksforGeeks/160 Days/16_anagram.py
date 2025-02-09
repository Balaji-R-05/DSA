# 16. Anagram
#Function is to check whether two strings are anagram of each other or not.

class Solution:
    def areAnagrams(self, s1, s2):
        arr = [0]*26
        for ch in s1:
            arr[ord(ch)-ord('a')] += 1
        
        for ch in s2:
            arr[ord(ch)- ord('a')] -=1
            
        for count in arr:
            if count!=0:
                return False
            
        return True
        
# Time Complexity: O(n + m)
# Auxiliary Space: O(1)