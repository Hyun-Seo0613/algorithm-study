arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):
    subset_sum = 0

    for j in range(n):
        if i & (1 << j):
            subset_sum += arr[j]
    print(subset_sum)