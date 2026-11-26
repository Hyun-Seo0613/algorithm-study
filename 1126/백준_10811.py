N, M = map(int, input().split())

# 바구니에 번호 매기기 1~N
basket = []
for i in range(1, N+1):
    basket.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    # 원하는 범위를 잘라낸 다음, 잘라낸 리스트를 뒤집는 방식
    basket[i-1:j] = basket[i-1:j:][::-1]
    # 처음부터 역방향으로 탐색하는 방식
    # basket[i-1:j:-1]
print(*basket)