############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

# 특정 길이 이상인 닉네임의 개수를 반환하는 함수 작성
# 반복문 돌려서 names리스트 항목 하나씩 확인함 -> min_length의 길이보다 긴지
# len()이 쓰이는 곳 -> names의 요소의 길이 -> 어떻게 안쓸 수 있을까?
# 반복문 안에 반복문
# 변수를 어디에 두는지도 굉장히 중요함 ...
# 반복문 안에 변수를 뒀을 때 계속 초기화 되는지 안되는지 잘보기


def count_long_names(names, min_length):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    letter_count = 0
    for name in names:
        count = 0
        for letter in name:
            count += 1
        if count >= min_length:
            letter_count += 1
    return letter_count


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(
    count_long_names(["kim", "developer", "ssafy", "a"], 5)
)  # 2 ('developer', 'ssafy')
print(count_long_names(["a", "bb", "ccc"], 5))  # 0
#####################################################
