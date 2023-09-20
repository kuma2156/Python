'''
    2023-09-20
    201795016 김명규
    선택문 if else
    년도를 입력 받아 윤년인지 아닌지 판단하는 프로그램

    연도가 4로 나누어 떨어지는 경우 윤년입니다.
    그러나 100으로 나누어 떨어지는 연도는 윤년이 아닙니다.
    그러나 400으로 나누어 떨어지는 연도는 다시 윤년입니다.
'''

# 선언 및 초기화
inputDate = int(input('년도를 입력하세요 >> '))

# 연산
if inputDate % 4 == 0 :
    isLeafDate = True
        
    if inputDate % 400 == 0 :
        isLeafDate = True
    elif inputDate % 100 == 0 :
        isLeafDate = False
        
    if isLeafDate :
        print("윤년입니다.")
    else :
        print("윤년이 아닙니다.")
else :
    print("윤년이 아닙니다.")