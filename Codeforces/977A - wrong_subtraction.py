# 977A - Wrong Subtraction

def wrong_sub(num: int, n: int) -> int:
    for _ in range(n):
        if num % 10 == 0:
            num //= 10
        else:
            num -= 1
    return num

if __name__ == "__main__":
    num, n = map(int, input().split())
    print(wrong_sub(num, n))


# Time Complexity: O(n)
# Space Complexity: O(1)
