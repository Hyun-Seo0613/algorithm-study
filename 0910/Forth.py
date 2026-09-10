T = int(input())


# 후위표기식의 결과값 계산
def get_result(postfix):
    stack = []

    for c in postfix[:-1]:
        # c가 피연산자(숫자)? 연산자?
        if c not in "+-*/":
            # 타입 조심
            stack.append(int(c))
        else:
            # c가 연산자라면 연산을 하기 위해 피연산자 2개 필요
            if len(stack) < 2:
                return "error"

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
                # 계산 결과 실수
                result = s // e

            # 이 계산 결과를 다른 연산자가 사용
            stack.append(result)

    # 계산이 완료되면 스택에 숫자 하나 남는다. => 최종 결과 값
    if len(stack) > 1:
        return "error"
    else:
        return stack.pop()


for tc in range(1, T + 1):
    susick = input().split()

    answer = get_result(susick)

    print(f"#{tc} {answer}")