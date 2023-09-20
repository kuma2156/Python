'''
    2023-09-20
    201795016 김명규
    선택문 if else
    random 을 이용한 가위바위보 게임
'''
# 선언
import random

rand = random.randint(1,3) # 랜덤하게 1~3 하나의 값 생성
UserChoice = (input("가위바위보 게임을 해요 뭘 내실 건가요? (가위 or 바위 or 보) >> "))

# 랜덤 숫자 가위바위보로 치환
if rand == 1 :
    randStr = "가위"
elif rand == 2 :
    randStr = "바위"
else :
    randStr = "보"

# 랜덤 숫자 가위바위보로 치환
print(f"{UserChoice} vs {randStr}")
