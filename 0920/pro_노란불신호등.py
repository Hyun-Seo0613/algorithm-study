import math
# 프로그래머스에서는 내가 직접 입력을 받지는 않는다.
# 신호등 n개의 신호 주기를 담은 2차원 정수배열 signals가 매개변수로 주어진다.
# 모든 신호등이 노란불이 되는 가장 빠른 시각을 return 하도록 solution 함수를 완성하기
# 만약 모든 신호등이 노란불이 되는 경우가 존재하지 않으면 -1 return

# 주기 구해서 노란불이 오는 시간을 구할 수 있음
# 전체 패턴이 다시 처음으로 돌아오는 시점은 각 신호등 주기의 최소공배수

# 모든 신호등의 패턴이 반복되는 최대 시간 max_time 구한다.
# 1초 ~ max_time 초 까지 하나씩 확인한다.
# 그 시간에 모든 신호등이 노란불이면 바로 return t
# 끝까지 없으면 -1

def solution(signals):
    # 각 신호등의 주기의 최소공배수 구하기 => 1초부터 어디까지 반복문 돌릴지 구해야함
    max_time = 1

    for i in range(len(signals)):
        G = signals[i][0]
        Y = signals[i][1]
        R = signals[i][2]

        cycle = G + Y + R
        max_time = math.lcm(max_time, cycle)

    # 1초부터 max_time까지 확인하기
    for t in range(1, max_time + 1):
        # 일단 모든 신호등이 노란불이라 하자
        all_yellow = True

        # 신호등 하나씩 확인하기
        for i in range(len(signals)):
            G = signals[i][0]
            Y = signals[i][1]
            R = signals[i][2]

            cycle = G + Y + R

            current = (t - 1) % cycle

            # 만약 노란불이 아니라면
            if not (G <= current < G + Y):
                all_yellow = False
                break

        # 전부 노란불이면
        if all_yellow:
            return t

    return -1







