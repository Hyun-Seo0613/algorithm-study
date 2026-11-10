# swea_View
# 양쪽 모두 거리 2이상의 공간이 확보될 때 조망권 확보
T = 10
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    # idea: i번째 건물에서 i-2, i-1,i+1,i+2 중에서의 최댓값을 빼면 조망권 확보 세대 알 수 있음
    # if height[i] > max_height: max_height을 heights[i]로 한다.
    # 양쪽으로 2칸씩 높이 0임 (건물없음)
    for i in range(2, N-2):
        max_height = max(
            heights[i-1], heights[i-1], heights[i+1], heights[i+2]
        )
        if heights[i] > max_height:
            max_height = heights[i]

            answer += heights[i] - max_height
    print(f"#{tc} {answer}")