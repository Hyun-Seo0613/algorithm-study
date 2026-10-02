T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 제품당 한줄씩 N개의 줄에 걸쳐 공장별 생산비용 주어짐
    cost = [list(map(int, input().split())) for _ in range(N)]

    # 전체 제품의 최소 생산 비용을 계산하는 프로그램 (

