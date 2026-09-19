N = int(input())
nums = list(map(int, input().split()))

# 오름차순으로 정렬
nums.sort()

# 0번부터 N-1번까지 => 중간값은 N-1//2 번 원소
mid = nums[(N-1)//2]
print(mid)