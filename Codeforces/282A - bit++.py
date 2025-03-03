# 282A - Bit++

def bit_result(n:int):
    count = 0
    for _ in range(n):
        s = input().strip()
        if s[1]=='+':
            count+=1
        else:
            count-=1
            
    return count


if __name__ == "__main__":
    n = int(input())
    print(bit_result(n))

# Time complexity: O(n)
# Space complexity: O(1)