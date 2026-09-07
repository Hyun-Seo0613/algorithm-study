# 종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.
# 예를 들어서 풍선에 든 꽃가루가 1개씩일때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날린다.
# N x M 개의 풍선에 들어있는 종이 꽃가루 개수 A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램
# 다 터뜨려봐야 알 수 있음

T = int(input())

# 델타탐색 방향 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 꽃가루 개수가 들어있는 2차원 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답 -> 합의 최댓값
    answer = 0

    # 모든 풍선을 하나씩 확인
    for i in range(N):
        for j in range(M):
            # (i, j) 위치에서 풍선 터뜨린 후 꽃가루 개수만큼 상하좌우 +
            # 이 위치에서 꽃가루 합
            cnt = arr[i][j]

            # 상하좌우로 뻗어나갈 길이 k의 범위는 (1, j) 위치의 꽃가루 개수만큼
            for k in range(1, cnt + 1):
                # 상하좌우 4방향 델타탐색
                for d in range(4):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k
                    # 계산한 다음 위치가 인덱스 범위 안인지 확인
                    if 0 <= ni < N and 0<= nj < M:
                        cnt += arr[ni][nj]
            answer = max(answer, cnt)
    print(f"#{tc} {answer}")


