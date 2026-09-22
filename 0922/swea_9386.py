T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = input()

    # 현재 몇개 연속인지
    count = 0
    # 최대로 연속된게 몇개인지
    answer = 0

    for i in range(N):
        if C[i] == "1":
            count += 1
            answer = max(answer, count)
        else:
            count = 0
    print(f"#{tc} {answer}")

