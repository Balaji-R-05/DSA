# 236A - Boy or Girl

def boy_or_girl():
    unique_chars = set()
    for char in input().strip():
        unique_chars.add(char)
    
    print("CHAT WITH HER!" if len(unique_chars) % 2 == 0 else "IGNORE HIM!")

if __name__ == "__main__":
    boy_or_girl()
