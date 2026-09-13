T = 10
for tc in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))

    count = 0
    for i in range(2, N - 2):
        max_heights = max(
            heights[i - 2], heights[i - 1], heights[i + 1], heights[i + 2]
        )

        if heights[i] > max_heights:
            count += heights[i] - max_heights
    print(f"#{tc} {count}")
