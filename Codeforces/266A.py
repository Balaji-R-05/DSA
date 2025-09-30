def main():
    N = int(input())
    ch = input().strip()
    count = 0
    for i in range(1, N):
        if ch[i] == ch[i-1]:
            count+=1
            
    print(count)
    
if __name__ == "__main__":
    main()