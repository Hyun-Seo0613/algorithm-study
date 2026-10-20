T = int(input())
for tc in range(1, T+1):
    # 탑 수
    N = int(input())
    # 이동 최대 횟수
    K = int(input())
    # 각각의 탑에 돌이 얼마나 쌓여있는지
    count = list(map(int, input().split()))

    answer = 0

    # K번 이하로 돌을 움직인 후에
    # 최소 불균형도 => (최대 돌 - 최소 돌)의 최소

    # 1. 일단 어디에 가장 많이 쌓여있는지 / 적게 쌓여있는지 인덱스로 찾기
    # 2. 그다음 가장 많이 쌓여있는 탑에서 가작 적게 쌓여있는 탑으로 하나 옮기기
    # 3. 이거를 최대 K번까지 반복하면서 언제 종료하는가?(가장 바깥쪽의 for문으로 감싸서)
    #---------------------------------------------------------------------

    for _ in range(K):
        max_count = 0
        min_count = 0
        # 최대/ 최소 인덱스를 찾기 위한 반복문 1 => 인덱스는 찾았음 => 바깥에서 뭔가를 계산해야한다. 
        for i in range(N):
            if count[i] > count[max_count]:
                max_count = i
            if count[i] < count[min_count]:
                min_count = i
        
        # 종료조건 
        if count[max_count] - count[min_count] <= 1:
            break
        
        # 돌을 옮기는 행위
        count[max_count] -= 1
        count[min_count] += 1

    # 최종 불균형도
    answer = max(count) - min(count)
    print(f"#{tc} {answer}")
