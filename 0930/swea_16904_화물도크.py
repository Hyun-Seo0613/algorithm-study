T = int(input())
for tc in range(1, T+1):
    N = int(input())

    work = []

    for _ in range(N):
        s, e = map(int, input().split())
        work.append((s, e))

    # 종료 시간이 빠른 순서로 정렬하기
    # 각 튜플의 두 번째 값 x[1]을 기준으로 오름차순 정렬하기 
    work.sort(key=lambda x: x[1])
    
    # 화물차 선택 개수
    count = 0
    end_t = 0

    # 현재 작업 시작시간이 이전의 작업 종료시간보다 같거나 늦으면 작업이 가능하다.
    for s,e in work:
        if s >= end_t:
            
            # 현재 작업 선택하고
            count += 1
            # 현재 작업 종료 시간을 다음 비교를 위해 저장하기
            end_t = e
    print(f"#{tc} {count}")