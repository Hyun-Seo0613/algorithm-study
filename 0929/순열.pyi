path = []
used = [0] * 3

# i : 단계, 이 문제에서는 숫자를 고른 횟수
def KFC(i):

    # 기저 조건 (숫자 3개 고르면 끝)
    if i == 3:
        print(path)
        return

    # path.append(1)
    # KFC(i+1)
    # path.append(2)
    # KFC(i+1)
    #
    # ..
    #
    # path.append(6)
    # KFC(i+1)
    for j in range(3):
        if used[j]:
            continue

        used[j] = 1
        path.append(j)
        KFC(i+1)
        used[j] = 0
        path.pop()

KFC(0)
