'''
  2023 09 13
  김명규
  이동거리 구하기 평균 시속과 이동 시간을 입력으로 받아 다음과 같이 이동시간은 시간 ,분,초 단위로 출력하고
  이동한 거리를 계산하여 출력
'''
# 변수 선언
avgSpeed = float(input('평균 시속(km/h)를 입력하세요'))
hour = float(input('이동 시간(h)을 입력하세요'))

# 연산
distance = avgSpeed * hour

# 시간, 분, 초 계산
seconds = int((hour * 3600) % 60)
minutes = int((hour * 60) % 60)
hours = int(hour)

# 출력
print('평균 시속 : ',avgSpeed)
print('이동 시간 : ', hours, '시간', minutes, '분', seconds, '초')
print('이동거리 : {} km',format(distance))
