T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = input()
    M = int(input())
    code = input()

    j = 0
    answer = 0

    for i in range(N):
        if nums[i] == code[j]:
            j += 1
            if j == M:
                answer = 1
                break
    print(f"#{tc} {answer}")

