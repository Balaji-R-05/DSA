# 1030A - In Search of an Easy Problem

def main():
    n = int(input())
    l = list(map(int, input().split()))
    
    if 1 in l:
        print("HARD")
    else:
        print("EASY")
        
if __name__ == "__main__":
    main()