T = 10
for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))

    for _ in range(N):
        max_height = max(height)
        min_height = min(height)

        if max_height - min_height <= 1:
            break
        max_idx = height.index(max_height)
        min_idx = height.index(min_height)

        height[max_idx] -= 1
        height[min_idx] += 1

    result = max(height) - min(height)
    print(f"#{tc} {result}")