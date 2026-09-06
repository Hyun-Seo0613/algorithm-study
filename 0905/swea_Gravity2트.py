# 24735 Gravity

# 상자들이 쌓여 있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다.
# 낙차가 가장 큰 상자를 구하여 낙차를 출력하는 프로그램 작성

# 상자가 놓인 가로 칸의 수
N = int(input())
# 각 칸의 상자 높이
heights = list(map(int, input().split()))

# 가장 높이가 큰 상자 찾기
# 낙차
answer = 0

# 가장 높은 거 찾기
for i in range(N):
    count = 0
    for j in range(i+1, N):
        if heights[i] > heights[j]:
            count += 1
            answer = max(answer, count)

print(answer)

