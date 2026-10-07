nums = list(map(int, input().split()))

# 250의 정수가 주어지면 마지막 으로 주어진 수 제외하고 나머지 정수들의 합계와 평균을 구하기
# 250 이 없으면 10개의 합계와 평균을 계산

total = 0
count = 0

for num in nums:
    if num >= 250:
        break

    # 250 미만일때만 실행되는 코드
    total += num
    count += 1

avg = total / count

print(f"{total} {avg:.1f}")