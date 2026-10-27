count = [0] * 4
# 입력
for _ in range(3):
    sym, temp = input().split()
    temp = float(temp)

    if sym == "Y" and temp >= 37:
        count[0] += 1
    elif sym == "N" and temp >= 37:
        count[1] += 1
    elif sym == "Y" and temp <= 36:
        count[2] += 1
    else:
        count[3] += 1

# 위급상황 : A가 2명 이상
# 출력
if count[0] >= 2:
    print(*count, "E")
else:
    print(*count)