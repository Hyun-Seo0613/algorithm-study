T = int(input())

for tc in range(1, T+1):
    # 문자열로 받아서 반복문 돌리기
    N = int(input())

    # 등장한 숫자 기록하기로 ㄱㄱ

    # 0~9까지 총 10개의 숫자가 한번씩 나오면 ㄱㄴ
    count = [0] * 10

    k = 1

    # 계속 반복하다가 count 의 합이 10이되면 바로 종료
    while True:
        num = N * k

        for i in str(num):
            count[int(i)] = 1

        if sum(count) == 10:
            break

        k += 1

    print(f"#{tc} {num}")





