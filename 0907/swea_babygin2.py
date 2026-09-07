# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다. 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.
#
# • 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
# • 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다. (456, 000)
# • 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin 이 아니다. (123을 run으로 사용하더라도 011이 run이나 triplet가 아님)
#
# 첫줄에 테스트케이스의 개수 T가 입력으로 주어진다.
# 두 번째 줄 부터 각 테스트케이스의 입력이 주어진다.
# 각 테스트케이스의 첫번째 줄에 카드6장의 숫자가 입력으로 주어진다.
#
# 카드6장으로 완성이 된다면 "Baby Gin" 을 출력하고, 되지 않는다면 "Lose"를 출력한다.
# 출력 형식은 예시를 참고한다.

T = int(input())
for tc in range(1, T+1):
    cards = input()

    # 0~9 count
    count = [0] * 10

    for card in cards:
        count[int(card)] += 1

    # Baby Gin
    i = 0
    # Triplet
    tri = 0
    # run
    run1 = 0

    while i < 10:
        if count[i] >= 3:
            count[i] -= 3
            tri += 1
            continue
        if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            continue
        i += 1

    if run1 + tri == 2:
        print(f"#{tc} Baby Gin")
    else:
        print(f"#{tc} Lose")






