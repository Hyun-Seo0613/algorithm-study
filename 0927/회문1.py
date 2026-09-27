T = 10

for tc in range(1, T+1):
    N = int(input())
    code = [list(input()) for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8-N+1):
            code_row = []
            for k in range(N):
                code_row.append(code[i][j+k])
            if code_row == code_row[::-1]:
                count += 1
    for j in range(8):
        for i in range(8-N+1):
            code_col = []
            for k in range(N):
                code_col.append(code[i+k][j])
            if code_col == code_col[::-1]:
                count += 1

    print(f"#{tc} {count}")
