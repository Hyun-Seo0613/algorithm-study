def dfs(s, V):
    visited = [0] * (V+1)
    stack = []

    v = s
    visited[v] = 1
    print(v, end=" ")

    while True:
       for w in graph[v]:
           if visited[w] == 0:
                stack.append(v)
                visited[w] = 1
                v = w
                print(v, end=" ")
                break
       else:
           if stack:
               v = stack.pop()
           else:
               break




V, E = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    graph[v1].append(v2)
    graph[v2].append(v1)

