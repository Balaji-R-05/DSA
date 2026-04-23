

class Solution:
    def isPower(self, x, y):
        if y == 1:
            return True
        if x == 1:
            return y == 1
        if x == 0:
            return y == 0
        
        while y > 1:
            if y % x != 0:
                return False
            y //= x
        return True
    
# Time Complexity: O(log y) in the worst case when x is 2.
# Space Complexity: O(1) since we are using only a constant amount of space.