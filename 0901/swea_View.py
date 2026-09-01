# 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2이상의 공간이 확보될 때 조망권 확보
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수 반환 프로그램 작성

# 10개의 테스트 케이스
T = 10

for tc in range(1, T+1):
    # N개의 건물 개수
    N = int(input())

    # N개의 건물 높이 # 맨 왼쪽과 맨 오른쪽 두칸에 있는 건물은 항상 높이0
    height = list(map(int, input().split()))

    # 조망권 수
    answer = 0
    # 반복문 -> 현재 건물 기준으로 왼쪽 2개,오른쪽 2개 높이 비교
    for i in range(2, N-2):
        # 현재 건물 주변 4개중 가장 높은 건물이
        max_height = max(
            height[i - 2],
            height[i - 1],
            height[i + 1],
            height[i + 2],
        )

        # 현재 건물이 주변 건물보다 높으면 조망권 확보
        # 현재 건물 높이에서 주변건물 중 가장 높은 것의 차이만큼 조망권 확보
        if height[i] > max_height:
            answer += height[i] - max_height

    print(f"#{tc} {answer}")



