T = int(input())

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 왼쪽, 오른쪽 회전 후 방향
left = [2, 3, 1, 0]
right = [3, 2, 0, 1]

for tc in range(1, T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]

    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                si = i
                sj = j

    Q = int(input())
    answer = []

    for _ in range(Q):
        C, commands = input().split()

        # 명령어마다 시작 위치와 방향 초기화
        i = si
        j = sj
        direction = 0  # 처음에는 위쪽

        for command in commands:

            # 왼쪽 회전
            if command == 'L':
                direction = left[direction]

            # 오른쪽 회전
            elif command == 'R':
                direction = right[direction]

            # 앞으로 이동
            elif command == 'A':
                ni = i + di[direction]
                nj = j + dj[direction]

                # 범위 안이고 나무가 없는 경우 이동
                if 0 <= ni < N and 0 <= nj < N:
                    if field[ni][nj] != 'T':
                        i = ni
                        j = nj

        # 목적지 도착 여부
        if field[i][j] == 'Y':
            answer.append(1)
        else:
            answer.append(0)

    print(f"#{tc} {' '.join(map(str, answer))}")