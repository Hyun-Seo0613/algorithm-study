def solution(strings, n):
    arr = []
    answer = []

    # 문자열의 n번째 글자를 배열에 담기
    for i in strings:
        arr.append(i[n])

    # 버블정렬로 작 -> 큰 순서로 정렬
    for j in range(len(arr) - 1):
        for k in range(len(arr) - 1 - j):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

    # 반복문 -> arr의 문자와 strings의 요소의 n번째 문자가 일치하면 strins의 문자열을 answer 배열에 담기
    for h in range(len(arr)):
        for t in strings:
            if arr[h] == t[n] and t not in answer:
                answer.append(t)
    return answer