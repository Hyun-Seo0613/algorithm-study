# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸기
# N을 소수점 아래 12자리 이내인 이진수로 표현할 수 있으면 0을 제외한 나머지 숫자 출력하고,
# 13자리 이상이 필요한 경우에는 overflow 출력

T = int(input())

for tc in range(1, T+1):
    N = float(input())

    # 변환된 이진수를 저장할 리스트
    arr = []
    # 2진수 변환 과정에서 소수 부분이 0이 되었다는 것은 더 이상 변환할 숫자가 없다는 뜻
    while N != 0:
        N *= 2 # 만약 N = 0.625 였다면 1.25가 된다.

        if N >= 1:  # 2를 곱한 값이 1이상인지 검사
            arr.append(1)  # 1이상이라면 이진수 1을 리스트에 추가
            N -= 1   # 정수부분인 1을 제거한다.
        else:
            arr.append(0)  # 1보다 작으면 이진수 0을 추가한다.

        if len(arr) > 12:  # 문제 조건 13자리 이상이면 만들필요 없음 => 중단
            break

    if len(arr) > 12:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc}", end=" ")
        print(*arr, sep="")