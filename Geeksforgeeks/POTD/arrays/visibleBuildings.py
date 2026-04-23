# Buildings with Sunlight

# Given an array of positive integers representing the heights of buildings, determine how many buildings will receive sunlight.
# A building receives sunlight if there are no taller buildings to its right.

class Solution:
    def visibleBuildings(self, arr):
        res = 1
        curr = arr[0]
        for i in range(1, len(arr)):
            if arr[i] >=  curr:
                res += 1
                curr = arr[i]
        return res
    
# Time Complexity: O(N)
# Space Complexity: O(1)