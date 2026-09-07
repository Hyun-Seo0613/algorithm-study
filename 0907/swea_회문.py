T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    text = [input() for _ in range(N)]

    answer = ""

    for i in range(N):
        for j in range(N - M + 1):

            # 가로 방향
            for k in range(M // 2):
                if text[i][j + k] != text[i][j + M - 1 - k]:
                    break
            else:
                answer = text[i][j:j + M]

            # 세로 방향
            for k in range(M // 2):
                if text[j + k][i] != text[j + M - 1 - k][i]:
                    break
            else:
                answer = ""

                for l in range(M):
                    answer += text[j + l][i]

    print(f"#{tc} {answer}")