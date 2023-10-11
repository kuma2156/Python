'''
    2023-10-11
    201795016 김명규
    함수
    def 예약어를 이용하여 함수를 만들고 호출하기
    
    함수의 defalut 인자
'''

def order(num,pickle , onion) :
  print("햄버거 {}개 ,피클{}, 양파{}" . format(num,pickle,onion))

#order(1)  #인자는 1개인데 매게변수는 3개이기에 오류 발생

# 인자가 부족한 경우 기본값을 넣어주는 것 => 디폴트 인자
def order2(num,pickle='기본' , onion='기본') :
  print("햄버거 {}개 ,피클{}, 양파{}" . format(num,pickle,onion))

order2(2)
order2(1,pickle='뺌')