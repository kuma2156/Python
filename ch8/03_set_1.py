'''
    2023-11-08 
    201795016 김명규
    키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}

    집합 set()
      중복을 허용하지 않는다!
      순서가 없다
'''

#빈 집합 생성
number = set()

# 숫자 3개로 이루어진 집합
number1 = {2,1,3}

print(f"집합 : {number1}")

# 리스트로부터 집합 생성
number2 = set([1,2,3,1,2])

print(f"집합 : {number2}") # 중복을 허용하지 않는다.

# 문자열을 집합으로 생성
text = set("asdfasdf")

print("text = ",text)

numbers = {2,4,5,1,2}

if 1 in numbers : # numbers 집합 안에 1이 있는가?
  print("1이 있습니다.")

# 집합은 순서가 없어서 인덱스로 접근이 불가능하다.
# 반복문으로 접근하여 출력이 가능하다.
numbers = {9,1,5,2,4,5,1,4,9,7}

for num in numbers :
  print(f"num = {num}",end = ' ')

print()
# 정렬 후 출력하기
for num in sorted(numbers) :
  print(f"num = {num}",end = ' ')

print()
# 정렬 후 출력하기
for num in sorted(text) :
  print(f"text = {num}",end = ' ')

print()
# 추가하기
numbers.add(100)
for num in sorted(numbers) :
  print(num , end = ' ')

print()
# 삭제하기
numbers.remove(100)
print(numbers)

