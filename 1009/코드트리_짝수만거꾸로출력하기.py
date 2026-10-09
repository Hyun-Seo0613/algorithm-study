N = int(input())
nums = list(map(int, input().split()))
even_num = []

for num in nums:
    if num % 2 == 0:
        even_num.append(num)

for i in range(len(even_num)-1, -1, -1):
    print(even_num[i], end=" ")
