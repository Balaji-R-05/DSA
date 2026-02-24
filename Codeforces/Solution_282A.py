def main():
    N = int(input())
    x = 0
    for _ in range(N):
        cmd = input().strip()
        x += 1 if cmd[1] == "+" else -1
    print(x)
    
if __name__ == "__main__":
    main()