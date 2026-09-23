# 정점 개수V, 간선개수 E
V, E = map(int, input().split())

# 간선 정보 입력
data = list(map(int, input().split()))

# 인접 리스트 생성
graph = [[] for _ in range(V + 1)]

# 연결 관계 저장 
for i in range(E):
    # 입력된 숫자를 두 개씩 묶기 위해서이다.
    # 서로 연결된 두 정점의 번호를 저장하는 변수.
    a = data[i * 2]
    b = data[i * 2 + 1]

    graph[a].append(b)
    graph[b].append(a)

    # 실행결과(예시)
    # graph = [
    #     [],
    #     [2],  # 1번 정점은 2번과 연결
    #     [1],  # 2번 정점은 1번과 연결
    #     [],
    #     []
    # ]

# 방문할 정점의 순서를 정렬 
# 작은 번호부터 탐색하도록 정렬
# 각 정점과 연결된 정점들을 오름차순으로 정렬하는 코드
for i in range(1, V + 1):
    graph[i].sort()

# 방문여부
visited = [False] * (V + 1)

# 스택생성
stack = [1]

# 시작 정점 방문 처리 
visited[1] = True

# 방문 순서 
answer = [1]

# DFS 시작
while stack:
    current = stack[-1]

    # 현재 정점과 연결된 정점 확인하기 
    for next_node in graph[current]:
        # 방문하지 않은 정점인지 확인하기
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
            answer.append(next_node)
            break
    else:
        stack.pop()

print(*answer)