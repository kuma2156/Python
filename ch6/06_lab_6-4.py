'''
    2023-10-11
    201795016 김명규
    함수
    lab 6-4

    리스트에서 최대값,최소값을 찾아 돌려주는 함수
    리스트에 10개의 값을 랜덤으로 생성하고, max 또는 min을 입력 받아 최대,최소값을 찾아 돌려주는 함수

    (함수)
        5) 두 값을 전달 받아 매게 변수에 저장
        6) 최대값, 최소값을 찾는다.
        7) 돌려준다.
    (메인)
      1. 무한 반복
        1) 랜덤으로 10 ~ 99 까지 10개의 수를 리스트로 생성
        2) 생성된 리스트를 출력
        3) 사용자로 부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
          사용자가 입력할 값은 max 또는 min 입니다.
        4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
        8) 돌려받은 최대값 또는 최소값을 출력한다.
'''
import random

# 함수
def outputMaxMin(input_list):
    max_val = max(input_list)
    min_val = min(input_list)
    return max_val, min_val

running = True

while running:
    # 10개의 랜덤 숫자를 생성하여 리스트에 저장
    numList = [random.randint(10, 99) for i in range(10)]

    # 생성된 리스트 출력
    print(numList)

    answer = input("알고 싶은 값 (max 또는 min) >> ")
    max_val, min_val = outputMaxMin(numList)
    
    if answer == "max":
        print(f"리스트의 최대값은 {max_val}")
    elif answer == "min":
        print(f"리스트의 최소값은 {min_val}")
    else:
        print("옳바른 값이 아닙니다.")

    
  

  