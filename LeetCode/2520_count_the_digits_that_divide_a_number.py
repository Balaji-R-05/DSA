# 2520. Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while(temp>0):
            rem = temp%10
            if num%rem==0: count+=1
            temp//=10
        return count
    
# Time complexity: O(logn)
# Space complexity: O(1)