import math

# 주기 내에서 현재위치, 주기, ..
def solution(signals):
    max_time = 1

    for i in range(len(signals)):
        G = signals[i][0]
        Y = signals[i][1]
        R = signals[i][2]

        cycle = G + Y + R
        max_time = math.lcm(max_time, cycle)

    for time in range(1, max_time+1):
        all_Y = True

        for i in range(len(signals)):
            G = signals[i][0]
            Y = signals[i][1]
            R = signals[i][2]

            cycle = G + Y + R

            # 주기 내에서 현재위치
            current = (time - 1) % cycle

            if not G <= current < G + Y:
                all_Y = False
                break
        if all_Y:
            return time

    return -1





