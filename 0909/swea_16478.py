# 반복문자 지우기
# 문자열 s에서 반복된 문자를 지우려고 한다.
# 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분 다시 지운다.
# 반복문자를 지운 후 남은 문자열의 길이 출력하기 / 남은 문자열 없으면 0출력

T = int(input())

for tc in range(1, T+1):
    text = input()

    # 문자열 길이 최대 1000
    size = 1000

    # 스택 만들기
    stack = [0] * size

    # stack 비어있는 상태
    top = -1

    for i in range(len(text)):
        # 스택이 비어잇으면 비교할 글자가 없다 => push
        if top == -1:
            top += 1
            stack[top] = text[i]

        # 스택에 비교할 글자가 있는 경우
        else:
            if stack[top] != text[i]:
                top += 1
                stack[top] = text[i]
            # 스택의 맨 위 문자와 현재문자를 비교해서 같으면 pop
            else:  ## stack[top] == text[i]
                top = -1
    # 스택에 남아있는 원소의 개수 = top + 1개
    print(f"#{tc} {top + 1}")
