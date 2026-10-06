N = 6

# 자식 번호를 인덱스로 부모 번호를 표현하는 트리
# p[x] = y: x번의 부모 번호는 y번
p = [0] * (N+1)

# 1. 초기화 연산
def make_set(x):
    # 처음에는 자기 자신을 부모로 설정(대표)
    p[x] = x

# for i in range(N+1):
#     p[i] = i
#     make_set(i)

# 2. 대표 찾는 연산
# x가 속한 집합의 대표를 찾는다.
def find_set(x):
    # x의 부모가 자기 자신을 가리키면 대표
    if p[x] != x:
        return x

    # 아닌 경우는 부모한테 다시 부모를 물어보고, 대표를 찾을때까지 계속
    else:
        return find_set(p[x])

# 3. 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합친다.
# 집합을 합치기 위해서는 반드시 대표를 통해서 진행
def union(x, y):
    # x가 속한 집합의 대표
    king_x = find_set(x)
    # y가 속한 집합의 대표
    king_y = find_set(y)

    # 두 집합을 합친 결과는 하나의 집합이 된다. 대표도 둘중 하나로
    p[king_y] = king_x

# for i in range(1, N+1):
#     make_set(i)
#
# union(1,3)
# union(2,3)
# union(5,6)
#
# print(p)
# print(find_set(6))

for i in range(1, 6):
    union(i+1, i)

print(p)
