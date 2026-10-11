def bfs(s, V):
    visited = [0] * (V+1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)
        print(t)
        for w in graph[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    # print(visited) # 방문 순서만 요구한다면 필요없음
V, E = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
bfs(1, V)