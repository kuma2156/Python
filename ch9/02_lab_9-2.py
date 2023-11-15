'''
    2023-11-15
    201795016 김명규
    문자열 슬라이싱
    
    lab 9-2
'''

text = "There's a reason some people are working to make it harder to vote, especially for people of color. It’s because when we show up, things change."

# 띄어쓰기로 문자열을 분리하고 , 단어의 개수를 찾아라
'''
new_text = text.split() # 띄어쓰기로 문자열을 분리 new_text 
print(f"공백을 기준으로 분리 : {new_text}")
len_text = len(new_text) # 단어의 개수 len_text
print(f"단어의 개수 : {len_text}")
'''
# 도전문제 9.1 회사명을 *** 로 처리하자.
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

spt_text = text.split()

for index, word in enumerate(spt_text): # 나누어준 문자열을 인덱스와 단어로 반복문을 돌려
    if word.lower() in ['kt', 'samsung', 'lg', 'skt']: # 소문자로 바꾼 단어가 해당 단어에 해당된다면
        spt_text[index] = '***' # 그 문자열 인덱스번지에 값을 * 로 변환
        
        
# 문자열을 다시 합쳐주기
join_text = ' '.join(spt_text)
print(f':::: 처리 전 텍스트 ::::')
print(text)
print()
print(f':::: 처리 후 텍스트 ::::')
print(join_text)


# 2 소문자로 바꾼 문자열을 공백으로 구분하여 저장하고 회사명이 있을 경우 * 처리 하여 리스트에 저장 아니면 그대로 리스트에 저장
low_text = text.lower()
spt_text = low_text.split()

for index , word in enumerate(spt_text) :
  if word in ['kt','samsung','lg','skt'] :
    spt_text[index] = '*'
  else :
    spt_text[index] = word
    
join_text = ' '.join(spt_text)
print(f"\n\n:::: 2 ::::\n{spt_text}") # 분리된 리스트 그냥 출력