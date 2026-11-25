N, M = map(int, input().split())

basket = []

# 바구니 초기화
for i in range(1, N+1):
    basket.append(i)

# M번 바구니 뒤집기
for _ in range(M):
    i, j = map(int, input().split())

    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)