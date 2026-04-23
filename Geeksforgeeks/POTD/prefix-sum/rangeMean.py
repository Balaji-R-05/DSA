class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]

        result = []
        
        for l, r in queries:
            length = r - l + 1
            if l == 0:
                total = prefix[r]
            else:
                total = prefix[r] - prefix[l-1]
            
            result.append(total // length)
        
        return result
    
# Time Complexity: O(n + q) where n is the length of the array and q is the number of queries.
# Space Complexity: O(n) for the prefix sum array.