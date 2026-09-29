# 현재 방번호: now
# 내가 지금까지 들른 방번호 모음: visited
# 내가 지금까지 사용한 에너지 사용량:e

def solve(now, visited, e):
    global answer
    # 종료조건
    if len(visited) == N:
        # e가 최소인지 확인
        e += Energy[now][0]
        # 최소 에너지 갱신
        answer = min(answer, e)
        return
    
    # 재귀호출
    # 내가 지금까지 들린적 없는 방 구역 선택해서 이동
    for i in range(N):
        # 내가 i번 구역을 간적이 없다면
        if i not in visited:
            # i번 구역으로 이동, i번 방문 목록에 추가, now -> i에너지 사용량 더하기
            solve(i, visited + [i], e + Energy[now][i])
            # i를 내가 지금까지 들른 방번호 모음에 제거


    

T = int(input())

for tc in range(1, T+1):
    # 구역의 개수
    N = int(input())

    # 이동하면서 사용하는 배터리 양
    # Energy[i][j] => i번 구역에서 j번 구역으로 가는데 소비하는 에너지 양
    # Energy[i][j] != Energy[j][i] 
    Energy = [list(map(int, input().split())) for _ in range(N)]
    answer = 1000000
    solve(0, [0], 0)
    print(f"#{tc} {answer}")




