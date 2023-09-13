'''
  2023 09 13
  김명규
  피자의 면적을 구하기
'''
# 피자의 반지름 필요 (입력받아 계산)
radius = int(input('피자의 반지름을 입력해주세요'))

# 연산
pizza = (radius ** 2) * 3.14

# 출력
print('반지름이 {} 인 피자의 면적은 {:.2f} 입니다. '.format(radius,pizza))

