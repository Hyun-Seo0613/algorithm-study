arr = []

for i in range(9):
    num = int(input())
    arr.append(num)

max_v = arr[0]
max_idx = 1

for j in range(len(arr)):
    if arr[j] > max_v:
        max_v = arr[j]
        max_idx = j + 1

print(max_v)
print(max_idx)