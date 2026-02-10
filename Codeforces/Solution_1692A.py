def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        print(sum(x > a for x in (b, c, d)))
 
if __name__ == "__main__":
    main()