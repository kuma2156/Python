'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    교재 127 페이지

    while 조건식 : 
      들여쓰기 (반복할 연산)
'''
# 반복문에서 반드시 종료 조건이 있어야한다.

under_contruction = True # 공사 상태

# True 일 때 동안 계속 반복
while(under_contruction) :
  response = input("공사가 완료 되었습니까?.")
  if(response == "예") : 
    print("공사 완료")
    under_contruction = False # 공사 완료