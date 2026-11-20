T = 10
for tc in range(1, T+1):
    D = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    for _ in range(D):
        max_height = 0
        min_height = 0

        for i in range(len(heights)):
            if heights[i] > heights[max_height]:
                max_height = i
            if heights[i] < heights[min_height]:
                min_height = i

        if heights[max_height] - heights[min_height] <= 1:
            break

        # 평탄화진행
        heights[max_height] -= 1
        heights[min_height] += 1

    answer = max(heights) - min(heights)
    print(f"#{tc} {answer}")