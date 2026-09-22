T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    answer = []

    for i in range(5):
        max_num = nums[0]
        min_num = nums[0]

        for num in nums:
            if num > max_num:
                max_num = num

            if num < min_num:
                min_num = num

        answer.append(max_num)
        answer.append(min_num)

        nums.remove(max_num)
        nums.remove(min_num)

    print(f"#{tc}", *answer)




