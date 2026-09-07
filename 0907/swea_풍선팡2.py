T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 꽃가루가 들어있는 2차원 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대값을 저장할 변수
    answer = 0

    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0<= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            answer = max(answer, cnt)
    print(f"#{tc} {answer}")




