
def register_sys(n):
    name_count = {}  
    res = []
    
    for _ in range(n):
        name = input().strip()
        if name in name_count:
            name_count[name] += 1
            new_name = f"{name}{name_count[name]}"
            res.append(new_name)
        else:
            name_count[name] = 0  
            res.append("OK")
    
    print("\n".join(res))
 
n = int(input())
register_sys(n)