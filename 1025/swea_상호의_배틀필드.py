T = int(input())

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 전차가 바라보는 방향
tank_mark = ['^', 'v', '<', '>']

# 명령어에 따른 방향
command_direction = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3
}

for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]

    # 전차의 현재 위치와 방향 찾기
    for i in range(H):
        for j in range(W):
            if field[i][j] in tank_mark:
                ti = i
                tj = j
                direction = tank_mark.index(field[i][j])

    N = int(input())
    commands = input()

    # 명령어 처리
    for command in commands:

        # 포탄 발사
        if command == 'S':
            ni = ti + di[direction]
            nj = tj + dj[direction]

            while 0 <= ni < H and 0 <= nj < W:

                # 벽을 만난 경우
                if field[ni][nj] == '*' or field[ni][nj] == '#':

                    # 벽돌 벽이면 파괴
                    if field[ni][nj] == '*':
                        field[ni][nj] = '.'
                    break

                # 같은 방향으로 포탄 이동
                ni += di[direction]
                nj += dj[direction]

        # 전차 이동
        else:
            direction = command_direction[command]

            ni = ti + di[direction]
            nj = tj + dj[direction]

            # 이동할 위치가 범위 안이고 평지라면
            if 0 <= ni < H and 0 <= nj < W and field[ni][nj] == '.':
                field[ti][tj] = '.'
                ti = ni
                tj = nj

            # 전차 방향 표시
            field[ti][tj] = tank_mark[direction]

    # 결과 출력
    print(f"#{tc} {''.join(field[0])}")

    for i in range(1, H):
        print(''.join(field[i]))