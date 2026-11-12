T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N개의 카드 이름이 공백으로 구분되어 주어진다.
    # 카드의 이름은 알파벳 대문자와 '-'로 이루어져있다.
    card = list(map(str, input().split()))

    # 퍼펙트 셔플 -> 절반 나누고 -> 교대로 카드 선택하기
