arr = [1,2,3]
N = len(arr)

for i in range(1<<N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(arr[j])
    print(subset)