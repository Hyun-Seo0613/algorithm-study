# 1차원 배열로 풀기
# 학생 한명의 점수를 리스트로 받음 => 반복분 돌려서 N명 받음

# 학생수
N = int(input())
# 통과한 학생
pass_student = 0

# 4과목 점수 입력받기
for _ in range(N):
    scores = list(map(int, input().split()))

    sum = 0
    count = 0
    for score in scores:
        sum += score
        count += 1

    avg = sum / count
    if avg >= 60:
        pass_student += 1
        print("pass")
    else:
        print("fail")

print(pass_student)
