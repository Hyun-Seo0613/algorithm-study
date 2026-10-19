# 마름모
T = int(input())
for tc in range(1, T+1):
    # 농장의 크기
    N = int(input())
    # 농장 속 농작물의 가치
    arr = [list(map(int, input())) for _ in range(N)]

    # 마름모 모양에 해당하는 칸만 골라서 더하기
    # 가운데 index 를 먼저 칠하고 가운데에서 얼마나 떨어졌나? 규칙찾기
    mid = N // 2
    width = 0
    answer = 0

    for i in range(N):
        for j in range(mid-width, mid+width+1):
            answer += arr[i][j]
            
        # 중간행 가기 전이면 width 를 늘리다가
        if i < mid:
            width += 1
        # 중간행 지나면서 다시 width 줄이기 => 마름모특징
        else:
            width -= 1
    print(f"#{tc} {answer}")