'''
    2023-10-18
    201795016 김명규
    리스트 만들기

    리스트의 객체 생성과 참조
'''

fruits1 = ['수박','멜론','사과']

# 실제 값을 복사하는 것이 아니라 리스트의 저장위치(주소) 가 참조 되어진다.
fruits2 = fruits1

print(f"fruits1 : {fruits1}")
print(f"fruits2 : {fruits2}\n\n")

fruits2[1] = '망고' # fruits2 1번지 과일을 망고로 바꾼다.

print(f"fruits1 : {fruits1}")
print(f"fruits2 : {fruits2}")

# 이상하게 fruits1 의 1번지는 수정한 적이 없지만 같이 망고로 수정된다.
# 실제 값을 복사하는 것이 아닌 주소를 참조하는 것이기에 이러한 결과가 나온다.

# 주소 확인 (메모리 위치 정보 알아보기.) id() 함수
print("fruits1의 id : ",id(fruits1))
print("fruits2의 id : ",id(fruits2))
# 주소가 같은걸 확인할 수 있다.


'''
  리스트 내용 복제하기 list() 함수
'''

# 그렇다면 주소값이 아닌 실제 값을 복제하고 싶다면 
fruits2 = list(fruits1) # 내용 복제
print("::: 내용 복제 후 (1):::")
print(f"fruits1 : {fruits1}")
print(f"fruits2 : {fruits2}")

# 주소 확인 (메모리 위치 정보 알아보기.) id() 함수
print("fruits1의 id : ",id(fruits1))
print("fruits2의 id : ",id(fruits2))
# 아이디 값이 다른걸 확인할 수 있다.

# 내용 복제 2
fruits3 = fruits1[:]

print("::: 내용 복제 후 (2):::")
print(f"fruits1 : {fruits1}")
print(f"fruits3 : {fruits3}")

# 주소 확인 (메모리 위치 정보 알아보기.) id() 함수
print("fruits1의 id : ",id(fruits1))
print("fruits3의 id : ",id(fruits3))
# 아이디 값이 다른걸 확인할 수 있다.

# fruits3 의 0번지 값을 복숭아로 수정
fruits3[0] = '복숭아'
print(f"fruits1 : {fruits1}")
print(f"fruits3 : {fruits3}")
# fruits3 의 값만 수정된 것을 보면 알다시피 실제 값만 복사한 것을 확인 가능하다.