'''
    2023-09-27
    201795016 김명규
    반복문 for

'''

print("::: 내 이름 5번 출력 ::: (for in 형) ")
for i in range(5) :
  print(f"{i}김명규")

print("::: 내 이름 5번 출력 ::: (list 형) ")
for i in [1,2,3,4,5] :
  print(f"{i}김명규")

print("::: 리스트로 구구단 19단 출력 ::: (list 형) ")
for i in [1,2,3,4,5,6,7,8,9] :
   print(f"19 X {i} = {19 * i}")

print("::: 문자열 내용 출력 ::: (for in 문자형) ")
for i in "hello" :
  print(f"i = {i}")


# 도전문제 5.3
bts = ['V','J-Hope','JungKook','Jin','Jimin','Suga']
for i in bts :
  print(f"bts 멤버 이름 : {i}")
