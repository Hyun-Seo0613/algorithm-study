# N: 바구니 개수 , M: 공을 넣는 횟수
N, M = map(int, input().split())
# M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
# i, j, k -> i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다.
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        basket[x] = k
print(*basket)
