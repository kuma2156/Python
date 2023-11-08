'''
    2023-11-08 
    201795016 김명규
    키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}

    집합 set()
      중복을 허용하지 않는다!
      순서가 없다

      lab 8-3
      파티 동시 참석자 알아내기
      2개 파티에 모두 참석한 사람들의 명단을 출력하려면 어떻게 해야 할까?
  
'''

partyA = set(["Park","Kim","Lee"])
partyB = set(["Park","Choi"])

print("::  2개 파티에 모두 참석한 사람들의 명단 :: ")
print(partyA.intersection(partyB))

print("::  2개 파티에 참석한 사람들의 명단 :: ")
print(partyA.union(partyB))

print("::  2개 파티에 중복없이 참석한 사람들의 명단 :: ")
print(partyA.union(partyB) - partyA.intersection(partyB))

print("::  A 파티에 참석한 사람들의 명단 :: ")
print(partyA.union(partyB) - partyB)


