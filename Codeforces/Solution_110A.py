# 110A - Nearly Lucky Number

def main():
    s = input().strip()
    count = 0
    for c in s:
        if c == '4' or c == '7':
            count += 1
    if count == 0:
        print("NO")
        return
 
    for c in str(count):
        if c not in "47":
            print("NO")
            return
 
    print("YES")
 
 
if __name__ == "__main__":
    main()

# Time complexity: O(N)
# Space complexity: O(1)