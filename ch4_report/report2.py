'''
    2023-09-20
    201795016 김명규
    따라하며 배우는 파이썬과 데이터 과학
    113 페이지 심화문제 풀이
    4.4 문제
    하나의 정수를 입력으로 받아서 이 정수가 2로 나누어지는지, 3으로 나누어지는지, 혹은 두 정수 모두로 나누어지는지 알려주는 프로그램을 작성하시오
'''
# 선언
inputNum = -1

# 오류해결
while (inputNum < 0):
  inputNum = int(input('정수를 입력하세요 >>> '))
  if inputNum < 0 :
    print(" ******* 정수를 입력하셔야 합니다 ..  *******")

# 연산
if inputNum % 2 == 0 :
  print(f"{inputNum}은 2로 나누어집니다 !")
else :
  print(f"{inputNum}은 2로 나누어지지않습니다..")

if inputNum % 3 == 0 :
  print(f"{inputNum}은 3으로 나누어집니다 !")
else :
  print(f"{inputNum}은 3으로 나누어지지않습니다..")

if inputNum % 2 == 0 and  inputNum % 3 == 0:
  print(f"{inputNum}은 2와 3 모두 나누어집니다 !")
else :
  print(f"{inputNum}은 2와 3 전부 나누어지지않습니다..")