T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 소수로 N을 나누어서 나누어 떨어지면 해당 소수의 지수를 증가시키자.
    num_list = [2,3,5,7,11]
    abcde = [0] * 5

    for i in range(5):
        while N % num_list[i] == 0:
            abcde[i] += 1
            N //= num_list[i]
    print(f"#{tc}", *abcde)