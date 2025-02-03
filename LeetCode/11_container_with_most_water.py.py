class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        while(left<right):
            vol = min(height[left], height[right]) * (right-left)
            maxWater = max(vol, maxWater)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxWater
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))
