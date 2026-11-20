# 반복횟수가 안나와있음 => for 문 x, while 문 O
while True:
    A, B = map(int, input().split())
    # 종료조건
    if A == 0 and B == 0:
        break
    print(A + B)