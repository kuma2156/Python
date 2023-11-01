'''
    2023-11-01
    201795016 김명규
    튜플

    리스트와 달리 안의 항목을 수정할 수 없다.
'''
# 리스트 생성
color_list = ["red","green","blue"]
# 튜플 생성
colors = ("red","green","blue","orange")

# 튜플 출력
print(f"colors = {colors}")

# color 튜플에 black 추가 하기.
# AttributeError: 'tuple' object has no attribute 'append' 에러발생!
#colors.append("black")
# tuple 에 append 라는 속성이 존재하지 않는다. 왜냐 수정이 불가능한 그릇이여서

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print("color 튜플 : ",colors)
print("color 튜플의 2,3,4번은? : ", colors[1:4])

print("color 튜플의 1,2,3번은? : ", colors[:3])
print("color 튜플의 3~번은? : ", colors[2:])
print("color 튜플의 1,3,5번은? : ", colors[::2])
#                                   0 부터 끝까지 2씩 증가 < 0 : 끝 : 2++>

print("color 튜플의 거꾸로는? : ", colors[::-1])

# 튜플끼리의 결합 => + 연산자 . 반복 => * 연산자
colors = colors + colors
print("color 튜플 : ",colors)
print("color 튜플 10번 반복: ",colors * 10 )
