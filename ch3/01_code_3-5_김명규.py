'''
  2023 09 13
  김명규
  직각 삼각형의 빗변의 길이를 구하시오
'''
# 입력 및 선언
height = int(input('직각 삼각형의 높이를 입력하세요'))
line = int(input('직각 삼각형의 및변을 입력하세요'))

# 연산
import math
result = math.sqrt(height**2 + line**2 )

# 출력
print('높이{} 밑변 {} 인 직각삼각형의 빗변의 길이는 {:.2f} 입니다.'.format(height,line,result))
