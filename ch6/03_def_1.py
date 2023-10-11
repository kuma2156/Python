'''
    2023-10-11
    201795016 김명규
    함수
    def 예약어를 이용하여 함수를 만들고 호출하기
    
    두 수를 입력받아 함수를 호출하여 두 수 사이의 합을 계산하여 돌려주는 함수
'''

'''
  [알고리즘]
  1. 두 수를 입력받는다.
  2. 함수를 만든다(입력받은 인자를 매게변수로 저장하고 연산 후 리턴)
  3. 입력받은 두 수를 인자로 함수로 넘겨준다.(result 변수에 리턴값을 저장)
  4. 출력
'''




#  2. 함수를 만든다.(입력받은 인자를 매게변수로 저장하고 연산 후 리턴)
def addNum(start,end) :
  sum = 0
  if start > end :
    temp = end
    end = start
    start = temp
  for i in range(start,end+1) :
    sum += i
  return sum

#  메인
#  1. 두 수를 입력받는다.
inputA = int(input("첫 번째 수 >> : "))
inputB = int(input("두 번째 수 >> : "))
#  3. 입력받은 두 수를 인자로 함수로 넘겨준다.(result 변수에 리턴값을 저장)
result = addNum(inputA,inputB)

#  4. 출력
print(f"입력받은 두 수 사이의 핪은 {result}")