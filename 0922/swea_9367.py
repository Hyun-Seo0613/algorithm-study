T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    count = 1
    answer = 1

    for i in range(1, len(C)):
        if C[i] - C[i-1] > 0:
            count += 1
            answer = max(count, answer)
        else:
            count = 1
    print(f"#{tc} {answer}")

