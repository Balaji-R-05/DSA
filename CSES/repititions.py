def main():
    s = input().strip()
    n = len(s)
    max_len = 0
    curr_len = 0
    curr_char = ''
    for i in range(n):
        if s[i] == curr_char:
            curr_len += 1
        else:
            curr_char = s[i]
            curr_len = 1
        max_len = max(max_len, curr_len)
    print(max_len)

if __name__ == "__main__":
    main()

# Time Complexity: O(N)
# Space Complexity: O(1)