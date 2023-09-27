'''
    2023-09-27
    201795016 김명규
    선택문 if else
    점수를 입력받아 학점을 출락하시오
    90 100 A
    80 89  B
    70 79  C
    60 69  D
    50 59  F
             학점

'''

# 선언 및 초기화
inputScore = int(input("학점을 입력하시오 : >> "))


# 첫번째 학점 계산
print("::: 첫 번째 학점 계산 :::")
if inputScore >= 90 and inputScore <= 100 :
  print(f"학점 {inputScore} 은 A학점입니다.")
elif inputScore >= 80 and inputScore <= 89 :
    print(f"학점 {inputScore} 은 B학점입니다.")
elif inputScore >= 70 and inputScore <= 79 :
    print(f"학점 {inputScore} 은 C학점입니다.")
elif inputScore >= 60 and inputScore <= 69 :
    print(f"학점 {inputScore} 은 D학점입니다.")
else :
  print(f"학점 {inputScore} 은 F학점입니다.")

# 문제점 : 100점을 초과하거나 음수를 입력할 경우 F 학점으로 출력된다 

# 문제 해결 2
# 정확한 범위를 입력해준다.
print("::: 두 번째 학점 계산 :::")
if 90 <= inputScore <= 100 :
  print(f"학점 {inputScore} 은 A학점입니다.")
elif inputScore >= 80 and inputScore <= 89 :
    print(f"학점 {inputScore} 은 B학점입니다.")
elif inputScore >= 70 and inputScore <= 79 :
    print(f"학점 {inputScore} 은 C학점입니다.")
elif inputScore >= 60 and inputScore <= 69 :
    print(f"학점 {inputScore} 은 D학점입니다.")
elif inputScore <= 59 and inputScore > 0 :
  print(f"학점 {inputScore} 은 F학점입니다.")
else :
   print("올바른 값을 입력하세요..")

# 정수는 0 ~ 100 사이야 합니다 이에 해당하지 않으면 잘못된 입력입니다.
print("::: 세 번째 학점 계산 :::")
if(0 <= inputScore <= 100) :
  if 90 <= inputScore <= 100 :
   print(f"학점 {inputScore} 은 A학점입니다.")
  elif inputScore >= 80 and inputScore <= 89 :
    print(f"학점 {inputScore} 은 B학점입니다.")
  elif inputScore >= 70 and inputScore <= 79 :
    print(f"학점 {inputScore} 은 C학점입니다.")
  elif inputScore >= 60 and inputScore <= 69 :
    print(f"학점 {inputScore} 은 D학점입니다.")
  elif inputScore <= 59 and inputScore > 0 :
   print(f"학점 {inputScore} 은 F학점입니다.")

else :
   print("올바른 값을 입력하세요..")