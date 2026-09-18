# 완전탐색
# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # N x N 배열 - 파리 마리 수가 적힌 2차원 배열 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대로 죽일 수 있는 파리 수
    answer = 0

    # 배열 안 검사
    # 파리채를 어디에 놓을지 결정 -> 놓은 파리채 안의 칸들 검사
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for ni in range(i, i+M):
                for nj in range(j, j+M):
                    fly += arr[ni][nj]
            answer = max(fly, answer)
    print(f"#{tc} {answer}")





