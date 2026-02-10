def main():
    colors = set(map(int, input().split()))
    n = len(colors)
    print(4-n)
    
if __name__ == "__main__":
    main()

# Time complexity: O(1)
# Space complexity: O(1)