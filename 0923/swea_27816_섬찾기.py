# 섬찾기
# 땅은 L, 바다는 W로 표시
# 상하좌우로 연결된 L은 같은 섬에 속하고 대각선으로만 인접한 육지는 서로 다른 섬
# 몇개의 섬이 존재하는지 알아내자.

T = int(input())

for tc in range(1, T+1):
    # 케이스별로 첫 줄에 N, M 주어진다.
    N, M = map(int, input().split())

    # N줄에 걸쳐 M의 문자가 주어진다.
    code = [input() for _ in range(N)]







