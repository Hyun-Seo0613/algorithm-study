N, Q = map(int, input().split())
# N개의 원소값이 주어진다
nums = list(map(int, input().split()))

# Q개의 줄에 걸쳐 Q개의 질의(문자열로 받을지, 정수로 받을지?)가 한 줄에 하나씩 차례대로 주어진다
for _ in range(Q):
    # i번째 줄에는 i번째 질의가 주어진다.
    # 질의 입력
    # 1 4 => 4번째 원소를 출력한다.
    q = list(map(int, input().split()))
    if q[0] == 1:
        print(nums[q[1] - 1])

    elif q[0] == 2:
        # N개의 원소 중 값이 b인 원소를 찾아 그 값의 인덱스 출력하기
        arr = []

        for i in range(N):
            if nums[i] == q[1]:
                arr.append(i+1)
        if arr:
            answer = min(arr)
        else:
            answer = 0
        print(answer)


    elif q[0] == 3:
        for i in range(q[1] - 1, q[2]):
            print(nums[i], end=" ")
        print()




