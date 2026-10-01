# 퀵 정렬
# pivot을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 보낸다.

def partition(A, l, r):
    # 가장 왼쪽 값을 pivot으로 설정
    p = A[l]

    # 왼쪽에서 오른쪽으로 이동할 인덱스
    i = l

    # 오른쪽에서 왼쪽으로 이동할 인덱스
    j = r

    # i와 j가 교차할 때까지 반복
    while i <= j:

        # 왼쪽에서 pivot보다 큰 값 찾기
        while i <= j and A[i] <= p:
            i += 1

        # 오른쪽에서 pivot보다 작은 값 찾기
        while i <= j and A[j] >= p:
            j -= 1

        # 아직 i와 j가 교차하지 않았다면
        # 잘못된 위치에 있는 두 값 교환
        if i < j:
            A[i], A[j] = A[j], A[i]

    # i와 j가 교차하면
    # pivot과 j 위치의 값을 교환
    A[l], A[j] = A[j], A[l]

    # pivot의 확정된 위치 반환
    return j


def quick_sort(A, l, r):
    # 원소가 2개 이상일 때만 정렬
    if l < r:

        # partition을 통해 pivot의 위치 확정
        p = partition(A, l, r)

        # pivot 왼쪽 부분 정렬
        quick_sort(A, l, p - 1)

        # pivot 오른쪽 부분 정렬
        quick_sort(A, p + 1, r)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    # 0번 인덱스부터 N-1번 인덱스까지 퀵 정렬
    quick_sort(A, 0, N - 1)

    # 정렬된 배열의 가운데 값
    answer = A[N // 2]

    print(f"#{tc} {answer}")