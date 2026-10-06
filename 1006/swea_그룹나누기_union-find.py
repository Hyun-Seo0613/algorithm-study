## 상호배타집합으로 사람들을 같은 조로 묶은 다음, 최종적으로 몇개의 조가 있는지 세기

#초기화 ( 처음에는 전부 혼자임 )
def make_set(x):
    p[x] = x # 처음에는 자기 자신을 부모로 설정하기

# 대표찾기
# x가 속한 집합의 대표 찾기
def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])

# 두 조 합치기
def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)
    p[king_y] = king_x



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 부모 저장 배열
    p = [0] * (N+1)

    for i in range(1, N+1):
        make_set(i)

    # M쌍의 신청서
    arr = list(map(int, input().split()))

    # 두명씩 같은 집합으로
    for i in range(M):
        a = arr[i*2]
        b = arr[i*2+1]

        union(a, b)

    answer = 0

    # 대표자 개수
    for i in range(1, N+1):
        if find_set(i) == i:
            answer += 1
    print(f"#{tc} {answer}")
