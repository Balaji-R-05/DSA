# 71A - Way Too Long Words

n = int(input())

for _ in range(n):
    word = input().strip()
    l = len(word)
    if len(word) > 10:
        print(f"{word[0]}{l-2}{word[-1]}")
    else:
        print(word)

# Time Complexity: O(n)
# Space Complexity: O(1)