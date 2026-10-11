arr = [1,2,3]
N = len(arr)

for i in range(1<<N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(arr[j])
    print(subset)


# ------------------------------------
arr = [1,2,3]
N = len(arr)

path = []

def dfs(level):
    if level == N:
        print(path)
        return

    # 1. 현재 원소 선택
    path.append(arr[level])
    dfs(level+1)
    # 원상복구
    path.pop()
    # 2. 현재 원소 선택안함
    dfs(level+1)
dfs(0)