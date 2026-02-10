def main():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        n = len(s)
        
        if n % 2 != 0:
            print("NO")
            continue
        
        mid = n // 2
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()

# Time Complexity: O(N)
# Space Complexity: O(1)