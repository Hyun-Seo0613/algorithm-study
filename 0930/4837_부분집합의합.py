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

    # --------------------------------------------------------------------------------------------------
    T = int(input())

    for tc in range(1, T + 1):
        N, K = map(int, input().split())

        arr = [1, 2, 3, 4, 5, 6,
               7, 8, 9, 10, 11, 12]

        answer = 0

        def dfs(idx, count, total):
            global answer

            # 12개의 숫자를 모두 확인했을 때
            if idx == 12:
                if count == N and total == K:
                    answer += 1
                return

            # arr[idx]를 선택하는 경우
            dfs(idx + 1, count + 1, total + arr[idx])

            # arr[idx]를 선택하지 않는 경우
            dfs(idx + 1, count, total)


        dfs(0, 0, 0)

        print(f"#{tc} {answer}")