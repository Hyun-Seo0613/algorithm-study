T = 10

for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_v = 0

    # 각 행의 합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if row_sum > max_v:
            max_v = row_sum

    # 각 열의 합
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if col_sum > max_v:
            max_v = col_sum

    # 대각선의 합 (왼쪽위에서 오른쪽 아래로, 오른쪽위에서 왼쪽 아래로 총 2개)
    diagonal1 = 0
    diagonal2 = 0
    for i in range(100):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][99-i]

    if diagonal1 >max_v:
        max_v = diagonal1
    if diagonal2 > max_v:
        max_v = diagonal2
    print(f"#{test_case} {max_v}")


