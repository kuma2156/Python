'''
    2023-11-01
    201795016 김명규
    튜플

    리스트와 달리 안의 항목을 수정할 수 없다.
    lab 7-6

    도시의 이름과 인구를 튜플로 묶어보자. 
'''

# 도시 정보를 담은 튜플의 리스트 생성
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1504), ('대전', 1531)]

# 초기값 설정
max_pop = 0             # 최대 인구 초기값 (0으로 설정)
min_pop = 999999999999  # 최소 인구 초기값 (아주 큰 값으로 설정)
total_pop = 0           # 인구 총합 초기값

max_city = None         # 최대 인구를 가진 도시 정보 (초기값 None)
min_city = None         # 최소 인구를 가진 도시 정보 (초기값 None)

# 도시 정보 순회
for city in city_info:
    total_pop += city[1]  # 도시의 인구를 총 인구에 더함
    if city[1] > max_pop:
        max_pop = city[1]  # 최대 인구 갱신
        max_city = city    # 최대 인구 도시 정보 갱신
    if city[1] < min_pop:
        min_pop = city[1]  # 최소 인구 갱신
        min_city = city    # 최소 인구 도시 정보 갱신

# 결과 출력
print('가장 큰 도시: {0}, 인구 {1}만명'.format(max_city[0], max_city[1]))  # 최대 인구 도시 출력
print('가장 작은 도시: {0}, 인구 {1}만명'.format(min_city[0], min_city[1]))  # 최소 인구 도시 출력
print('평균 인구: {0}만명'.format(total_pop / len(city_info)))  # 평균 인구 출력
