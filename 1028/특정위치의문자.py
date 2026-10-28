# 6개의 문자 배열을 만들고, 초기화
arr = ['L', 'E', 'B', 'R', 'O', 'S']
# 첫번째 줄에 한개의 문자가 입력
code = input()
# 없다고 설정해놓고 시작 => 탐색 과정에서 걸리면 index나오고 아니면 None 나옴
answer = 'None'

# 문자탐색
for i in range(len(arr)):
    if arr[i] == code:
        answer = i
        break

print(answer)