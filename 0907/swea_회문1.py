T = 10

for tc in range(1, T+1):
    # 회문의 길이
    M = int(input())
    # 8개의 문자열을 입력받아서 arr에 저장
    arr = [input() for _ in range(8)]

    # 회문의 개수를 저장하는 변수
    cnt = 0

    # 모든 행과 열을 확인하기 위한 반복문
    for i in range(8):
        # M개의 문자열을 몇번 볼 수 있는지
        for j in range(8-M+1):

            # 가로방향에서 앞과 뒤를 비교 (행 고정시키고 열이 움직임)
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                cnt += 1
            #세로(열 고정시키고 행 움직임)
            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    break
            else:
                cnt += 1
    print(f"#{tc} {cnt}")