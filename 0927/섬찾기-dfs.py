T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(input()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    answer = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if ground[i][j] == "L" and visited[i][j] == 0:
                answer += 1

                stack = [(i, j)]
                visited[i][j] = 1

                while stack:
                    x, y = stack.pop()

                    for d in range(4):
                        nx = x + di[d]
                        ny = y + dj[d]

                        if 0 <= nx < N and 0<= ny < M:
                            if ground[nx][ny] == "L" and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                stack.append((nx, ny))
