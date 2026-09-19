T = int(input())

for tc  in range(1, T+1):
    nums = list(map(int, input().split()))

    answer = 0

    for i in nums:
        if i % 2 != 0:
            answer += i

    print(f"#{tc} {answer}")

