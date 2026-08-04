############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  max, min
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)


# 최고가와 최저가의 차이를 정수로 반환하는 코드
# def find_price_range(prices):
#     # 여기에 코드를 작성하여 함수를 완성합니다.
#     min_price = min(prices)
#     max_price = max(prices)

#     result = max_price - min_price
#     return result


def find_price_range(prices):
    # 최고가와 최저가를 어떻게 구할건지 ?
    # 반복문 안에서 if 문으로 처리
    max_price = prices[0]
    min_price = prices[0]
    for price in prices:
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price
    result = max_price - min_price
    return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_price_range([1000, 2500, 1800, 3000, 2200]))  # 2000 (3000 - 1000)
print(find_price_range([500]))  # 0
#####################################################
