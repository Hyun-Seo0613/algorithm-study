a = 128
b = 2021

while b != 0:
    tmp = a % b
    a = b
    b = tmp

print(a)
