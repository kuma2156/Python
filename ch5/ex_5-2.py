'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    두 수를 입력 받아 두 수 사이의 합계를 출력하기
    두 수 사이의 짝수의 합계 출력하기

    페이지 141쪽 for 나 while 중 원하는 거
'''

# 두 수 입력받기
inputNum1 = int(input("첫 번째 수 : "))
inputNum2 = int(input("두 번째 수 : "))

result = 0  # 합
even_sum = 0  #짝

if inputNum1 < inputNum2:
    i = inputNum1
    big = inputNum2
else:
    i = inputNum2
    big = inputNum1

while i <= big:
    result += i
    if i % 2 == 0:
        even_sum += i
    i += 1

print(f"두 수 {inputNum1}, {inputNum2} 사이의 합계는 {result}")
print(f"두 수 {inputNum1}, {inputNum2} 사이의 짝수 합계는 {even_sum}")
