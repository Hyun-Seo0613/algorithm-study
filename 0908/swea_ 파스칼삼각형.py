# 첫번째 줄은 항상 숫자 1
# 두번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자 합으로 구성된다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 파스칼 삼각형을 저장할 2차원 리스트 만들기
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        # 각 행의 첫 숫자와 마지막 숫자 1
        arr[i][0] = 1
        arr[i][i] = 1

        # 가운데 숫자
        for j in range(1, i):
            #           왼쪽 위        +  오른쪽 위
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
               # 3,2  = 2, 1 + 2, 2

    print(f"#{tc}")
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()

# 스택으로
# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = []
#
#     # i : 행
#     for i in range(n):
#         row = []
#         # j : 줄
#         for j in range(i + 1):
#             if j == 0:
#                 row.append(1)
#             elif j == i:
#                 row.append(1)
#             else:
#                 a = arr[i - 1][j - 1] + arr[i - 1][j]
#                 row.append(a)
#         arr.append(row)
#     print(f"#{tc}")
#     for row in arr:
#         print(*row)