'''
    2023-10-18
    201795016 김명규
    리스트 만들기
    lab 7-1
    입력을 받아 과일의 리스트를 만들자.

    좋아하는 과일 5개를 입력받아 리스트에 저장합니다.
    과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단.

    추가 append() 메소드
    판단 in 연산자 
'''

# 빈 리스트 생성
fruits = []

for i in range(5):
    insert = input(f"{i+1}. 과일을 입력하세요 >> : ")
    fruits.append(insert)

print(f'과일 목록 : {fruits}')

# 찾기
fav_fruit = input("좋아하는 과일을 입력하세요 >> : ")
isFavorite = fav_fruit in fruits

print(f":: 과일 목록에 {fav_fruit}이(가) 있나요? ::")
if (isFavorite) :
  print("좋아하는 과일이 존재하는 군요!")
else :
  print("좋아하는 과일이 존재하지 않습니다.")
   