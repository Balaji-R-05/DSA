class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        i = 0
        j = len(arr)-1
        count = 0
        while(i<j):
            k = arr[i] + arr[j]
            if (k>=target):
                j-=1
            else:
                count += j-i
                i+=1
        return count
                

# Time Complexity: O(N log N) + O(N) ~ O(N log N)
# Space Complexity: O(1)