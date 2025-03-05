# 110A - Nearly Lucky Number

def nearly_lucky(n:int):
    count = 0
    while n>0:
        if n%10==4 or n%10==7:
            count+=1
        n//=10
        
    print("YES" if (count==7 or count==4) else "NO")
    
if __name__ == "__main__":
    n = int(input())
    nearly_lucky(n)

# Time Complexity: O(d) where d is the number of digits in n
# Space Complexity: O(1)

def nearly_lucky(n: int):
    count = sum(1 for digit in str(n) if digit in {'4', '7'})
    print("YES" if count in {4, 7} else "NO")

if __name__ == "__main__":
    n = int(input())
    nearly_lucky(n)

# Time Complexity: O(d) where d is the number of digits in n
# Space Complexity: O(1)