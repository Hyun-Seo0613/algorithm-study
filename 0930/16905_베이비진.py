T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = [0] * 12
    player2 = [0] * 12

    answer = 0

    for i in range(12):
        # player1 => 번갈아서 가져감 0,2,4,6,8,10
        if i % 2 == 0:
            # 뽑은 카드의 개수를 1 증가
            player1[cards[i]] += 1

            # triplet 검사
            if player1[cards[i]] >= 3:
                answer = 1
                break

            # run 검사 j= 0 이면 0,1,2 ..... j=7 이면 7,8,9 검사하므로 8번
            for j in range(8):
                if player1[j] >= 1 and player1[j+1] >= 1 and player1[j+2] >= 1:
                    answer = 1
                    break

            if answer == 1:
                break

        # player2
        else:
            player2[cards[i]] += 1

            # triplet
            if player2[cards[i]] >= 3:
                answer = 2
                break

            # run
            for j in range(8):
                if player2[j] >= 1 and player2[j+1] >= 1 and player2[j+2] >= 1:
                    answer = 2
                    break
            if answer == 2:
                break
    print(f"#{tc} {answer}")