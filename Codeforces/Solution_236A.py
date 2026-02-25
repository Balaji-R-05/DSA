# def main():
#     username = input().strip()
#     if len(set(username)) % 2 == 1:
#         print("IGNORE HIM!")
#     else:
#         print("CHAT WITH HER!")
        
def main():
    username = input().strip()
    seen = [False] * 26
    distinct = 0
    for ch in username:
        idx = ord(ch) - ord('a')
        if not seen[idx]:
            seen[idx] = True
            distinct += 1
    
    if distinct % 2 == 1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")


if __name__ == "__main__":
    main()
    