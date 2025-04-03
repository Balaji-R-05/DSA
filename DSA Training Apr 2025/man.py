def test(k):
    if k>155:
        return
    print(k)
    test(k+2)
    print(k) 

k = 150
test(k)