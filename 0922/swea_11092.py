T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_num = nums[0]
    min_num = nums[0]

    max_idx = 0
    min_idx = 0

    for i in range(len(nums)):
        # 최대값의 위치와 최소값의 위치의 차이를 절대값abs로 출력하기
        # 수가 여러개 나오면 최소값은 가장 왼쪽, 최대값은 가장 오른쪽으로

        # 최대, 최소 먼저 찾기  / 위치도 동시에 갱신
        if nums[i] >= max_num:
            max_num = nums[i]
            max_idx = i

        if nums[i] < min_num:
            min_num = nums[i]
            min_idx = i

    result = abs(max_idx - min_idx)
    print(f"#{tc} {result}")

