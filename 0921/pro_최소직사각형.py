# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어진다.
# 모든 명함을 수납할 수 있는 가장 작은 지갑 만들기 => 지갑의 크기 return하는 함수
# 명함의 가로 길이와 세로 길이가 담긴 sizes 2차원 배열
def solution(sizes):
    max_width = 0
    max_height = 0

    for i in range(len(sizes)):
        width = max(sizes[i][0], sizes[i][1])
        height = min(sizes[i][0], sizes[i][1])

        if width > max_width:
            max_width = width

        if height > max_height:
            max_height = height

    return max_width * max_height

