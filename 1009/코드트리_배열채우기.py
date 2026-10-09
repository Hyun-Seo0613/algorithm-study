A = list(map(int, input().split()))

arr = []
# 중간에 0이 입력되면 바로 중단 => 입력받은 것들을 거꾸로 출력한다.
# 건너뛰는게 아니라 입력 자체를 중단
for i in A:
    if i != 0:
        arr.append(i)
    else:
        break

# 인덱스 번호로 생각해야된다 => 만약 5번째 원소까지면 0부터 4까지
for j in range(len(arr) - 1, -1, -1):
    print(arr[j], end=" ")


