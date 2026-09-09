# 재귀함수의  기본형
# def f(i, N):
#     if i == N:    # 중단조건
#         return
#     else:       # 재귀호출
#         f(i+1, N)

def f(i, N):  # 배열의 모든 원소를 출력하는 함수, i 인덱스, N 배열크기
    if i == N:
        return
    else:
        print(arr[i])
        f(i+1, N)
        print(arr[i])
arr = [1,2,3]
f(0, 3)