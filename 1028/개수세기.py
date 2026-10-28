N, M = map(int, input().split())
nums = list(map(int, input().split()))

# N개의 정수중에 M이 몇번 등장하는지 세기
cnt = 0
for i in range(N):
    if nums[i] == M:
        cnt += 1
print(cnt)
