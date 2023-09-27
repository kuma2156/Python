'''
    2023-09-27
    201795016 김명규
    range() 사용
    터틀 그래픽으로 여러개의 원을 그려보자
'''

#터틀 모듈을 사용하기 위해 준비
import turtle as t
# turtle 클래스 객체를 t로 생성(별명)

# 모양 터틀
t.shape('turtle')

# 원 하나 그리기
# 반지름이 100인 원
#t.circle(100)

# 반복문을 사용
for i in range(10) :
  t.left(360 / 10)
  t.circle(100)

# 종료되지 않게 하기
t.mainloop() # or t.done()