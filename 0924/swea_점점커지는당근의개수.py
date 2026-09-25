# 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램을 만드시오. 연속으로 커지지않는 경우 구간의 최소 길이는 1이다.
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 당근의 크기가 N개의 정수로 주어짐
    C = list(map(int, input().split()))

    # 당근 크기가 연속으로 증가하는 경우가 있고 그렇지 않은 경우가 있음
    # 증가하면 answer += 1, 증가하지 않으면 다시 count = 1
    count = 1
    answer = 1

    for i in range(1, len(C)):
        if C[i-1] < C[i]:
            count += 1
        else:
            count = 1
        answer = max(answer, count)

    print(f"#{tc} {answer}")


