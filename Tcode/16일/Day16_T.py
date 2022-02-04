# #문제5
# A = ["red","green","yellow","apple","is","delicious"]
# print(A[:3])

# print(A[0],A[3],A[4],A[5])

# #리스트 연산자
# #연결(+) 반복(*) len(길이)
# list_a = ["A","B","C"]
# list_b = ["D","E","F","G","H"]
# print(list_a + list_b)
# print(list_a*3)
# print(len(list_a))

# #문제6 
# a = [1,2,3,4]
# #1번
# A = a[0] + a[1] + a[2] + a[3]
# print(A/4)

# #2번
# print(sum(a))
# print(len(a))

# print(sum(a)/len(a)) # 총합 / 개수 = 평균

# #리스트 함수
# #요소 추가
# list_a = ["A","B","C"]
# print("#append사용해서 뒤에 요소 추가")
# list_a.append("D")
# list_a.append("E")
# print(list_a)

# print("#insert 중간에 요소 추가")
# list_a.insert(0,"추가!")
# print(list_a)

# print("#extend 여러 요소 추가")
# list_a.extend(["F","G","H"])
# print(list_a)

# list_a = ['추가!', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

# print("#리스트의 특정 요소 하나 제거")
# #키워드
# del list_a[0]
# print(list_a)

# print("#리스트의 특정 요소 하나 제거")
# #함수
# list_a.pop()
# print(list_a)

# print("#리스트의 특정 요소 여러개 제거")
# del list_a[1:3]
# print(list_a)

# #값으로 제거
# list_b = [1,2,3,1,2,3,1,2,3]
# print("#리스트 내부에 있는 2제거")
# for i in range(3):
#     list_b.remove(2)
# print(list_b)

# #모두 제거
# list_c = [1,2,3,4,5]

# list_c.clear()
# print(list_c)

# #문제7 
# A = [0,1,2,3,4,5,6,7,8,9]

# A.append(10)
# print(A)

# A.insert(3,0)
# print(A)

# A.extend(A)
# print(A)

# del A[0]
# print(A)

# A.pop(2)
# print(A)

# A.remove(0)
# print(A)

# A.clear()
# print(A)

# #리스트 + For문
# list_1 = [273,32,103,57,52]

# for i in list_1:
#     print(i)

# 

# #리스트 정리하기문제2
# a = [200,101,5,32,64,9,72,900,99,1000]

# for i in a:
#     print("a의 자리수는 {} 입니다.".format(len(str(i))))

# #리스트  정리하기 문제3
# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# b = [[],[],[]]

# for i in a:
#     b[(i+2)%3].append(i)
# print(b)

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# b = [[],[],[],[]]

# for i in a:
#     b[(i+3)%4].append(i)
# print(b)


# #딕셔너리

# dict_a = {"name":"펭수","age":20}
# print(dict_a)

# #name값
# print(dict_a["name"])
# #age값
# print(dict_a["age"])


# #딕셔너리 + 리스트 사용
# dict_b = {"workmate":["뚝딱이","범이","뿡뿡이","번개맨","EBS사장님"]}
# print(dict_b)

# #예제1 
# #특정 키의 값 출력
# #선언
# dict_c = {
#     "name":"펭수",
#     "age" : 20,
#     "workmate":["뚝딱이","범이","뿡뿡이","번개맨","EBS사장님"],
#     "birthplace":"남극"
# } 

# #출력
# print(dict_c["name"])
# print(dict_c["age"])
# print(dict_c["workmate"])
# print(dict_c["birthplace"])

# #리스트의 값 "범이" 출력
# print(dict_c["workmate"])
# print(dict_c["workmate"][1])

# #값변경
# dict_c["name"] = "펭구"
# print(dict_c["name"])

# #새로운 키 - 값 추가
# dict_c["like food"] = "동원참치"
# print(dict_c)

# #기존의 값을 새로운 값으로 대치
# dict_c["like food"] = "물고기"
# print(dict_c)

# #특정 키의 값 제거
# del dict_c["like food"]
# print(dict_c)