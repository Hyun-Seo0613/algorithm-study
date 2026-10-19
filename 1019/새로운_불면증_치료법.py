# 양세기
# N, 2N, ... kN
# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지 모든 숫자를 보는 것은 최소 몇 번 양을 센 지점일지

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 0~9
    count = [0] * 10
    k = 1
    while True:
        num = N * k

        for i in str(num):
            count[int(i)] = 1
        if sum(count) == 10:
            break
        k += 1
    print(f"#{tc} {num}")
