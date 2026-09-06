T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 합들을 저장할 변수
    sums = []

    for i in range(N-M+1):
        current_sum = sum(nums[i: i+M])
        sums.append(current_sum)

    answer  = max(sums) - min(sums)

    print(f"#{tc} {answer}")


# max, min 사용하지 않는 방법
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    sums = []

    for i in range(N-M+1):
        current_sum = sum(nums[i:i+M])
        sums.append(current_sum)

    max_sum = sums[0]
    min_sum = sums[0]

    for j in range(len(sums)):
        if sums[j] > max_sum:
            max_sum = sums[j]
        if sums[j] < min_sum:
            min_sum = sums[j]
    answer = max_sum - min_sum
    print(f"#{tc} {answer}")






