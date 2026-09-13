T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = input()

    count = [0] * 10

    for i in nums:
        count[int(i)] += 1

    max_count =  0
    max_num = 0

    for j in range(10):
        if count[j] >= max_count:
            max_count = count[j]
            max_num = j

    print(f"#{tc} {max_num} {max_count}")

