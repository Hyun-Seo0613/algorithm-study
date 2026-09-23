# 회문 : 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말
# 문자열 길이의 반만 비교하면 된다.

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [list(input()) for _ in range(N)]
    answer = ""

    # 가로 검사
    for i in range(N):
        for j in range(N-M+1):
            code_row = []

            for k in range(N):
                code_row.append(code[i][j+k])
                if code_row == code_row[::-1]:
                    print(f"#{tc}", ''.join(code_row))

    # 세로 검사
    for j in range(N):
        for i in range(N-M+1):
            code_col = []

            for k in range(N):
                code_col.append(code[i+k][j])
                if code_col == code_col[::-1]:
                    print(f"#{tc}", ''.join(code_col))

