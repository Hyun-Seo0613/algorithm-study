# 유방향
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    # 출발정점과 도착정점 입력
    S, G = map(int, input().split())

    visited = [False] * (V+1)
    
