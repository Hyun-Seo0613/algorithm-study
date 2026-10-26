T = 10

for tc in range(1, T+1):
    test_case, count = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    for i in range(0, len(nums), 2):
        v1 = nums[i]
        v2 = nums[i+1]
        graph[v1].append(v2)

    # S, G = map(int, input().split())
    visited = [0] * 100

    def dfs(v):
        visited[v] = 1
        for w in graph[v]:
            if visited[w] == 0:
                dfs(w)
    dfs(0)
    answer = visited[99]
    print(f"#{test_case} {answer}")