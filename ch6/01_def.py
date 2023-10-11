'''
    2023-10-11
    201795016 김명규
    함수
    def 예약어를 이용하여 함수를 만들고 호출하기
'''

print(":::def 예약어를 이용하여 함수를 만들고 호출하기:::")

# 함수 선언
def address() :
  print("부산시 사상구 ")
  print("괘법동 1-1번지")
  print("신라대학교")

# 함수 호출
address()

print()

'''
  함수에 값을 넘겨주고 일을 시킨다.
  인자와 매게변수
'''

print("::::::인자와 매게변수::::::")
# 함수 선언
def welcome(name) :
  print(f"{name}님 환영합니다!")

inputName = input("이름을 입력하시오. >> : ")
# 함수 호출
welcome(inputName)