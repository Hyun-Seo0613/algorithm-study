T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    # 마름모 모양에 해당되는 칸만 골라서 더하기
    # 가운데 index를 먼저 칠하고 가운데에서 얼마나 떨어졌는지? 규칙찾기
    mid = N // 2
    width = 0

    answer = 0

    for i in range(N):
        for j in range(mid-width, mid+width+1):
            answer += arr[i][j]

        # 가운데 행 전까지는 범위를 넓히고, 지나면 다시 줄인다.
        if i < mid:
            width += 1
        else:
            width -= 1

    print(f"#{tc} {answer}")
