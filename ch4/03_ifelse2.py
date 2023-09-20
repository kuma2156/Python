'''
    2023-09-20
    201795016 김명규
    선택문 if else 를 이용하여 짝수인지 홀수인지 판단하는 코드
    짝수 홀수는 양수일 경우에만 판단한다.
'''
# 변수 선언 및 초기화
inputNum = int(input('숫자를 입력하세요'))

if inputNum < 0 : 
    print("양수 일때 만 판단합니다. ")
else :
    # 연산
    if inputNum % 2 == 0 :
        print(f"{inputNum}은 짝수입니다. \n")
    else : 
        print(f"{inputNum}은 홀수입니다. \n")
