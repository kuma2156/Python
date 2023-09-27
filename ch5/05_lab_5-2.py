'''
    2023-09-27
    201795016 김명규
    range() 사용
    터틀 그래픽으로 n 각형 도형 그리기
    사용자로부터 그리고 싶은 도형의 변의 갯수를 입력받아 도형을 그린다.
'''
#터틀 모듈을 사용하기 위해 준비
import turtle as t
# turtle 클래스 객체를 t로 생성(별명)

# 펜 이동 / 펜 자국을 남지 않도록 들어서 이동
t.penup()
t.goto(-50,-50) # 이동
t.pendown() # 이동을 마치면 펜을 내려 놓는다. 그래야 그림을 그릴 수 있다.

# 모양 터틀
t.shape('turtle')

# 입력값을 정수로 자료형으로 변경하고 연산
shape = int(input('몇각형 도형을 그릴까요? >> '))
rangle = 360 / shape

# 반복문으로 입력받은 도형 그리기 (5번)
for r in range(5) :
  for i in range(shape):
    t.forward(100)
    t.left(rangle)

  t.left(10)
# 종료되지 않게 방지
t.done()