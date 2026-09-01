# N개의 정수가 들어있는 배열에서 이웃한 M개의 합 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램 작성하기

# 테스트 케이스 개수
T = int(input())

# T번 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 합을 넣어놓을 변수
    sums = []

    # 몇번반복을 해야하는가? -> 10개의 숫자, 3개합이면 8번 => N - M + 1
    for i in range(N-M+1):
        current_sum = sum(numbers[i:i+M])
        sums.append(current_sum)

    # max, min 안쓰고 하는 방법도 따로 해보기
    answer = max(sums) - min(sums)

    print(f"#{tc} {answer}")



