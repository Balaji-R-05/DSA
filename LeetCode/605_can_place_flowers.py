class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        while i<len(flowerbed):
            left = i == 0 or flowerbed[i-1]==0
            right = i == len(flowerbed)-1 or flowerbed[i+1]==0
            if left and right and flowerbed[i]==0:
                n-=1
                i+=2
            else:
                i+=1
        return n<=0
    
solution = Solution()
print(solution.canPlaceFlowers(flowerbed=[1,0,0,0,1], n = 1))
print(solution.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))