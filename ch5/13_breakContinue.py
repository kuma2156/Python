'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    break 와 continue
    교재 137페이지
'''

word = input("단어를 입력하세요 >> ")
# test word == programming


print("\n::: break 1 :::")
for i in word: # word 안의 단어까지 반복
  if i == 'a' or i =='i' or i =='e'  or i =='o' or i =='u' : # 해당 단어를 만나면 반복문 종료
    break
  else : # 해당하는 단어가 아닐 경우 출력
    print(i , end='')# 결과 pr

print("\n::: break 2 :::")
for i in word: # word 안의 단어까지 반복
  if i in ['a','i','e','o','u','A','I','E','O','U']: # 리스트를 만들어 해당하는 값이 있으면 break 실행
    break
  else : # 해당하는 단어가 아닐 경우 출력
    print(i , end='')# 결과 pr

print("\n::: continue :::")
for i in word: # word 안의 단어까지 반복
  if i in ['a','i','e','o','u','A','I','E','O','U']: # 리스트를 만들어 해당하는 값이 있으면 
    continue # 반복문을 종료시키지 않고 인덱스를 증가시키고 처음으로 돌아간다.
  print(i , end='')# 결과 prgrmmng