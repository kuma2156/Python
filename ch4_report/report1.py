'''
    2023-09-20
    201795016 김명규
    따라하며 배우는 파이썬과 데이터 과학
    113 페이지 심화문제 풀이
    4.3 문제
    다음과 같이 사용자로부터 나이를 입력받아 20살 이상이면 'Adult', 10살 이상이면 'Youth' 10살 미만이면
    'Kid' 를 출력하는 프로그램을 if-else 문을 사용하여 작성하라.
'''
# 선언
inputAge = -1

# 오류 해결
while (inputAge < 0):
  inputAge = int(input('나이를 입력하세요'))
  if inputAge < 0 :
    print(" ******* 나이를 정확히 입력하세요 *******")
    inputAge = int(input('나이를 입력하세요'))

# 연산 및 출력
if inputAge >= 20 : 
  print("Adult")
elif inputAge >= 10 :
  print("Youth")
else :
  print("Kid")