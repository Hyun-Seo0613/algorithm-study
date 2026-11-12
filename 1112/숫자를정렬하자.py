T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 주어진 N길이의 숫자열을 오름차순으로 정렬하여 출력하기
    # 버블 정렬
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(f"#{tc}", *nums)
