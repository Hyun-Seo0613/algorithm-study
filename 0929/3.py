def abc(level):
    # print("#", end=" ")
    if level == 2:
        # print("#", end=" ")
        return

    # print("#", end=" ")
    for i in range(3):
        # print('#', end=" ")
        abc(level+1)
        print("#", end=" ")
    # print("#", end=" ")
abc(0)

# print() 할때 어떻게 출력되는지 바로바로 알정도로 공부하기