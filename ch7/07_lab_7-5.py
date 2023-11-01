'''
    2023-11-01
    201795016 김명규
    튜플

    리스트와 달리 안의 항목을 수정할 수 없다.
    lab 7-5

    함수는 튜플을 돌려줄 수 있다.

    반지름을 입력받아 원의 넓이와 둘레를 계산하시오
    넓이와 둘레룰 계산하는 함수를 작성하시오
    함수는 넓이와 둘레를 함께 돌려줍니다 return

    [함수]
    3. 함수 계산해준다.
    4. 계산한 값을 리턴한다.
    [메인]
    1. 반지름을 입력받는다
    2. 함수로 넘겨준다
    5. 넓이와 둘레를 출력
'''
# 파이값 가져오기
import math
PI = math.pi

# 함수 작성
def calCircle(r) :
  circleArea = r * r * PI    # 넓이
  Circumference = r * 2 * PI # 둘레
  return (circleArea , round(Circumference,2))# 소수 둘째 자리까지만 출력

inputRadius = int(input("원의 반지름을 입력하세요 >> "))
# 함수에서 돌려주는 방식이 튜플이다.
circleArea , Circf = calCircle(inputRadius) # 함수의 리턴값을 각각 배정
print(f"원의 넓이 : {circleArea:.2f}\n원의 둘레 : {Circf}")
#                              :.2f 소수점 둘째 자리까지 출력

circle = calCircle(inputRadius) # 튜플로 출력
print(f"원의 넓이 : {circle[0]:.2f}\n원의 둘레 : {circle[1]}")
