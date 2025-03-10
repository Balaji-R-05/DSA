# 200B - Drinks

def main():
    n = int(input())
    l = list(map(int, input().split()))
    print(sum(l)/n)
    
if __name__ == "__main__":
    main()