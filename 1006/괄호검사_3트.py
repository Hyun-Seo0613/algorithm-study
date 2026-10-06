T = int(input())

for tc in range(1, T+1):
    txt = input()
    pair = {'(':')', '{':'}'}

    # 스택생성
    top = -1
    stack = [0] * 100
    # 짝이 맞다고 가정 : 1
    ans = 1

    for x in txt:
        # 여는 괄호 만나면 push
        if x in "{(":
            top += 1
            stack[top] = x
        
        # 닫는 괄호 만나면 pop 1) 스택이 비어있는 경우 2) 스택이 비어있지 않으면 짝 확인
        elif x in ")}":
            # 스택이 비어있으면 오류(여는괄호 부족)
            if top == -1:
                ans = 0
                break
            # 스택이 비어있지 않다면 짝이 맞는지 확인하기
            else:
                top -= 1
                # pop
                tmp = stack[top+1]
                if pair[tmp] != x:
                    ans = 0
                    break
    # 여는 괄호가 더 많은 경우
    if top != -1:
        ans = 0
    print(f"#{tc} {ans}")

