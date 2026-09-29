# 각 칸에서 오른쪽이나 아래로만 이동할 수 있다 => 재귀 떠올라야함

di = [0, 1]
dj = [1, 0]

# 범위 검사
def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N

# 재귀함수 만들기
# i, j : 현재 내 위치 행번호, 열번호 (재귀 단계를 나타낸다.)
# now_sum: 현재까지 내가 거쳐온 칸들에 적혀있던 숫자의 합
def solve(i, j, now_sum):
    global answer
    # 기저 조건: 맨 오른쪽 아래에 도착시 종료
    if (i, j) == (N-1, N-1):
        answer = min(answer, now_sum)
        return

    # 재귀호출
    # 다음 단계로 갈때 선택가능한 경우의 수 2가지(오른쪽, 아래)
    # d:0 오른쪽 / d:1 아래
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]
        if is_valid(ni, nj):
            # 다음 단계로
            # 다음 위치로 이동하면서 다음 위치에 있는 숫자 더하기
            solve(ni, nj, now_sum + matrix[ni][nj])
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답: 최소 합
    answer = 10000

    # 맨 왼쪽 위에서 출발,
    solve(0, 0, matrix[0][0])

    print(f"#{tc} {answer}")