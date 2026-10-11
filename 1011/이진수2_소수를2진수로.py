T = int(input())
for tc in range(1, T+1):
    N = float(input())
    arr = []

    while N != 0:
        N *= 2
        if N >= 1:
            arr.append(1)
            N -= 1
        else:
            arr.append(0)

        if len(arr) > 12:
            break
        if len(arr) > 12:
            print(f"#{tc} ovreflow")
        else:
            print(f"#{tc}", end=" ")
            print(*arr, sep="")