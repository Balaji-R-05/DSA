def word(s:str):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        else:
            lower_count += 1
        
    if upper_count > lower_count:
        print(s.upper())
    else:
        print(s.lower())
        
if __name__ == "__main__":
    s = input().strip()
    word(s)