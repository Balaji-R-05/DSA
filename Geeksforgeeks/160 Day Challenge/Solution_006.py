from collections import Counter

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        res = []
        arr = Counter(arr)
        for i in arr:
            if arr[i]>n//3:
                res.append(i)
        return sorted(res)
    
# Time Complexity: O(N)
# Space Complexity: O(N)