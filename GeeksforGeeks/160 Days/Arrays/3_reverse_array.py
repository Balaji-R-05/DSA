# 3. Reverse an Array
# Given an array, the task is to reverse the array.

class Solution:
    def reverseArray(self, arr):
        i = 0
        j = len(arr)-1
        while(i<j):
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        return arr

# Time Complexity: O(n)
# Auxiliary Space: O(1)