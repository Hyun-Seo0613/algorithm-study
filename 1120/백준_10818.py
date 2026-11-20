N = int(input())
nums = list(map(int, input().split()))

max_v = nums[0]
min_v = nums[0]
for i in nums:
    if i > max_v:
        max_v = i
    if i < min_v:
        min_v = i
print(min_v, max_v)