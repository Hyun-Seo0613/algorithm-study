# 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬
# 대문자는 소문자보다 작은 것으로 간주한다.

def solution(s):
    answer = []
    
    # 우선 문자열을 배열에 넣어놓고
    for j in range(len(s)):
        answer.append(s[j])

    # 버블정렬 알고리즘
    for i in range(len(s) - 1):
        for j in range(len(s) - 1 - i):
            if answer[j] < answer[j+1]:
                answer[j], answer[j+1] = answer[j+1], answer[j]
    result = ''.join(answer)
    
    return result