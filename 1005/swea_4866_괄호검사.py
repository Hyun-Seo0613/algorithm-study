T = int(input())

for tc in range(1,T+1):
    txt = input()
    pair = {'(': ')', '{': '}'}

    # 스택 생성
    top = -1
    stack = [0] * 100

    ans = 1

    for x in txt:
        # 여는 괄호면 push
        if x in "{(":
            top += 1
            stack[top] = x
        elif x in ")}":
            # 닫는 괄호면 꺼내서 확인
            if top == -1:  # 스택이 비어있으면 오류(여는괄호 부족)
                ans = 0
                break  # for x
            else:  # 짝이 맞는지 확인하기 ..
                top -= 1
                tmp = stack[top + 1]  # pop
                if pair[tmp] != x:  # x의 짝 (여는괄호)과 스택에서 꺼낸 여는 괄호가 다르면 ..
                    ans = 0
                    break  # for x

    if top != -1:  # 여는괄호가 더 많은 경우
        ans = 0
    print(f"#{tc} {ans}")


 
