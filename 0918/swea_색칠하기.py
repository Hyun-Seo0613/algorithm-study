T = int(input())

for tc in range(1, T+1):
    # 칠할 영역의 개수
    N = int(input())

    # 10 X 10 격자
    paper = [[0] * 10 for _ in range(10)]

    # 정답 purple 이 칠해진 영역 수
    purple = 0

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        # 색칠하기
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 0: 흰색, 1: 빨강, 2: 파랑, 3:보라(1+2)
                paper[i][j] += color

                if paper[i][j] == 3:
                    purple += 1
    print(f"#{tc} {purple}")

