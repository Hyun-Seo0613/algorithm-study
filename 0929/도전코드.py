#  1부터 6까지 사용하는 중복순열 ([1,1,1] ~ [6,6,6])을 출력하는 코드를 재귀호출로 구현
path = []

# i: 단계
def KFC(i):

    # 기저 조건 (숫자 3개 고르면 끝)
    if i == 3:
        print(path)
        return
    # path.append(1)
    # KFC(i+1)
    # path.append(2)
    # KFC(i+1)
    #.. 6까지 반복

    for j in range(1, 7):
        path.append(j)
        KFC(i+1)
        path.pop()