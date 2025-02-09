# 4. Rotate Array
# Given an array, the task is to rotate the array to the left by k steps, where k is non-negative.

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        def reverse(arr,start,end):
            while(start<end):
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
                
        n = len(arr)
        d = d%n
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
        reverse(arr,0,n-1)

# Time Complexity: O(n)
# Auxiliary Space: O(1)