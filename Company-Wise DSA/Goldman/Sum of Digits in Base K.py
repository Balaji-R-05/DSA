# Sum of Digits in Base K

# Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.
# After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

# -------- Input Format
# First line contains the integer n.
# Second line contains the integer k.
# -------- Output Format
# Display the sum of digits after converting the number into base k.

# Constraints
# 1 <= n <= 100
# 2 <= k <= 10

# Input: 10 10
# Output: 1

# Input: 8 2
# Output: 1


import sys

def sumBase(n, k):
    count = 0
    while n>0:
        count += n%k
        n //=k
    return count


def main():
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    result = sumBase(n, k)
    print(result)


if __name__ == "__main__":
    main()