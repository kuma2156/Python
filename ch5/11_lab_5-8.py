'''
    2023-10-04
    201795016 김명규
    조건에 따라 반복하는 while 문
    lab 5-8
    while 문으로 별 그리기
'''

input = int(input("입력한 수 만큼 별을 그리겠습니다! >> : "))

import turtle as t

# 모양 터틀
t.shape('turtle')
i = 0
while i < input :
  t.forward(150)
  t.right(140)
  i += 1 