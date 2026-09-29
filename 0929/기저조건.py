def kfc(x):
    if x == 2:
        return
    
    print(x)
    kfc(x + 1)
    print(x)


kfc(0)

print("끝")