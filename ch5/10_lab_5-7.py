'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    lab 5-7
    입력받은 수를 사용하는 구구단을 출룍
'''

input = int(input("입력받은 수로 구구단을 출력합니다 >> : "))

i = 1
while (i <= 9) :
  result = input * i
  print(f"{input} x {i} = {result}")
  i += 1
