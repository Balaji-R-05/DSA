# 339A - Helpful Maths

def main():
    l = list(map(int, input().split("+"))) 
    l.sort()  
    print("+".join(map(str, l)))  

if __name__ == "__main__":
    main()
