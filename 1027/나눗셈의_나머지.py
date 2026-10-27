A, B = map(int, input().split())
# A를 B로 나눈 몫을 A에 계속해서 저장하는 것을 반복하는 코드

# 어떤 양의 정수를 B로 나누면 나머지는 항상 0부터 B-1까지 나오기 때문.
count = [0] * B
while A > 1:
    # 나머지
    i = A % B

    # 나머지가 등장한 한 횟수
    count[i] += 1

    # 그 몫인데 계속 다시 저장이 될 거임
    A = A // B

# 출력하자
answer = 0
for i in count:
    answer += i ** 2

print(answer)


