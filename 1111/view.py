# 조망권 확보 세대 수 구하기
T = 10
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    answer = 0
    # 현재 높이 , 최대 높이
    for i in range(2, N-2):
        # 주변 높이 중 가장 높은 층 수
        max_height = max(
            heights[i-2],
            heights[i-1],
            heights[i+1],
            heights[i+2]
        )

        if heights[i] > max_height:
            answer += heights[i] - max_height

    print(f"#{tc} {answer}")