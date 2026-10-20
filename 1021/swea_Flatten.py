# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다
# 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이 반환

T = 10
for tc in range(1, T+1):
    # 제한된 덤프 횟수
    N = int(input())
    # 각 상자의 높이값
    height = list(map(int, input().split()))
    answer = 0

    # 2. 최대 N번까지 반복하니까 바깥 반복문 안에 넣기
    for _ in range(N):
        # 1. 가장 높은 곳과 가장 낮은 곳의 인덱스 찾기
        max_count = 0
        min_count = 0
        for i in range(len(height)):
            if height[i] > height[max_count]:
                max_count = i
            if height[i] < height[min_count]:
                min_count = i
        # 3. N번까지 안해도될 수도 있으므로 종료조건
        if height[max_count] - height[min_count] <= 1:
            break

        # 4. 상자 옮기는 작업 (개수 조정)
        height[max_count] -= 1
        height[min_count] += 1

    # 5. 모든 반복문에서 나와서 (모든 작업이 끝난 후) 계산
    answer = max(height) - min(height)
    print(f"#{tc} {answer}")


