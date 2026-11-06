def solution(sizes):
    answer = 0

    # sizes는 2차원 배열
    # sizes[i][0] 을 긴 길이/ sizes[i][1]을 짧은 길이로 만들고
    max_width = 0
    max_height = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

        if sizes[i][0] > max_width:
            max_width = sizes[i][0]
        if sizes[i][1] > max_height:
            max_height = sizes[i][1]
    answer = max_width * max_height

    return answer
