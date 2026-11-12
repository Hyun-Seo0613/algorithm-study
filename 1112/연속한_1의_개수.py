T = int(input())
for tc in range(1, T+1):
    # 수열의 길이 N
    N = int(input())
    # N개의 0과1로 구성된 수열(공백없이)
    arr = list(map(int, input()))

    count = 0
    answer = 0
    # 연속한 1의 개수 중 최대값을 출력하는 프로그램
    for i in range(N):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        answer = max(count, answer)
    print(f"#{tc} {answer}")

