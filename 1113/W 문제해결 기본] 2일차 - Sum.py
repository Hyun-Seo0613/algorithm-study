T = 10
for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0

    # 각 행의 합
    for i in range(100):
        # 새로운 행으로 넘어갈 때마다 reset 되어야함
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if row_sum > max_v:
            max_v = row_sum
    # 각 열의 합
    for j in range(100):
        # 새로운 행으로 넘어갈 때마다 reset 되어야함
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if col_sum > max_v:
            max_v = col_sum

    # 각 대각선의 합(왼쪽위에서 오른쪽아래로, 오른쪽위에서 왼쪽아래로)
    diagonal_sum1 = 0
    diagonal_sum2 = 0
    for k in range(100):
        diagonal_sum1 += arr[k][k]
        diagonal_sum2 += arr[k][99-k]

    if diagonal_sum1 > max_v:
        max_v = diagonal_sum1
    if diagonal_sum2 > max_v:
        max_v = diagonal_sum2

    print(f"#{tc} {max_v}")
