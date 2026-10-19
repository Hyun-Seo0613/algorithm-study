T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = input()
    M = int(input())
    code = input()

    # N개의 숫자들을 앞에서부터 순서대로 입력하거나, 입력하지 않고 M개의 숫자를 맞춰야한다.
    # 보기에 주어진 N개의 숫자로 M개의 숫자를 맞출 수 있는지 판단하는 프로그램 작성

    j = 0
    answer = 0
    for i in range(N):
        if nums[i] == code[j]:
            j += 1
            if j == M:
                answer = 1
                break
    print(f"#{tc} {answer}")
