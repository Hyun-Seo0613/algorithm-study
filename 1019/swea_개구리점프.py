# N : 물웅덩이의 길이
# K : 개구리가 점프할 수 있는 최대 거리 , 뛸 수 있는 나뭇잎 없어도 무조건 뜀
# 물 웅덩이의 가장 왼쪽에는 나뭇잎이 있음, 거기서 개구리가 점프를 시작

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 개구리의 현재위치
    pos = 0
    # 개구리가 물웅덩이 끝에 도착할때까지 반복
    while pos < N -1:
        found = False

        for i in range(pos + K, pos, -1):
            if i >= N:
                continue

            if arr[i] == 1:
                pos = i
                found = True
                break  # 짜피 먼곳에서부터 찾는거니까

        # 점프할 수 있는 나뭇잎이 없다면
        if found == False:
            pos = min(pos+K, N-1)
            break
    print(f"#{tc} {pos + 1}")











