T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0

    for i in range(N):
        for j in range(i, N):
            if arr[j] - arr[i] <= K:
                cnt = j - i + 1

                if cnt > answer:
                    answer = cnt
            else:
                break
    print(f"#{tc} {answer}")








    
    

