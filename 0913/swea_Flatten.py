T = 10

for tc in range(1, T+1):
    D = int(input())
    heights = list(map(int, input().split()))

    for i in range(D):
        max_height = max(heights)
        min_height = min(heights)

        max_idx = heights.index(max_height)
        min_idx = heights.index(min_height)

        heights[max_idx] -= 1
        heights[min_idx] += 1

    result = max(heights) - min(heights)
    print(f"#{tc} {result}")