'''
    2023-09-27
    201795016 김명규
    range() 사용

'''
for i in range(3) :
  print(i , end =', ') # 줄바꿈하지 않는다
  print("안녕하세요")
  print("   김명규입니다.")


# range(시작값 , 숫자 앞 까지 , 증가값(감소값))
# for(초기값, 조건식 : , 증감식)

print("::: 1 ~ 5 :::")
# 1 ~ 5
for i in range(1,6) :
  print(i, end =', ')

print("\n::: 10 ~ 1 :::")
# 10 ~ 1
for i in range (10 ,0, -1) :
  print(i, end = ', ')