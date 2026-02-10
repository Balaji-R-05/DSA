# Codeforces Problem 158A - Next Round

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    target = arr[k-1]
    count = sum(1 for score in arr if score >= target and score > 0)
    print(count)
 
if __name__ == "__main__":
    main()

# Time Complexity: O(N)
# Space Complexity: O(1)