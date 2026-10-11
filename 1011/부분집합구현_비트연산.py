arr = [1, 2, 3]
N = len(arr)

# 1 << N = 2 ** N
for i in range(1 << N):
    subset = []

    for j in range(N):
        # 현재 부분집합에서 j번째 원소를 선택해야 하는지 확인하고, 선택해야 한다면 리스트에 추가하는 코드
        # 결과가 0이 아니면 arr[j]를 부분집합에 포함시키고, 0이면 포함시키지 않는다. 
        if i & (1 << j):
            subset.append(arr[j])

    print(subset)