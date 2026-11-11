T = 10
for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    # 이 문제에서 찾는 행, 열, 대각선 중 최대
    max_v = 0

    # 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램 작성하기
    # 1. 각 행
    # i 고정시키고 고정시키고
    for i in range(100):
        row_sum = 0
        #
        for j in range(100):
            row_sum += arr[i][j]
        if row_sum > max_v:
            max_v = row_sum

    # 2. 각 열
    # j 고정시키고
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if col_sum > max_v:
            max_v = col_sum
    # 3. 대각선의 합 (왼쪽위에서 오른쪽 아래로, 그 반대 총 2개)
    diagonal1 = 0
    diagonal2 = 0
    for i in range(100):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][99-i]

    if diagonal1 > max_v:
        max_v = diagonal1
    if diagonal2 > max_v:
        max_v = diagonal2

    print(f"#{tc} {max_v}")
            

