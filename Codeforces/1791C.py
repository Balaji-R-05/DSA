# 1791C - Prepend and Append

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        s = input().strip()
        l = len(s)
        i = 0
        j = l - 1
        while (i < j):
            if s[i] != s[j]:
                l -= 2
                i+=1
                j-=1
            else:
                break
        print(l)
 
if __name__ == "__main__":
    main()

# Time complexity: O(T * l)
# Space complexity: O(l)