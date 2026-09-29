# 매개변수는 global이 아니다
# 함수가 끝나면 함수를 호출한 곳으로 돌아간다.

# # 재귀 이용해서 출력해보기
# 0 1 2 3 2 1 0
# 0 1 2 3 4 5 5 4 3 2 1 0

# def abc(level):
#     # print(level, end=' ')
#     if level == 3:
#         # return 전에 출력해도 같은 결과
#         print(level, end=' ')
#         return
#
#     print(level, end=' ')
#     abc(level+1)
#     print(level, end=' ')
#
# abc(0)

# 코드가 어떤 타이밍에 호출이 되는지 여러번 연습해보기 
def abc(level):
    if level == 6:
        return

    print(level, end=' ')
    abc(level+1)
    print(level, end=' ')


abc(0)
