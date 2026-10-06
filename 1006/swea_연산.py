# +1, -1. *2. -10 네개의 연산으로 N -> M
# 최소연산횟수를 구해야하기 때문에 큐를 쓴다.

# N를 Queue에 넣음 
# Queue에서 하나 꺼냄
# 현재 숫자 v에서 갈 수 있는 v+1, v-1, v*2, v-10을 확인 
# 방문하지 않은 숫자를 Queue에 넣음 
# Queue에서 다음 숫자 꺼냄
# 반복하기

def bfs(N, M):
    visited = [0] * 1000001
    q = [0] * 1000001
    front = -1
    rear = -1

    # 시작 정점 삽입
    rear += 1
    q[rear] = N

    visited[N] = 1

    while front != rear:
        #dequeue
        front += 1
        v = q[front]

        if v == M:
            return visited[v] - 1

        next_list = [v+1, v-1, v*2, v-10]

        for w in next_list:
            if 1 <= w <= 1000000 and visited[w] == 0:
                # 몇번의 연산으로 w까지 왔는지 기록
                visited[w] = visited[v] + 1

                # enqueue
                rear += 1
                q[rear] = w

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = bfs(N, M)
    print(f"#{tc} {answer}")