# 공백으로 구분된 학생들의 점수가 주어지며, 전체 입력값은 100개 이하
# 0이 등장하면 그 이후의 값은 무시한다
scores = list(map(int, input().split()))

# 주어진 점수를 10점 단위로 구분하여 점수대별 학생 수를 출력하는 프로그램 작성하기
# 십의 자리 수를 세면 된다. = > 카운팅 배열
count = [0] * 100

for score in scores:
    if score == 0:
        break
    if 0 < score < 10:
        continue
    else:
        count[score//10] += 1

# 100 점대 -> 90점대 -> 80점대 역순으로 출력한다.
for i in range(10, 0, -1):
    print(f"{i*10} - {count[i]}")

