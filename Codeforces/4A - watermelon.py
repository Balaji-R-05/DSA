# 4A - Watermelon

def watermelon():
    num = int(input())
    print("YES" if num % 2 == 0 and num > 2 else "NO")

if __name__ == "__main__":
    watermelon()

# Time Complexity: O(1)
# Space Complexity: O(1)