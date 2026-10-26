V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (V+1)

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)
        print(t, end=" ")

        for w in graph[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
bfs(1)