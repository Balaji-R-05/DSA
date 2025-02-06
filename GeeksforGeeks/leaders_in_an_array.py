# Leaders In An Array

class Solution:
    def leaders(arr: int):
        res = []
        n = len(arr)
        maxRight = arr[-1]
        res.append(maxRight)
        for i in range(n-2,-1,-1):
            if arr[i]>=maxRight:
                maxRight=  arr[i]
                res.append(arr[i])
    
        res.reverse()
        return res

# Time Complexity - O(n)
# Space Complexity - O(n)

arr = [16, 17, 4, 3, 5, 2]
print(Solution.leaders(arr)) # [17, 5, 2]

arr = [1, 2, 3, 4, 5, 2]
print(Solution.leaders(arr)) # [5, 2]