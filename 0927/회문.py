T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]

    answer =""

    for i in range(N):
        for j in range(N-M+1):
            code_row = []
            for k in range(M):
                code_row.append(code[i][j+k])
            if code_row == code_row[::-1]:
                answer = ''.join(code_row)

    for j in range(N):
        for i in range(N-M+1):
            code_col = []
            for k in range(M):
                code_col.append(code[i+k][j])
            if code_col == code_col[::-1]:
                answer = ''.join(code_col)

    print(f"#{tc} {answer}")
