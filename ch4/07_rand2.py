'''
    2023-09-20
    201795016 김명규
    선택문 if else
    random 을 이용한 가위바위보 게임
    2명의 플레이어의 이름을 입력받아 가위바위보를 진행합니다

'''

UserName1 = (input("플레이어1 의 이름 : >> "))
UserName2 = (input("플레이어2 의 이름 : >> "))

import random

num1 = random.randint(1,3)
num2 = random.randint(1,3)

print(UserName1 ," : " ,end ='') # end = '' 맨 끝에 해당 변수 출력
if num1 == 1:
    print("가위")
if num1 == 2:
    print("바위")
if num1 == 3 :
    print("보")

print(UserName2 ," : " ,end ='')
if num2 == 1:
    print("가위")
if num2 == 2:
    print("바위")
if num2 == 3 :
    print("보")

if num1 == num2 :
    print("무승부!")
elif num1 == 1 and num2 == 2 :
    print(f"{UserName2} 의 승리! ")
elif num1 == 2 and num2 == 3 :
    print(f"{UserName2} 의 승리! ")
elif num1 == 3 and num2 == 1 :
    print(f"{UserName2} 의 승리! ")
else : 
    print(f"{UserName1} 의 승리! ")