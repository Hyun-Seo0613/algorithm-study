def solve(count):
    global answer

    # 현재 숫자 상태
    state = ''.join(numbers)

    if state in visited[count]:
        return

    visited[count].add(state)

    if count == change:
        num = int(''.join(numbers))
        answer = max(answer, num)
        return

    # 서로 다른 자리 선택하기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # 바꾸기
            numbers[i], numbers[j] = numbers[j], numbers[i]

            solve(count + 1)

            # 다시 되돌리기
            numbers[i], numbers[j] = numbers[j], numbers[i]



T = int(input())

for tc in range(1, T+1):
    # 숫자판의 정보와 교환 횟수
    num, change = input().split()

    # 자리교환하기 위해서 리스트로 
    numbers = list(num)
    change = int(change)

    answer = 0

    # 같은 교환 횟수에서 같은 숫자 상태를 이미 봤으면 다시 탐색 x
    visited = [set() for _ in range(change+1)]  # 교환 횟수별로 방문한 숫자 상태 저장하도록
    solve(0)

    print(f"#{tc} {answer}")