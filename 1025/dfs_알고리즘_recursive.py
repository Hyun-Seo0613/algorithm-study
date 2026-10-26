# DFS - recursive
# 정점과 간선 개수
V, E = map(int, input().split())
Graph = [[] for _ in range(V+1)]

# 간선정보 입력하기
for i in range(E):
    v1, v2 = map(int, input().split())
    # 무방향 그래프
    Graph[v1].append(v2)
    Graph[v2].append(v1)

# 방문 배열 초기화하기
visited = [0] * (V+1)

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    # 그 정점과 연결된 것들도 반복문으로 처리하기
    for w in Graph[v]:
        if visited[w] == 0:
            dfs(w)

dfs(1)
