# 첫째항과 두번째항은 주어짐
nums = list(map(int, input().split()))
# 세번째항부터 계산해서 nums에 추가
for i in range(2, 10):
    nums.append((nums[i-2] + nums[i-1]) % 10)
print(*nums)