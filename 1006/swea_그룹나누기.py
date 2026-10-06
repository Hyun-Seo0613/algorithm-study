def dfs(v):
    for w in graph[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(w)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    # M 쌍의 신청서 입력
    arr = list(map(int, input().split()))

    for i in range(M):
        a = arr[i*2]
        b = arr[i*2+1]

        # 무방향
        graph[a].append(b)
        graph[b].append(a)

    # 방문 배열
    visited = [0] * (N+1)

    answer = 0

    # 1번 사람부터 N번까지 확인
    for v in range(1, N+1):
        if not visited[v]:
            visited[v] = 1

            # 해당 사람과 같은 조인 사람들 모두 탐색하기
            dfs(v)

            # DFS 한번이 하나의 조
            answer += 1
    print(f"#{tc} {answer}")
