'''
    2023-11-08 
    201795016 김명규
    키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}

    집합 set()
      중복을 허용하지 않는다!
      순서가 없다
'''
# 비교 연산자
num1 = {1,2,3}
num2 = {1,2,3}

print("num1 == num2 ? ", num1 == num2)

# 6개 숫자로 이루어진 집합생성
num_set = {1,4,5,7,9,8,8}
print("num_set = ",num_set)
print(num_set)
print("num_set 의 길이 : ",len(num_set))
print("num_set 중 가장 큰 값 : ",max(num_set))
print("num_set 중 가장 작은 값 : ",min(num_set))
print("num_set 합계 : ",sum(num_set))

num1 = {1,2,3}
num2 = {3,4,5}

# 합집합
print("num1 | num2 : ",num1 | num2) # 합집합 연산자
print("num1.union : ",num1.union(num2)) # 합집합 연산자

# 교집합
print("num1 & num2 : ",num1 & num2)
print("num1.intersection(num2) : ",num1.intersection(num2)) 

# 차집합
print("num1 - num2 : ",num1 - num2)
print("num1.difference(num2) : ",num1.difference(num2)) 

# 대칭 차집합
print("num1 ^ num2 : ",num1 ^ num2)
print("num1.symmetric_difference(num2) : ",num1.symmetric_difference(num2))



