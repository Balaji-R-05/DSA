# 520A - Pangram

def is_pangram(s:str):
    return len(set(s.lower()))==26
    
if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    print("YES" if is_pangram(s) else "NO")

# Time Complexity: O(n)
# Space Complexity: O(1)

""" Ignores numbers, spaces, and special characters """

def is_pangram(s: str) -> bool:
    return len(set(c for c in s.lower() if 'a' <= c <= 'z')) == 26  # Only count letters

if __name__ == "__main__":
    n = int(input())  # Read n (not used)
    s = input().strip()
    print("YES" if is_pangram(s) else "NO")
