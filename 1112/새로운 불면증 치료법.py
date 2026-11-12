T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = [0] * 10

    k = 1
    while True:
        num = N * k
        for i in str(num):
            count[int(i)] = 1
        if sum(count) == 10:
            break
        k += 1
    print(f"#{tc} {num}")