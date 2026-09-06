# 양쪽 거리 2 이상의 공간이 확보될 때 조망권이 확보된다.
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대수 반환하는 프로그램 작성

# 변수 => 현재 빌딩, 주변에서 가장 높은 빌딩

# Test Case 수
T = 10

for tc in range(1, T + 1):
    # 건물 개수 N
    N = int(input())
    # N개의 건물 높이
    heights = list(map(int, input().split()))

    # 조망권 세대 수
    count = 0
    # 현재 내가 있는 곳과 주변 건물의 높이를 비교해서 조망권 확보 가능한지 확인
    # 양쪽 2개씩은 비어있으므로
    for i in range(2, N-2):
        max_height = max(
            heights[i-2],
            heights[i-1],
            heights[i+1],
            heights[i+2]
        )
        # 만약 현재 빌딩이 가장높은 주변빌딩보다 높다면 층 수 차이가 조망권 확보 수
        if heights[i] > max_height:
            count += (heights[i] - max_height)

    print(f"#{tc} {count}")


