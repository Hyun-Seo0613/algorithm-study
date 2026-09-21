# 두개의 행렬을 입력받아 행렬 덧셈의 결과를 반환하는 함수
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[i])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)

    return answer
