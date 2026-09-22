T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 여기 못적은 부분
    count = [0] * 10

    k = 1
    # count[i] = 1 => 이런식으로 count의 합이 10이되면 바로 종료한다.
    while True:
        nums = N * k
        for i in nums:
            # += 1 하면 안됨
            count[i] = 1

        if sum(count) == 10:
            break

        k += 1

    print(f"#{tc} {nums}")
