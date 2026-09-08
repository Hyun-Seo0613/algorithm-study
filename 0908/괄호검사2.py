T = int(input())

for tc in range(1, T+1):
    code = input()

    # 괄호검사에 사용할 스택
    stack = []

    pair = {"(":")", "{":"}"}

    # 일단 괄호 잘 닫혀있다고 가정 -> 제대로 안된 조건 시 바꾸기
    answer = 1

    for c in code:
        if c in "({":
            stack.append(c)

        if c in ")}":
            # 스택에 꺼낼 괄호 남아있는지 확인
            if not stack:
                answer = 0
                break

            left = stack.pop()
            if pair[left]!= c:
                answer = 0
                break
    if stack:
        answer = 0

    print(f"#{tc} {answer} ")




    