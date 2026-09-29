# 누적합 구하기 - 재귀 DFS 구현시 변수를 global로 선언하는가? 매개변수에 선언하는가? 에 따른 차이
# arr = [1,3,5,7]
#
# Sum = arr[0]
#
# def abc(level):
#     global Sum
#
#     if level == 3:
#         print(Sum, end=' ')
#         return
#
#     Sum += arr[level+1]
#     abc(level + 1)
#     # 재귀 호출에서 돌아온 뒤, 이번 단계에서 더했던 값을 다시 빼서 원래 상태로 복구하는 역할 => Sum은 전역변수이므로
#     Sum -= arr[level+1]
#     print(Sum, end=' ')
#
#
# abc(0)

# Sum을 전역변수가 아니라 매개변수로 넣어보기 => 따로 빼줄 필요가 없다.
arr = [1,3,5,7]

def abc(level, Sum):


    if level == 3:
        print(Sum, end=" ")
        return

    abc(level + 1, Sum+arr[level+1])
    print(Sum, end=" ")



abc(0,0)