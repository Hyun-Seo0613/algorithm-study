# 첫째줄부터 열번째 줄까지 숫자가 한 줄에 하나씩 주어진다.
arr = []
for _ in range(10):
    num = int(input())
    arr.append(num)


answer = []
for i in arr:
    result = i % 42

    if result not in answer:
        answer.append(result)

count = len(answer)
print(count)