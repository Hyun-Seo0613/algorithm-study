T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 컨테이너마다 실린 화물의 무게
    weight = list(map(int, input().split()))
    # 트럭마다의 적재용량
    trucks = list(map(int, input().split()))

    # 큰 -> 작 순서
    weight.sort(reverse=True)
    trucks.sort(reverse=True)

    answer = 0
    # 현재 확인할 트럭 번호
    current = 0

    for truck in trucks:
        # 현재 컨테이너가 트럭보다 무거우면
        # 해당 컨테이너는 포깋고 다음 컨테이너 확인하기
        while current < N and weight[current] > truck:
            current += 1

        # 모든 컨테이너를 확인햇다면 종료
        if current == N:
            break

        # 현재 트럭에 컨테이널르 실기 
        answer += weight[current]

        # 사용한 컨테이너 처리
        current += 1

    print(f"#{tc} {answer}")

