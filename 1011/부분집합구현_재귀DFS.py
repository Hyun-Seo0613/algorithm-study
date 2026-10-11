arr = [1,2,3]
N = len(arr)

# 현재까지 선택한 원소들을 저장할 리스트
path = []

# level: 현재 확인하고 있는 원소의 인덱스
def dfs(level):
    # 모든 원소를 확인했다면
    if level == N:
        print(path)
        return

    # 1. 현재 원소 선택
    path.append(arr[level])
    dfs(level + 1)

    # 원상복구
    path.pop()

    # 2. 현재 원소 선택하지 않음
    dfs(level + 1)

dfs(0)