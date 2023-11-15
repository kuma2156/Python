'''
    2023-11-15
    201795016 김명규
    문자열 슬라이싱
'''
# 문자열 슬라이싱
s = "Happy Day!"

# 문자열의 0번지
print(s[0])
print(s[6:10])
print(s[:-2])

# 문자열 분리 : split()
s = "Welcome to Python"
print(s.split()) # 공백을 기준으로 분리 리스트형태

s = '2023-11-15'
print(s.split('-')) # - 을 기준으로 분리 리스트형태 

s = 'Hello, World!'
print(s.split(',')) # ,을 기준으로 분리 리스트형태 World 앞에 공백이 남았다.
print(s.split(', ')) # , 을 기준으로 분리 리스트형태 공백도 분리 기준으로 넣어줌

# 공백제거 strip()
s= "Welcome, to, Python, and , dding,      pong"
print(s.strip())
print([x.strip() for x in s.split(',')]) # 반복문을 사용하여 공백과 쉼표를 문자열에서 제거

print(list('hello, world!')) # 리스트에 모든 문자열을 하나씩 나누어서 저장

# 문자열 연결 join()
print(','.join(['apple','water melon','melon'])) # , 를 붙여서 연결하라
print('-'.join('010.1234.5678'.split('.'))) # .을 기준으로 나누어주고 -로 연결

# . 을 -로 변경
print('010.1234.5678'.replace('.','-')) # 문자열의 .을 -로 변경

s = "Hello World!"
print(s)

# 리스트로 문자열 분리 시켜 slist에 저장
slist = list(s)
print(slist)
# 분리된 문자를 다시 합치기
print(''.join(slist)) 

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as well, \n\t Have a Happy Day.'
print(a_string)

# 문자열 자르기 word_list 에 저장
word_list = a_string.split()
print(word_list)
# 다시 합치기 : 문자열을 자르고 다시 합치면 줄바꿈과 탭이 없어진다..
refind_string = ' '.join(word_list)
print(refind_string)

# 대소문자 변환과 문자열 삭제
s = "Hello World!"
print(s)
print(s.lower()) # 문자열을 모두 소문자로 바꾸기
print(s.upper()) # 문자열을 모두 대문자로 바꾸기

# 공백제거 strip()
s = '      Hello, World!'
print(s.strip()) # 왼쪽, 오른쪽 모든 공백을 제거
print(s.lstrip()) # 왼쪽 공백제거 left
print(s.rstrip()) # 오른쪽 공백제거 right

s = '######Hello, World!#########'
print(s)
print(s.strip('#')) # 왼쪽, 오른쪽 모든 # 제거

# 문자열 찾기
s = 'www.silla.ac.kr'
print(s)
# .kr 을 찾고 싶다.
print(s.find('.kr')) # 번지수를 리턴한다. .이 시작하는 번지 12번지이다.
print(s.find('x')) # 없는 값을 찾을려면 -1이 리턴한다.

# . 몇개인가.
print(s.count('.')) # count() 로 찾아준다.