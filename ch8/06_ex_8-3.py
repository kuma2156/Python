'''
    2023-11-08 
    201795016 김명규
    키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}

    집합 set()
      중복을 허용하지 않는다!
      순서가 없다

      ex 8-3
      학번, 이름, 전화번호의 3쌍의 요소를 가지는 student_tup이 다음과 같이 존재한다
      student_tup = (('201795016','김명규','010-1111-2222'),('202295011','이지수','010-4444-5555'),('202056632','엄준식','010-2999-6666'))

      투플을 수정하여 {학번 : [이름,전화번호]} 의 쌍으로 이루어진 딕셔너리 만들어 출력

      학번을 입력받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성
      student_tup 의 마지막 항목에 학점을 추가한다.

'''
student_tup = (('201795016','김명규','010-1111-2222'),('202295011','이지수','010-4444-5555'),('202056632','엄준식','010-2999-6666'))

# 투플을 수정하여 {학번 : [이름,전화번호]} 의 쌍으로 이루어진 딕셔너리 만들어 출력
student_dict = {}
for id,name,phone in student_tup :
  student_dict[id] = [name , phone]

print(":: 학생의 정보 목록 ::")
for key,value in student_dict.items() :
  print(f"{key} : {value}")

# 학번을 입력받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성
insertID = input("학번을 입력하시오 : ")
if insertID in student_dict :
  print(f"이름 : {student_dict[insertID][0]}")
  print(f"연락처 : {student_dict[insertID][1]}")

# student_tup 의 마지막 항목에 학점을 추가한다.
student_dict['201795016'].append(4.5)
student_dict['202295011'].append(4.2)
student_dict['202056632'].append(4)

print(":: 학생의 정보 목록 ::")
for key,value in student_dict.items() :
  print(f"{key} : {value}")

total = 0
for key , value in student_dict.items() :
  total = student_dict[key][2] + total

print(f"전체 점수 : {total}\n전체 평균 : {(total / len(student_dict)):.2f}")