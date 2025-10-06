# 1772A - A+B?

def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split("+"))
        print(a+b)
 
if __name__ == "__main__":
    main()

# Time Complexity: O(T)
# Space Complexity: O(1)