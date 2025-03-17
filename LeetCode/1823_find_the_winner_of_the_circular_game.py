# 1823. Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        def helper(arr, start):
            if len(arr)==1:
                return arr[0]
            remove_index = (start+k-1)%len(arr)
            del arr[remove_index]
            return helper(arr, remove_index)

        return helper(arr, 0)
    

# Time complexity: O(nk)
# Space complexity: O(n)