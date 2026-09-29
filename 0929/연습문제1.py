# 6자리 숫자 입력
numbers = list(map(int, input().split()))
answer = False

# i: 단계를 나타낼 파라미터
# path : 각 단계에서 고른 숫자 저장
# 지금까지 만든 순열의 상태를 나타낸다
# used: 각 단계에서 사용한 인덱스 체크
def perm(i, path, used):
    global answer

    # 기저조건
    if i == 6:
        # 순열을 완성한 상태
        # path에서 앞3 / 뒤3 앞 뒤가 각각 run 또는 triplet 이면 baby-gin!
        front = sorted(path[:3])
        back = sorted(path[3:])

        front_triplet = front[0] == front[1] == front[2]
        front_run = front[0] + 1 == front[1] and front[1] + 1 == front[2]

        back_triplet = back[0] == back[1] == back[2]
        back_run = back[0] + 1 == back[1] and back[1] + 1 == back[2]

        if (front_triplet or front_run) and (back_triplet or back_run):
            answer = True
        return

    # 재귀호출
    for j in range(6):
        # j : 내가 i단계에서 고를 숫자의 인덱스
        # 이전에 j번 인덱스에 있는 숫자를 사용했는지 확인
        # 사용했다면 다른 인덱스에 있는 숫자를 사용하도록 건너뛴다.
        if used[j]:
            continue
        # j번 숫자 사용 체크
        used[j] = 1
        # j번 숫자 순열에 넣고
        path.append(numbers[j])
        perm(i+1, path, used)

        # j번 숫자 사용 해제
        used[j] = 0

        # j번 숫자 순열에서 제거
        path.pop()

# 0단계부터 시작, 순열 초기 상태(아무것도 선택안함), 사용한 인덱스(아무것도 사용안함)

perm(0, [], [0] * 6)

print("Yes" if answer else "No")

# --------------------------------------------------------------------------------------------

# # 6자리 숫자 입력
# numbers = list(map(int, input()))
# answer = False
#
# # i: 단계를 나타낼 파라미터
# # path : 각 단계에서 고른 숫자 저장
# # 지금까지 만든 순열의 상태를 나타낸다
# # used: 각 단계에서 사용한 인덱스 체크
# def perm(i, path, used):
#
#     # 기저조건
#     if i == 6:
#         # 순열을 완성한 상태
#         # path에서 앞3 / 뒤3 앞 뒤가 각각 run 또는 triplet 이면 baby-gin!
#         if(
#                 ((path[0] == path[1] == path[2]) or (path[0] + 2 == path[1] + 1 == path[2])) and
#                 ((path[3] == path[14 == path[5]) or (path[3] + 2 == path[4] + 1 == path[5]))
#         ):
#
#         return
#
#     # 재귀호출
#     for j in range(6):
#         # j : 내가 i단계에서 고를 숫자의 인덱스
#         # 이전에 j번 인덱스에 있는 숫자를 사용했는지 확인
#         # 사용했다면 다른 인덱스에 있는 숫자를 사용하도록 건너뛴다.
#         if used[j]:
#             pass
#         # j번 숫자 사용 체크
#         # j번 숫자 순열에 넣고
#         perm(i+1, path, used)
#         # j번 숫자 사용 해제
#         # j번 숫자 순열에서 제거
#
# # 0단계부터 시작, 순열 초기 상태(아무것도 선택안함), 사용한 인덱스(아무것도 사용안함)
#
# perm(0, [], [0] * 6)





