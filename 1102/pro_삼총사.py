# 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생을 삼총사라고 부른다.
# numbers가 리스트로 주어짐

def solution(number):
    answer = 0

    # 풀이작성
    # 중첩 반복문
    # 인덱스가 i < j < k 순이 되도록 작성해야됌 => 중복 없애기 위함 (조합)
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer