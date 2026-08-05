# 정수 배열 array가 매개변수로 주어질 때,
# 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    max_num = array[0]
    list_of_max_num = []
    for i in array:
        if i > max_num:
            max_num = i
    list_of_max_num.append(max_num)
    # 이부분 다시 보기
    list_of_max_num.append(array.index(max_num))

    return list_of_max_num


print(solution([1, 3, 5, 7, 9]))
