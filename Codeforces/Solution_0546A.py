# 546A - Soldier and Bananas

def main():
    k, n, w = map(int, input().split())
    total = 0
    for i in range(1, w+1):
        total += (i * k)
    print(total - n  if total > n else 0)
 
if __name__ == "__main__":
    main()

# Time Complexity: O(w)
# Space Complexity: O(1)