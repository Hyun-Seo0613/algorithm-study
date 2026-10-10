# 10진수를 2진수로 표현
num = 13
answer = []

while num > 0:
    print(num % 2)
    num //= 2
    # 나머지를 구하는 순서대로 출력하면 거꾸로 출력되기 때문에 순서뒤집기 
print(*answer[::-1], sep="")