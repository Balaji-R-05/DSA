# 617A - Elephant

def elephant(n:int):
    if n%5==0:
        return n//5
    return n//5+1
    
if __name__ == "__main__":
    n = int(input())
    print(elephant(n))