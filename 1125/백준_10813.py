N, M = map(int, input().split())
basket = []
for i in range(1, N+1):
    basket.append(i)

for _ in range(M):
    # i번 바구니와 j번 바구니의 공을 교환한다.
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)