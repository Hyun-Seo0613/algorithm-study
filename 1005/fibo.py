# cnt: 피보나치 수열을 위해서 몇번의 계산이 일어나는지
def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
cnt = 0 #호출횟수 기록
print(fibo(10), cnt)
