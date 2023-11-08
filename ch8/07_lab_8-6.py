'''
    2023-11-01 
    201795016 김명규
    키와 값을 가지는 딕셔너리
    
    튜플 = () 리스트 = [] 딕셔너리 = {}

    lab 8-6

'''

student_tup = (('201795016','김명규','010-1111-2222'),('202295011','이지수','010-4444-5555'),('202056632','엄준식','010-2999-6666'))

# 딕셔너리 만들기
student_dict = {}
student_dict_phone = {}
for id,name,phone in student_tup:
  student_dict[id] = [name]
  student_dict_phone[id] = [phone]

# 출력
print(":: 학생 정보 :: ")
for key , value in student_dict.items() :
  print(f"{key} : {value}")

# 조회
insertID = input("학번을 입력하시오 : ")
if insertID in student_dict :
  print(f"학생 이름은 {student_dict[insertID][0]}이며, 전화번호는 {student_dict_phone[insertID][0]}")
