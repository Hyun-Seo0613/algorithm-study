arr = [1, 2, 3]

visited = [False] * 3
path = []

def perm():
    # 숫자 3개를 모두 선택한다면
    if len(path) == 3:
        print(path)
        return

    for i in range(3):
        # 이미 사용한 숫자라면 건너뛰기
        if visited[i]:
            continue

        # 숫자 선택
        visited[i] = True
        path.append(arr[i])

        # 다른 숫자 선택
        perm()

        # 선택 취소
        path.pop()
        visited[i] = False
perm()