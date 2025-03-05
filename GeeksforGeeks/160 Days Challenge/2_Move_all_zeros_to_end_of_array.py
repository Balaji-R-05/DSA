# 2. Move all zeros to end of array
# Given an array, the task is to move all the zeros present in the array to the end of the array.

class Solution:
	def pushZerosToEnd(self,arr):
		n = len(arr)
		count = 0
		for i in range(n):
			if arr[i]!=0:
				arr[count],arr[i] = arr[i],arr[count]
		count+=1
		return arr
	
# Time Complexity: O(n)
# Auxiliary Space: O(1)

