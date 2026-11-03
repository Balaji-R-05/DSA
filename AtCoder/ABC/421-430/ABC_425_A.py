def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += ((-1) ** i) * (i ** 3)
    print(ans)

if __name__ == "__main__":
    main()