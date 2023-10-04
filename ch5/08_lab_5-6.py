'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    교재 5-6 문제
    사용자로 부터 암호를 받아 로그인하기
    
'''

CheckLogin = True

password = ""

while CheckLogin :
  password = input("비밀번호를 입력하세요 >> : ")
  if(password == "1234"):
    print("로그인 성공!")
    CheckLogin == False
    break

  print("비밀번호가 일치하지 않습니다.")