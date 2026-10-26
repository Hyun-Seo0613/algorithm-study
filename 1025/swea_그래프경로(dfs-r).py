T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 1. 인접 리스트 생성
    Graph = [[] for _ in range(V+1)]

    # 2. 간선 정보 입력 (방향 그래프)
    for i in range(E):
        v1, v2 = map(int, input().split())
        Graph[v1].append(v2)

    # 3. 출발 정점과 도착 정점 입력
    S, G = map(int, input().split())

    # 4. 방문 배열 초기화
    visited = [0] * (V+1)

    # 5. DFS 함수 작성
    def dfs(v):
        visited[v] = 1
        for w in Graph[v]:
            if visited[w] == 0:
                dfs(w)

    # 6. 출발 정점부터 DFS 실행
    dfs(S)

    # 7. 도착 정점 방문 여부 출력
    answer = visited[G]

    print(f"#{tc} {answer}")