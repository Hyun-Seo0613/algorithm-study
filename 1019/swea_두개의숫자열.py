T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_i = list(map(int, input().split()))
    B_j = list(map(int, input().split()))

    # 무조건 A_i가 더 짧은 숫자열이 되도록 만들어 놓기
    if N > M:
        A_i, B_j = B_j, A_i
        N, M = M, N
    answer = 0

    # 두개의 반복문 필요
    # 짧은 숫자열을 한칸씩 이동시킬 반복문
    # 마주보는 것끼리 곱할 반복문

    for i in range(M - N + 1):
        total = 0
        for j in range(N):
            total += A_i[j] * B_j[j + i]
        answer = max(answer, total)
    print(f"#{tc} {answer}")
