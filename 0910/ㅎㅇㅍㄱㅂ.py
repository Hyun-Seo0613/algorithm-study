# 중위표기법(infix) => 후위표기법(postfix)

# 스택 외부(icp) 우선순위
icp = {"(": 3, "*": 2, "/": 2, "+": 1, "-": 1}

# 스택 내부(isp) 우선순위
isp = {"(": 0, "*": 2, "/": 2, "+": 1, "-": 1}


# 중위표기식 => 후위표기식
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""

    # 연산자를 저장할 스택
    stack = []

    for i in range(n):
        # 피연산자(숫자)인지 연산자인지 확인
        if infix[i] not in "()+-*/":
            # 숫자라면 후위표기식에 바로 추가
            postfix += infix[i]

        else:
            # 오른쪽 괄호인 경우
            if infix[i] == ")":
                while stack:
                    # 스택에서 연산자 하나 꺼냄
                    op = stack.pop()

                    # 왼쪽 괄호를 만나면 종료
                    if op == "(":
                        break

                    # 괄호가 아니면 후위표기식에 추가
                    postfix += op

            else:
                # 현재 연산자보다 우선순위가 높거나 같은 연산자를
                # 스택에서 먼저 꺼냄
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    postfix += stack.pop()

                # 현재 연산자를 스택에 저장
                stack.append(infix[i])

    # 스택에 남은 연산자를 모두 꺼냄
    while stack:
        postfix += stack.pop()

    return postfix


infix = "(6+5*(2-8)/2)"
postfix = get_postfix(infix, len(infix))

print(postfix)


# 후위표기식 계산
def get_result(postfix):
    stack = []

    for c in postfix:
        # 숫자인 경우
        if c not in "+-*/":
            stack.append(int(c))

        # 연산자인 경우
        else:
            # 뒤쪽 피연산자
            e = stack.pop()

            # 앞쪽 피연산자
            s = stack.pop()

            result = 0

            if c == "+":
                result = s + e

            elif c == "-":
                result = s - e

            elif c == "*":
                result = s * e

            elif c == "/":
                result = s / e

            # 계산 결과 다시 스택에 넣기
            stack.append(result)

    # 최종 결과 반환
    return stack.pop()


result = get_result(postfix)

print(result)