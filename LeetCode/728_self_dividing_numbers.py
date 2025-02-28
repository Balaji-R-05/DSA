# 728. Self Dividing Numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDiv(num):
            temp = num
            while(temp>0):
                res = temp%10
                if res == 0 or num%res!=0:
                    return False
                temp//=10
            return True
        ans = []
        for i in range(left,right+1):
            if isSelfDiv(i):
                ans.append(i)
        return ans
    
# Time Complexity: O(n)
# Space Complexity: O(1)