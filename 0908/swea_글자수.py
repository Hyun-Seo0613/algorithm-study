# 두개의 문자열 str1, str2
# 문자열 str1에 포함된 글자들이 str2에 몇개씩 들어있는지 찾고,
# 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만들기

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    answer = 0

    for i in range(len(str1)):
        count = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        answer = max(answer, count)
    print(f"#{tc} {answer}")