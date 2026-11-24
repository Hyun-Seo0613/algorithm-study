N, M = map(int, input().split())
# M개의 줄에 걸쳐서 공을 넣는 방법이 주어지고
# i, j, k 로 주어짐
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())

    for x in range(i-1, j):
        basket[x] = k
print(*basket)