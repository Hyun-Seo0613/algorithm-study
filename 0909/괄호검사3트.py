# stack 으로
T = int(input())

for tc in range(1, T+1):
    text = input()

    pair = {"(":")", "{":"]"}

    stack = []

    # 우선 괄호 잘 닫혀있다고 가정
    answer = 1

    # 검사 시작
    for t in text:
        if t in "({":
            stack.append(t)

        if t in ")}":
            # 스택에 꺼낼 괄호 남아있는가?
            if not stack:
                answer = 0
                break

            left = stack.pop()
            if pair[left] != t:
                answer = 0
                break
        if stack:
            answer = 0

        print(f"#{tc} {answer}")



