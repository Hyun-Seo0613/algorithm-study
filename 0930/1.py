# "ABC"의 각 문자를 넣을지 말지 선택해서 모든 부분집합을 만드는 재귀코드
name = "ABC"

# level: 지금 어떤 문자를 선택할지 
# path: 지금까지 선택한 문자들

def abc(level, path):
    if level == 3:
        print(*path)
        return

    # 현재 문자를 선택하지 않는 경우(첫번째재귀)
    abc(level+1, path)
    # 현재 문자를 선택하는 경우(두번째재귀)
    abc(level+1, path+[name[level]])

abc(0, [])