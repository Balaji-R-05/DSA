# 110A - Nearly Lucky Number

def main():
    N = int(input())
    s = set([4, 7])
    while (N > 0):
        rem = N%10
        N //= 10
        if rem not in s:
            print("NO")
            return
    print("YES")
    
if __name__ == "__main__":
    main()

# Time complexity: O(log(N))
# Space complexity: O(1)