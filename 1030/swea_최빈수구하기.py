T = int(input())
for tc in range(1, T+1):
    test_case = int(input())
    scores = list(map(int, input().split()))
    count = [0] * 1000

    for i in scores:
        count[i] += 1

    max_count = 0
    for j in range(len(count)):
        if count[j] >= count[max_count]:
            max_count = j

    print(f"#{tc} {max_count}")




