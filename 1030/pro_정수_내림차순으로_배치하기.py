# n이 매개변수로 전달되고 있기 때문에 따로 n을 입력받지 않아도 된다.
def solution(n):
    answer = []

    # 풀이 작성
    # 우선 n이 정수로 전달 -> 각 자릿수를 배열로 넣으려면 문자열로 바꾼 후 처리
    str_n = str(n)
    # answer 이라는 배열에 하나씩 넣자
    for i in range(len(str_n)):
        answer.append(int(str_n[i]))

    # 버블정렬 시작
    # 버블정렬은 배열 길이가 N이면 최대 N-1번 반복하면 된다.
    # 바깥쪽 반복문은 안쪽 반복문을 처음부터 다시 실행하는 역할
    for j in range(len(answer) - 1):
        # 이미 정렬된 부분은 제외하고 비교
        # 안쪽 반복문은 두개씩 비교
        for k in range(len(answer) -1 -j):
            if answer[k] < answer[k+1]:
                answer[k], answer[k+1] = answer[k+1], answer[k]

    # 리스트를 정수로 다시 변환
    result = ''
    for h in answer:
        result += str(h)

    return int(result)