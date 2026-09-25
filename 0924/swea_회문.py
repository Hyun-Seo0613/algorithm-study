# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 2차원 배열로 입력받음
    code = [list(input()) for _ in range(N)]
    answer = ''

    # 가로 검사
    for i in range(N):
        # 몇번째 열부터 회문검사를 할건지
        for j in range(N-M+1):
            code_row = []
            # k: 이동거리
            for k in range(M):
                code_row.append(code[i][j+k])

            if code_row == code_row[::-1]:
                answer = ''.join(code_row)

    # 세로 검사
    for j in range(N):
        for i in range(N-M+1):
            code_col = []

            for k in range(M):
                code_col.append(code[i+k][j])

            if code_col == code_col[::-1]:
                answer = ''.join(code_col)

    print(f"#{tc} {answer}")














