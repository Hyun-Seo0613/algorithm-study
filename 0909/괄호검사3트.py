T = int(input())
for tc in range(1, T+1):
    text = input()

    # 스택 이용해서 풀기
    stack = []

    pair = {"(":")", "{": "}"}

    for i in text:
        if i in "{(":
            if not stack:
                answer = 0
                break
            left = stack.pop()
            if pair[left] != i:
                answer = 0
                break
    if stack:
        answer = 0

    print(f"#{tc} {answer}")
