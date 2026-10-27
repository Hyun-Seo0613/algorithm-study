nums = list(map(int, input().split()))
count = [0] * 100

for num in nums:
    if num == 0:
        break
    if 0 < num < 10:
        continue
    else:
        count[num//10] += 1

# 이제 출력
# 10의 자리 수는 1부터 9까지 9개이다.
for i in range(1, 10):
    print(f"{i} - {count[i]}")