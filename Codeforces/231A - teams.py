# 231A - Team

def team():
    n = int(input())
    count = 0
    for _ in range(n):
        a, b, c= map(int, input().split())
        if a+b+c >1:
            count+=1
    print(count)

if __name__ == "__main__":
    team()

# Time complexity: O(n)
# Space complexity: O(1)

