T = int(input())

for tc in range(1, T+1):
    text = input()
    size = 1000

    top = -1
    stack = [0] * size

    for i in range(len(text)):
        # 스택이 비어있으면 비교할 글자가 x => push해서 스택에 넣기
        if top == -1:
            top += 1
            stack[top] = text[i]
        # 스택에 비교할 글자가 있으면
        else:
            # 비교 후 다르면 push
            if stack[top] != text[i]:
                top += 1
                stack[top] = text[i]
            # 비교 후 같으면 pop
            else:
                top -= 1
    # top+1 인 이유: top은 원소의 개수가 아니라 인덱스이기 때문
    print(f"#{tc} {top+1}")