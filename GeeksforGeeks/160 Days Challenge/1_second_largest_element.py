# 1. Second Largest Element in an Array
# Given an array, the task is to find the second largest element in the array.

class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        largest = second_largest = -1
        for i in range(n):
            if arr[i]>largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i]>second_largest and arr[i]!=largest:
                second_largest = arr[i]

        return second_largest
    
# Time Complexity: O(n)
# Auxiliary Space: O(1)
        