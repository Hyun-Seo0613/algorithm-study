# 받은 점수 / 최대M * 100
# 시험 본 과목의 개수 N
N = int(input())
scores = list(map(int, input().split()))

# 최대 점수 먼저 찾기
max_score = scores[0]
for j in range(len(scores)):
    if scores[j] > max_score:
        max_score = scores[j]

ans = []
for i in range(len(scores)):
    scores[i] = scores[i]/max_score*100
    ans.append(scores[i])

total = 0
for k in range(len(ans)):
    total += ans[k]

print(total/len(ans))