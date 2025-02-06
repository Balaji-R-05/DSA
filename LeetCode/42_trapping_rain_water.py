# 42. Trapping Rain Water

class Solution:
    def trap(self, height: list[int]) -> int:
        vol = 0  
        l, r = 0, len(height) - 1  
        lmax, rmax = 0, height[r]  
        
        while l < r:
            if height[l] <= height[r]:
                if height[l] < lmax:
                    vol += lmax - height[l] 
                else:
                    lmax = height[l]  
                l += 1  
            else:
                if height[r] < rmax:
                    vol += rmax - height[r]  
                else:
                    rmax = height[r]  
                r -= 1  
        return vol
    
# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(Solution().trap([4,2,0,3,2,5]))  # 9