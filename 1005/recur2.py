def f(i, N): # 배열의 모든 원소를 출력하는 함수, i: 인덱스, N: 배열의크기
    if i == N:
        return
    else:
        print(A[i])
        f(i+1, N)
A = [1,2,3]
f(0,3)
