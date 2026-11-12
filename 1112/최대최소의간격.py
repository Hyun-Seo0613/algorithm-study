# T = int(input())
# for tc in range(1, T+1):
#     # 양수의 개수 N
#     N = int(input())
#     # N개의 양수
#     nums = list(map(int, input().split()))
#
#     # 최대값의 위치와 최소값의 위치의 차이
#     # 여러개일 때 조건 확인하기
#     max_idx = 0
#     min_idx = 0
#     for i in range(len(nums)):
#         # 등호가 없으면 같은 값일 때 갱신하지 않아서 가장 왼쪽 위치가 남는다.
#         if nums[i] < nums[min_idx]:
#             min_idx = i
#         # 등호가 있으면 같은 값이어도 갱신해서 가장 오른쪽 위치가 남는다.
#         if nums[i] >= nums[max_idx]:
#             max_idx = i
#     answer = abs(max_idx - min_idx)
#     print(f"#{tc} {answer}")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for i in range(len(nums)):
        if nums[i] < nums[min_idx]:
            min_idx = i
        if nums[i] >= nums[max_idx]:
            max_idx = i

    answer = abs(max_idx - min_idx)
    print(f"#{tc} {answer}")


