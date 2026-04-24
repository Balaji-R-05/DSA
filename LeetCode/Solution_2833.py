# 2833. Furthest Point From Origin

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count_l = 0
        count_r = 0
        count = 0
        for move in moves:
            if move == "L": count_l += 1
            elif move == "R": count_r += 1
            else: count += 1
        
        return abs(count_l - count_r) + count
    
# Time Complexity: O(n)
# Space Complexity: O(1)