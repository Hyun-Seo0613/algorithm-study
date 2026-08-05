############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 별도 라이브러리 없이 구현합니다.


# 자율비행 드론이 격자 형태의 구역을 비행합니다
# 구역은 2 차원 리스트 grid 로 주어지며 , 값이 0 이면 비행 가능 , 1 이면 장애물입니다
# 드론은 시작 위치 start = (row, col) 에서 출발하여 처음에는 위쪽 상 을 바라봅니다
# 이동 명령 문자열 commands 가 주어질 때 , 모든 명령을 수행한 후
# 드론의 최종 위치 (row,col) 를 튜플 형태 로 반환하는 simulate_drone 함수를 완성하시오
# 명령어 규칙
# 방향 및 좌표 규칙 ] 격자는 0 indexed, row 는 위에서 아래로 증가
# 상 Up): row 1
# 하 Down): row + 1
# 좌 Left): col 1
# 우 Right): col + 1
# 전진 제약
# 전진하려는 칸이 격자 범위를 벗어나거나 장애물 ( 이면 , 그 전진 명령은 무시합니다 .
# 제자리 유지 , 방향도 그대로
def simulate_drone(grid, start, commands):
    # 상, 우, 하, 좌
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상  # 우  # 하  # 좌

    row, col = start

    # 처음에는 위쪽을 바라보므로 directions의 0번
    direction = 0

    for command in commands:
        # 왼쪽 회전
        if command == "L":
            direction = (direction - 1) % 4

        # 오른쪽 회전
        elif command == "R":
            direction = (direction + 1) % 4

        # 전진
        elif command == "F":
            dr, dc = directions[direction]

            next_row = row + dr
            next_col = col + dc

            # 격자 범위 안이고 장애물이 아닐 때만 이동
            if (
                0 <= next_row < len(grid)
                and 0 <= next_col < len(grid[0])
                and grid[next_row][next_col] == 0
            ):
                row = next_row
                col = next_col

    return (row, col)


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
# grid: 0 = 비행 가능, 1 = 장애물
# 시작 방향은 위쪽(상), 좌표는 (row, col), R=시계/L=반시계 회전
# 전진하려는 칸이 격자 밖이거나 장애물이면 그 전진 명령은 무시
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# 1) (0,0) 상 -> F: 위는 격자 밖 -> 무시
# 2) R -> 우를 봄
# 3) F: (0,1) 이동 / 4) F: (0,2) 이동
print(simulate_drone(grid, (0, 0), "FRFF"))  # (0, 2)
# 1) (2,1) 상 -> F: (1,1) 장애물 -> 무시
# 2) R -> 우 / 3) F: (2,2) 이동 / 4) F: (2,3) 격자 밖 -> 무시
print(simulate_drone(grid, (2, 1), "FRFF"))  # (2, 2)
#####################################################
