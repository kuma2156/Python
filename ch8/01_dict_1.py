'''
    2023-11-01 
    201795016 김명규
    8.1 키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}
'''

# 빈 딕셔너리 생성
phone_book1 = {}

# 1. 딕셔너리에 값 저장 key, value  [key] = value
phone_book1['김명규'] = '010-1234-5676'
#             key            value
print(f"phone_book1 = {phone_book1}")

# 2. 딕셔너리에 값 저장 {key : value}
phone_book2 = {'홍길동': '010-4545-2211','김명규':'010-8221-0329'}
#                key          value
print(f"phone_book2 = {phone_book2}")

phone_book3 = {}
phone_book3['김명규'] = '010-1234-5676'
phone_book3['홍길동'] = '010-4231-2211'
phone_book3['엄준식'] = '010-0001-9999'
phone_book3['이지수'] = '010-3974-0808'
phone_book3['차차차'] = '010-4554-2366'
print(f"phone_book3 = {phone_book3}\n\n")

print("::: 전화번호 phone_book3 출력 ::: ")
# 모든 key 출력
print(phone_book3.keys())
# 모든 value 출력
print(phone_book3.values())
# 모든 key 와 value 출력
print(phone_book3.items())


print()
print("::: 전화번호 phone_book3 items()출력 ::: ")
for name,phoneNum in phone_book3.items() :
  print(name, ' :',phoneNum)

print()
print("::: 전화번호 phone_book3[keys]로 접근하여 출력 ::: ")
for key in phone_book3.keys() :
  print(key, ': ', phone_book3[key])
  #     key에 해당하는 value 값 출력

print()
print("딕셔너리 작성시 :(콜론)을 기준으로 key와 value 작성")
person_dict = {'name':'김명규','age':19,'class':'1학년'}

print('name : ',person_dict['name']) # 딕셔너리에 'name'깂을 조회하여 출력
print('age : ',person_dict['age'])   # 딕셔너리에 'age' 값을 조회하여 출력
print('class : ',person_dict['class'])

print()

print("::: 정렬 :::")
# phone_book3 를 정렬
# 딕셔너리를 키를 기준으로 정렬하여 리스트로 출력
print(sorted(phone_book3))

print("::: 키를 기준으로 전체 정렬 :::")
sort_phone_book3 = sorted(phone_book3.items(),key = lambda X : X[0]) # phone_book3.items(),key = lambda X : X[0] 0번지를 기준으로 정렬
print(f"sort_phone_book3 = {sort_phone_book3}") # lambda 는 이름없는 함수 lambda 매개변수 : 매개변수[번지]

print("::: 값를 기준으로 전체 정렬 :::")
sort_phone_book3 = sorted(phone_book3.items(),key = lambda X : X[1]) # phone_book3.items(),key = lambda X : X[1] 1번지를 기준으로 정렬
print(f"sort_phone_book3 = {sort_phone_book3}")

print()

print("::: 항목 삭제 :::")
del phone_book3['김명규']
print(phone_book3)

print("::: 항목 전체삭제 :::")
phone_book3.clear()
print(phone_book3)
