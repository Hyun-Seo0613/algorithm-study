txt = input()

# 스택 생성
top = -1
stack = [0] * 100

ans = 1

for x in txt:
    # 여는 괄호면 push
    if x == "(":
        top += 1
        stack[top] = x
    elif x == ")":
        # 닫는 괄호면 꺼내서 확인
        if top == -1: # 스택이 비어있으면 오류(여는괄호 부족)
            ans = 0
            break # for x
        else: # 짝이 맞는지 확인하기 ..
            top -= 1
if top != -1: #여는괄호가 더 많은 경우
    ans = 0
print(ans)

