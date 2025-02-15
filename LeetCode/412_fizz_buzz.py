# 412. Fizz Buzz 

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lst.append("FizzBuzz")
            elif i%3==0: lst.append("Fizz")
            elif i%5==0: lst.append("Buzz")
            else: lst.append(f"{i}")
        return lst        
    
# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().fizzBuzz(15)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
print(Solution().fizzBuzz(1)) # ["1"]