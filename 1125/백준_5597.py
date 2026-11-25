# X대학 M교수님, 학생 30명의 추럭번호 1~30
# 과제제출을 28명이 했고 그 중 제출 안한 2명의 출석번호 구하기
# 28명 입력받기
students = []
answer = []

for i in range(28):
    n = int(input())
    students.append(n)

for i in range(1, 31):
    if i not in students:
        answer.append(i)
answer.sort()
print(answer[0])
print(answer[1])