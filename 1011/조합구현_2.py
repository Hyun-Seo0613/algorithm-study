# 4개의 원소에서 3개의 원소를 고르는 경우의 수 = 조합
arr = [1,2,3,4]
N = len(arr)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])

# --------------------------------------------------------
arr = [1, 2, 3, 4]
N = len(arr)

# 선택개수
R = 2

path = []

def dfs(start):

    # R개를 선택했다면
    if len(path) == R:
        print(path)
        return

    # start부터 N-1까지 탐색
    for i in range(start, N):

        # 현재 원소 선택
        path.append(arr[i])

        # 다음 원소 선택하러 이동
        dfs(i + 1)

        # 원상복구
        path.pop()


dfs(0)