# 112A - Relative Sort

def main():
    s1 = input().strip().lower()
    s2 = input().strip().lower()
    n = len(s1)
    for i in range(n):
        if s1[i] > s2[i]:
            print(1)
            return
        elif s2[i] > s1[i]:
            print(-1)
            return
    print(0)
    
if __name__ == "__main__":
        main()

# Time complexity: O(N)
# Space complexity: O(1)