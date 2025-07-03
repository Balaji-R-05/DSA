s = input().lower().strip()
n = len(s)
mat = [[0]*n for _ in range(n)]

max_length = 1
longest_palindrome = ""

for i in range(n):
    mat[i][i] = 1 

for i in range(n):
    for j in range(n):
        if s[i] == s[j] and j - i == 1:
            mat[i][j] = 1
            if max_length < 2:
                max_length = 2
                longest_palindrome = s[i:j+1]
        elif i < n - 1 and j < n - 1 and s[i] == s[j] and mat[i + 1][j - 1] == 1:
            mat[i][j] = 1
            if max_length < j - i + 1:
                max_length = j - i + 1
                longest_palindrome = s[i:j+1]
        
        
        


print(*mat, sep="\n")
        