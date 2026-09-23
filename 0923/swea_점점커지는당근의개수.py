T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    count = 1
    answer = 1

    # 연속으로 커지는 당근 개수의 최대값 출력
    for i in range(1, N):
        if C[i-1] < C[i]:
            count += 1
            answer = max(answer, count)
        else:
            count = 1
    print(f"#{tc} {answer}")
