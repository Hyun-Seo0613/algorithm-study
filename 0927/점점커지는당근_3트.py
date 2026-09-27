T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    count = 1
    answer = 1

    for i in range(1, N):
        if C[i-1] < C[i]:
            count += 1
        else:
            count = 1
        answer = max(answer, count)
    print(f"#{tc} {answer}")
