T = int(input())
for tc in range(1, T+1):
    # K : 한 번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 총 정류장 수
    # M : 충전기가 있는 정류장 수
    K, N, M = map(int, input().split())
    # 충전 가능한 정류소 번호
    chargers = list(map(int, input().split()))

    # 충전횟수
    count = 0
    # 현재 위치
    current = 0

    # 종점에 도달하지 못하면 계속 반복한다 -> 다음 충전기가 어딨는지 못찾았다고 두고
    # 아래의 반복문에서 그걸 찾기
    while current+K < N:
        next_stop = -1

        for i in range(current +K, current, -1):
            if i in chargers:
                next_stop = i
                break
        # 충전기를 못 찾으면 종점까지 갈 수 없다
        if next_stop == -1:
            count = 0
            break

        current = next_stop
        count += 1
    print(f"#{tc} {count}")



