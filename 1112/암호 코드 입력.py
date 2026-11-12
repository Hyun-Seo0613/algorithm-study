T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    code = list(map(int, input().split()))

    j = 0
    for i in range(N):
        if nums[i] == code[j]:
            j += 1
        if j == M:
            break
        if j == M:
            print(f"#{tc} 1")
        else:
            print(f"#{tc} 0")