'''
  2023 09 13
  김명규
  터틀 그리기
'''
#터틀 모듈을 사용하기 위해 준비
import turtle as t
# turtle 클래스 객체를 t로 생성(별명)

# 모양 터틀
t.shape('turtle')

# 선그리기
'''
  t.speed(2) 속도
  t.forward(200) 전진
  t.left(120) 120도로 회전
'''

# 삼각형 그리기
'''
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(100)
'''

# 입력값을 정수로 자료형으로 변경하고 연산
shape = int(input('몇각형 도형을 그릴까요?'))
rangle = 360 / shape

# 반복문으로 삼각형 그리기
for i in range(shape):
  t.forward(100)
  t.left(rangle)

# 별그리기
for i in range(5) :
  t.forward(200)
  t.left(144)

# 종료되지 않게 하기
t.mainloop()