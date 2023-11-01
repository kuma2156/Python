'''
    2023-11-01 
    201795016 김명규
    8.1 키와 값을 가지는 딕셔너리
    
    튜플 = () 리스트 = [] 딕셔너리 = {}

    lab 8-1
    편의점 재고 관리 프로그램
'''
items = {"커피음료" : 7,"종이컵" : 2,"우유" : 1,"콜라" : 4,"책" : 5}

# 물건의 목록 출력
print(f"::: 물건의 목록 :::")
for key in items.keys() :
  print(key , end=', ')

# 물건의 이름을 입력
inputName = input("\n물건의 이름을 입력 하세요 >> ")


# 입력받은 이름으로 출력
if inputName in items :
  print(f"{inputName} 재고는 : {items[inputName]}")
else :
  print(f"{inputName}은(는) 재고 목록에 없습니다.")
