'''
    2023-09-20
    201795016 김명규
    따라하며 배우는 파이썬과 데이터 과학
    113 페이지 심화문제 풀이
    4.7 문제
    파이썬의 random.randint(1,100)을 이용하여 1에서 100사이의 임의의 난수 2개를 생성하여라. 다음으로 두 수의 합을 묻는 질문을 사용자에게 던지도록 하자 
    만일 사용자가 두 수의 합을 맞추면 '잘했어요!' 출력하여라 만일 틀릴경우 '정답은 --- 입니다 출력하기'
'''

# 선언
import random
randNum1 = random.randint(1,100)
randNum2 = random.randint(1,100)

# 입력
inputNum = int(input(f"{randNum1} + {randNum2} = "))

# 연산
result = randNum1 + randNum2

if result == inputNum :
  print("잘했어요!! ")
else:
  print(f"정답은 {result}입니다.")
