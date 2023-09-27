'''
    2023-09-27
    201795016 김명규
    lab 5-5 문제
    사용자로부터 임의의 정수 n울 입력받은 뒤에 for 문을 이용하여서 팩토리얼을 계산하는 코드
'''
fac = 1
# 입력
inputNum = int(input("정수를 입력하시오."))

# 연산
if(inputNum < 0) :
  print("정수를 입력하셔야 합니다.")
else :
  for i in range(1, inputNum +1) :
    fac = fac * i

  print(f"{inputNum}!은 {fac}입니다.")

