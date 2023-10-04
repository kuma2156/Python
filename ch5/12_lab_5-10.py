'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    lab 5-10
    while 문
    사용자가 입력하는 숫자의 합을 계산하자
'''

# 합계
sum = 0
answer = "yes"

# 대답이 yes일 땐 계속 반복한다.
while(answer == "yes") : # 대답이 yes가 아니면 종료
  inputNum = int(input("숫자를 입력하시오 : ")) # 숫자 입력받기
  sum += inputNum # 입력받은 값 더하기
  answer = input("계속 ? (yes / no) : ") # 대답 받기 (yes or no)
  if(answer == "no") : # 대답이 no 일 경우 합계출력
    print(f"합계는 {sum} 입니다. ")
  