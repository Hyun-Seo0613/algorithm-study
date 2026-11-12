# n번째 메모리를 골라 0또는 1로 고르면 끝까지 덮어씌우는 오류 발생
# 원래 상태로 돌아가는데
T = int(input())
for tc in range(1, T+1):
    target = input()

    # 0000 -> 0011
    # 세번째 자리부터 모두 1로 바꾸면 된다.
    # 000 -> 100
    # 첫번째 자리부터 모두 0으로 바꾼다음, 두번째 자리부터 모두 1로 바꾼다.
    # 횟수 자체만 세면 되는거 아닌가?

    current = '0'
    count = 0

    for i in target:
        if i != current:
            count += 1
            current = i
    print(f"#{tc} {count}")