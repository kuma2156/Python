'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    break 와 continue
    lab 5-11 더하기 암산 문제 만들기
      2개의 수로 더하기 결과를 맞추는 게임
      두개의 수는 1에서 100 사이의 랜덤으로 출제됌
      사용자가 0을 입력하면 프로그렘은 종료
      즉, 사용자가 0을 입력하기 전까지는 무한 반복하여 문제풀기
      정답을 맞추면 "참 잘했어요" 틀리면 정답을 알려주고, " 틀렸습니다" 출력하기
'''

import random

inputNum = 1

while inputNum != 0 :
  # 랜덤으로 1 ~ 100 숫자
  rand1 = random.randint(1,100) 
  rand2 = random.randint(1,100) 

  inputNum = int(input(f"{rand1} + {rand2} = ")) # 정답 입력
  sum  = rand1 + rand2 # 더하기
  if inputNum == 0 : break # 정답이 0 일 경우 반복문 종료
  if inputNum == sum : # 답과 합계가 같을 경우 
    print(f"참 잘했어요! ") 
  else :
    print(f"틀렸습니다.. 정답은 {sum}입니다.")