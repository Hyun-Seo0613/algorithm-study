# A, B 두명에게 같은 코드를 반복해야하므로 함수로 만들어서 호출하는 방식으로
def binary_search(P, target):
    left = 1
    right = P
    count = 0

    while True:
        # 가운데 페이지
        mid = (left+right) // 2
        count += 1

        # 찾고 싶은 페이지를 찾았다면 종료
        if mid == target:
            return count

        # 찾는 페이지가 가운데보다 오른쪽에 있는 경우
        elif mid <= target:
            left = mid

        # 찾는 페이지가 가운데보다 왼쪽에 있는 경우
        else:
            right = mid

# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    P, P_A, P_B = map(int, input().split())

    A_count = binary_search(P, P_A)
    B_count = binary_search(P, P_B)

    if A_count < B_count:
        answer = "A"
    elif A_count > B_count:
        answer = "B"
    else:
        answer = 0

    print(f"#{tc} {answer}")





