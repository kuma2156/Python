'''
    2023-10-18
    201795016 김명규
    리스트 만들기
'''
# 리스트 만들기
fruits = ['딸기','사과','바나나']

print(f"과일 목록 : {fruits}")

# 리스트 추가 => append() 함수 사용 (마지막 인덱스에 추가 된다.)
fruits.append("수박")
print(f"\n:: append(수박) ::\n과일 목록 : {fruits}")

fruits.append("망고")
print(f"\n:: append(망고) ::\n과일 목록 : {fruits}")

# + 연산자 사용 (마지막 인덱스에 추가된다.)
fruits = fruits + ['포도']
print(f"\n:: + [list] ::\n과일 목록 : {fruits}")

numbers = [1,2,3] + [4,5,6] # list 에서 + 는 연결이다.
print(f"\n:: + 연산자 ::\n숫자 리스트 : {numbers}")

# * 연산자 사용 (배열을 n 번 반복한다.)
numbers = [1,2,3] * 3
print(f"\n:: * 연산자 ::\n숫자 리스트 : {numbers}")

# in 연산자 사용 (포함 되는가?)
print("과일 목록에 망고가 있나요?", '망고' in fruits)

'''
  인덱스를 사용하여 리스트의 항목에 접근하기.
'''
# 과일 리스트에 있는 과일의 갯수? 
print(f'과일의 개수 : {len(fruits)}')

# 과일 중 제일 첫 번째 과일은 ? (인덱스 0)
print(f"과일 중 첫 번째 과일은 ? {fruits[0]}")

# 과일 리스트 중 제일 마지막 과일은 ? (인덱스 -1)
print("과일 중 제일 마지막 과일은? ",fruits[-1])

'''
  문자열 배열에선 사전식 순서로 max() 와 min() 으로 된다
  즉, 가나다라... 순서이다.
'''

# 과일 중 가장 큰 과일은 ? (max())
print(f"가장 큰 과일 (문자열 배열의 max()) : {max(fruits)}")

# 과일 중 가장 작은 과일은 ? (max())
print(f"가장 작은 과일 (문자열 배열의 min()) : {min(fruits)}")

# 정렬
fruits.sort() # 오름차순
print(f'오름차순 정렬 : {fruits}')
fruits.sort(reverse=True) # 내림차순 영구적으로 리버스 된다.
print(f'내림차순 정렬 : {fruits}')

'''
  리스트를 원하는 모양으로 자르는 슬라이싱
'''
# :
print("\n\n\n과일 목록 : ", fruits)
print("과일 리스트 중 2,3,4 번 과일은 ? : ",fruits[1:4]) # 1번지 ~ 3 번지까지 
print("과일 리스트 중 1 ~ 3 번 과일은 ? : ",fruits[0:3]) # 0번지 ~ 2 번지까지 
print("과일 리스트 중 1 ~ 3 번 과일은 ? : ",fruits[:3]) # 0번지 ~ 2 번지까지 
print("과일 리스트 중 3 ~ 마지막 번 과일은 ? : ",fruits[2:]) # 2번지 ~ 마지막 번지까지 

# ::
print("과일 리스트 중 1,3,5 번 과일은 ? : ",fruits[::2]) # 처음부터 끝까지 2씩 증가하면서.
print("과일을 거꾸로 출력 ",fruits[::-1]) # == revers=True 일시적으로 리버스 시켜준다.


'''
  리스트의 원소 값을 자유롭게 조작해보자.
'''
print("\n\n\n과일 목록 : ", fruits)

# 원하는 위치에 추가 '두리안' 추가. insert() 사용
fruits.insert(3,'두리안') # insert(번지 , 추가할 요소)
print("두리안이 추가된 과일 목록 : ", fruits)

# 위치 찾기 index() 사용
print("사과의 위치는 ? : ",fruits.index("사과"))

# 사과를 마지막에 추가
fruits.append("사과")
print("사과 마지막에 추가: ",fruits)

# 사과의 개수 찾기 count() 사용
print(f"사과의 개수는 ? : {fruits.count('사과')}")

'''
  리스트의 항목 삭제
'''
print("\n\n\n")

# 사과 삭제 remove() "지정 삭제"
#   리스트에 제거할 같은 이름의 항목이 여러개 일 경우 배열의 앞 인덱스 값 하나만 지워진다.
fruits.remove("사과")
print("과일 목록(remomve('사과')) : ", fruits)

# 항목 삭제  pop() 사용 "마지막 인덱스 삭제"
#   마지막 항목을 삭제시켜준다.
fruits.pop()
print("과일 목록(pop) : ", fruits)

# del() 키워드=> 포도 삭제
del fruits[0] # 0 번지 항목 삭제
print("과일 목록(del fruits[0]) : ", fruits)
