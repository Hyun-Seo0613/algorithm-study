T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [1, 2, 3, 4, 5, 6,
           7, 8, 9, 10, 11, 12]

    answer = 0

    # 모든 부분집합 확인
    for i in range(1 << 12):

        count = 0
        total = 0

        for j in range(12):

            # j번째 숫자가 현재 부분집합에 포함되어 있다면
            if i & (1 << j):
                count += 1
                total += arr[j]

        # 원소 개수가 N개 이고 합이 K인지 확인
        if count == N and total == K:
            answer += 1

    print(f"#{tc} {answer}")