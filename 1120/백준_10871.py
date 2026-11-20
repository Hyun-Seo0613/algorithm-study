N, X = map(int, input().split())
A = list(map(int, input().split()))

answer = []

# A에서 X보다 작은 수를 출력하는 프로그램
# A를 순회해서 X보다 작은 수가 있는지 if문으로 확인하기
for i in range(len(A)):
    if A[i] < X:
        answer.append(A[i])
print(*answer)




