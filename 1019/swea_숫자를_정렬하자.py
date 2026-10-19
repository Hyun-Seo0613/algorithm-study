T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    answer = ' '.join(map(str, nums))
    print(f"#{tc} {answer}")