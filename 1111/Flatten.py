# 평탄화
T = 10
for tc in range(1, T+1):
    # 덤프횟수
    D = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    for i in range(D):
        max_idx = 0
        min_idx = 0
        for j in range(len(heights)):
            if heights[j] < heights[min_idx]:
                min_idx = j
            if heights[j] > heights[max_idx]:
                max_idx = j

        heights[min_idx] += 1
        heights[max_idx] -= 1

    # 덤프가 끝난 후
    # 최고점과 최저점의 차이를 구해야함
    max_height = heights[0]
    min_height = heights[0]
    for k in range(len(heights)):
        if heights[k] > max_height:
            max_height = heights[k]

        if heights[k] < min_height:
            min_height = heights[k]

    answer = max_height - min_height

    print(f"#{tc} {answer}")





