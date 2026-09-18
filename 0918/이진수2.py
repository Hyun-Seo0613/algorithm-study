T = int(input())

for tc in range(1, T+1):
    decimal = float(input())

    arr = []

    while decimal != 0:
        decimal *= 2

        if decimal >= 1:
            arr.append(1)
            decimal -= 1
        else:
            arr.append(0)

        if len(arr) > 12:
            break

    if len(arr) > 12:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc}", *arr, sep="")