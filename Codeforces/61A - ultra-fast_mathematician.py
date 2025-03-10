# 61A - Ultra-Fast Mathematician

def main():
    s = input().strip()
    t = input().strip()
    print("".join("0" if s[i] == t[i] else "1" for i in range(len(s))))

if __name__ == "__main__":
    main()