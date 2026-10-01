# 병합정렬 : 계속 반으로 쪼갠다 => 정렬하면서 다시 합친다.
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0

    def merge_sort(arr):
        global count

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        # 결과에 따라 + 1 or + 0
        count += left[-1] > right[-1]

        result = []

        i, j = 0, 0

        # 두 리스트를 비교하면서 작은값부터
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # left에 남은 값 넣기
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1

        return result
    sorted_arr = merge_sort(arr)

    answer = sorted_arr[N//2]
    print(f"#{tc} {answer} {count}")

