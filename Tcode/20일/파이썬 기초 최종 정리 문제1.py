# #반복문 연습1
# #문제1
# N = int(input("수입력: "))
# if N % 2 == 0:
#         print("짝수")
# else:
#         print("홀수")

# #문제2
# N = int(input("수입력: "))
# for i in range(1,N+1):
#         if i % 2 == 0:
#                 print("짝수")
#         else:
#                 print("홀수")

# #문제3
# N = int(input("수입력: "))
# a,b = 0,0
# for i in range(1,N+1):
#         if i % 2 == 0:
#                 a += i
#         else:
#                 b += i
# print("짝수의 합:{} \t 홀수의 합:{}".format(a,b))

# #문제4
# a = []
# N = int(input("수입력: "))
# a.append(N)
# print(a)

# #문제5
# a = []
# N = int(input("수입력: "))
# for i in range(1,N+1):
#         a.append(i)
# print(a)


# #문제6
# a = []
# N = int(input("수입력: "))
# for i in range(1,N+1):
#         if i % 2 == 1:
#                 a.append(i)
# print(a)

# #문제7
# N = int(input("수입력: "))
# if N % 3 == 0:
#         print("{}은(는) 3의 배수입니다.".format(N))
# else:
#         print("{}은(는) 3의 배수가 아닙니다.".format(N))


# #문제8
# N = int(input("수입력: "))
# for i in range(1,N+1):
#         if i % 3 == 0:
#                 print("{}은(는) 3의 배수입니다.".format(i))


# #문제9 
# N = int(input("몇일?: "))
# if N % 4 == 1:
#         print("A가 당번")
# elif N % 4 == 2:
#         print("B가 당번")
# elif N % 4 == 3:
#         print("C가 당번")
# else:
#         print("D가 당번")    

# #문제10 
# N = int(input("몇일?: "))
# for i in range(1,N+1):
#         if i % 4 == 1:
#                 print("A가 당번")
#         elif i % 4 == 2:
#                 print("B가 당번")
#         elif i % 4 == 3:
#                 print("C가 당번")
#         else:
#                 print("D가 당번")    

# #보너스
# for i in [2031,39401,293619,2382837,33828301]:
#         if i % 4 == 1:
#                 print("A가 당번")
#         elif i % 4 == 2:
#                 print("B가 당번")
#         elif i % 4 == 3:
#                 print("C가 당번")
#         else:
#                 print("D가 당번")

# #문제11
# N = int(input("몇년?: "))
# if (N % 4 == 0 and N % 100 != 0) or N % 400 == 0:
#         print("{}년은 윤년 입니다.".format(N))
# else:
#         print("{}년은 윤년이 아닙니다.".format(N))        

# #문제12
# N = int(input("몇년?: "))
# for i in range(1,N+1):
#         if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
#                 print("{}년은 윤년 입니다.".format(i))
#         else:
#                 print("{}년은 윤년이 아닙니다.".format(i))

# #반복문 연습2

# #문제13
#방법1
# for i in range(4):
#         N = int(input("수입력: "))
#         if N % 2 == 0:
#                 print("{}은(는) 짝수".format(N))
#         else:
#                 print("{}은(는) 홀수".format(N))

# #방법2
# for i in [1,1,1,1]:
#         N = int(input("수입력: "))
#         if N % 2 == 0:
#                 print("{}은(는) 짝수".format(N))
#         else:
#                 print("{}은(는) 홀수".format(N))

# #방법3
# i = 0
# while i < 4:
#         N = int(input("수입력: "))
#         if N % 2 == 0:
#                 print("{}은(는) 짝수".format(N))
#         else:
#                 print("{}은(는) 홀수".format(N))
#         i += 1

# #문제14
# a = []
# for i in range(4):
#         N = int(input("수입력: "))
#         a.append(N)
# for i in a:
#         if i % 2 == 0:
#                 print("{}은(는) 짝수".format(N))
#         else:
#                 print("{}은(는) 홀수".format(N))

# #문제15
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = a % 10 + b % 10

# if c >= 10:
#         print("올림발생")
# else:
#         print("올림발생X")

# #문제16
# #방법1
# for i in range(5):
#         a = int(input("수입력: "))
#         b = int(input("수입력: "))
#         c = a % 10 + b % 10

#         if c >= 10:
#                 print("올림발생")
#         else:
#                 print("올림발생X")

# #방법2
# i = 0
# while i < 5:
#         a = int(input("수입력: "))
#         b = int(input("수입력: "))
#         c = a % 10 + b % 10

#         if c >= 10:
#                 print("올림발생")
#         else:
#                 print("올림발생X")
#         i += 1

# #문제17
# a = []
# for i in range(5):
#         N = int(input("점수 입력: "))
#         a.append(N)
# avr = sum(a)/len(a)
# print("5개 점수의 평균은 {}입니다.".format(avr))

# #문제18
# #방법1
# a = []
# for i in range(5):
#         N = int(input("점수 입력: "))
#         a.append(N)
#         avr = sum(a)/len(a)
# print("5개 점수의 평균은 {}입니다.".format(avr))
# for i in a:
#         if avr >= i:
#                 print("{}는 평균이하".format(i))


# #방법2
# a = []
# for i in range(5):
#         N = int(input("수 입력: "))
#         a.append(N)
# # print(a)
# b = 0
# for i in a:
#         b += i
# print("평균은{}입니다.".format(b/5))
# avr = b/5
# for i in a:
#         if i <= avr:
#                 print("{}는 평균이하".format(i))

# #문제19
# a = float(input("수입력: "))
# b = float(input("수입력: "))
# c = a % 1 + b % 1
# if c >= 0.5:
#         print("반올림발생")
# else:
#         print("반올림 발생X")

# #문제20
# for i in range(5):
#         a = float(input("수입력: "))
#         b = float(input("수입력: "))
#         c = a % 1 + b % 1
#         if c >= 0.5:
#                 print("반올림발생")
#         else:
#                 print("반올림 발생X")

# #문제21
# seat = [[0,0,0,0,0,0,0,0,0,0],\
#         [0,0,0,0,0,0,0,0,0,0],\
#         [0,0,0,0,0,0,0,0,0,0],\
#         [1,1,1,0,0,0,0,0,1,0],\
#         [0,1,0,0,0,0,1,0,1,0],\
#         [0,0,0,0,0,0,0,1,0,0],\
#         [1,0,1,0,0,0,0,0,0,1],\
#         [0,0,0,0,0,0,0,0,1,1],\
#         [0,1,1,0,0,0,0,0,0,0]]

# for i in range(len(seat)): #세로 9개
#         for j in range(len(seat[i])): #가로 10개
#                 if seat[i][j] == 0:
#                         print("{}".format("□"),end =" ")
#                 else:
#                         print("{}".format("■"),end =" ")
#         print()
# print("\n※예약가능:■,예약불가:□")

# #문제22 
# 관리자 = ("admin","12345")
# id = input("관리자 아이디를 입력하세요: ")
# password = input("관리자 비밀번호를 입력하세요: ")

# if id == 관리자[0] and password == 관리자[1]:
#     print("관리자 계정으로 로그인에 성공하셨습니다.")
# else:
#     print("아이디 또는 비밀번호를 잘못 입력하셨습니다.")

# #문제23
# 관리자 = {"id":"admin","password":"12345"}
# id = input("관리자 아이디를 입력하세요: ")
# password = input("관리자 비밀번호를 입력하세요: ")

# if id == 관리자["id"] and password == 관리자["password"]:
#     print("관리자 계정으로 로그인에 성공하셨습니다.")
# else:
#     print("아이디 또는 비밀번호를 잘못 입력하셨습니다.")

# #문제24
# word = {"사과":"apple","바나나":"banana","책":"book","학생":"student","책상":"desk"}

# for i in word:
#     j = input("{}에 해당하는 영어 단어 입력: ".format(i))
#     if j == word[i]:
#         print("정답!")
#     else:
#         print("틀렸습니다!")

# #문제25 
# #네비게이션 즐겨찾기 등록 프로그램
# navi = {}
# while True:
#     print("===즐겨찾기 등록===")
#     print("1.주소 등록")
#     print("2.주소 수정")
#     print("3.주소 목록")
#     print("4.검색")
#     print("5.종료")
#     num = int(input("번호 선택: "))
#     if num == 1:
#         name = input("목적지 이름을 입력해주세요: ")
#         if navi.get(name) == None:
#             navi[name] = input("목적지 주소를 입력하세요: ")
#             print("등록 완료 되었습니다.")
#         else:
#             print("입력하신 목적지는 이미 존재 합니다.")
#     elif num ==2:
#         name = input("수정하실 목적지 이름을 입력해주세요: ")
#         if navi.get(name) == None:
#             print("잘못입력하셨습니다.")
#         else:
#             navi[name] = input("수정하실 목적지 주소를 입력하세요: ")
#             print("수정 완료 되었습니다.")
#     elif num == 3:
#         for a,b in navi.items():
#             print(a,"\t",b)
#     elif num == 4:
#         name = input("검색하실 목적지 이름을 입력해주세요: ")
#         if navi.get(name) == None:
#             print("입력하신 목적지는 존재하지 않습니다.")
#         else:
#             print(navi.get(name)) 
#     elif num == 5:
#         print("프로그램을 종료 합니다.")
#         break
#     else:
#         print("번호를 다시 입력해주세요.")


# #문제26
# def apeach():
#     print("과일 종류 : 복숭아")
#     print("효능 : 피로회복")
#     print("제철 : 6 ~ 8월")

# apeach()    

# #문제27
# def 증가(a):
#     print(a+1)
# def 감소(a):
#     print(a-1)
#
# 증가(10)
# 감소(10)

# #문제28
# def 증가(a):
#     return a+1
# def 감소(a):
#     return a-1

# print(증가(10))
# print(감소(10))

# #문제29
# def calc(num1,num2,op):
#     if op == "+":
#         return num1 + num2
#     elif op == "-":
#         return num1 - num2
#     elif op == "*":
#         return num1 * num2
#     elif op == "/":
#         return num1 / num2


# print(calc(1,2,"+"))
# print(calc(1,2,"p"))

# #문제30
# #문제5
# # vsum 함수를 만들어 인자로 전달된 모든 값을 더하는 함수를 만드시오.

# # 사용예시) vsum(1,2) 결과값: 3
# #        vsum(1,2,3) 결과값:6
# #        vsum(1,2,3,4,5) 결과값:15
# def vsum(num1 = 0,num2 = 0, num3 = 0, num4 = 0, num5 = 0):
#         lst = []
#         lst.append(num1)
#         lst.append(num2)
#         lst.append(num3)
#         lst.append(num4)
#         lst.append(num5)
#         sum = 0
#         for i in lst:
#                 sum += i
#         return sum

# print(vsum(1,2))
# print(vsum(1,2,3))
# print(vsum(1,2,3,4,5))

# #[*인자 사용]
# def vsum(*num1):
#         a = 0
#         for i in num1:
#                 a += i
#         return a

# print(vsum(1,2))
# print(vsum(1,2,3))
# print(vsum(1,2,3,4,5,6,7,8,9,10))


