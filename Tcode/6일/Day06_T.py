# 폴더클릭후 => CODE로 열기 
# 새파일 만들기
# https://mgr.kgitbank.com/

# #문제3
# import turtle as t
# a = int(input("길이 입력: "))
# t.shape("turtle")
# t.left(60)
# t.forward(a)
# t.left(60)
# t.forward(a)
# t.left(60)
# t.forward(a)
# t.left(60)
# t.forward(a)
# t.left(60)
# t.forward(a)
# t.left(60)
# t.forward(a)
# t.mainloop()

# #문제4
# import turtle as t
# a = int(input("길이 입력: "))
# t.shape("turtle")
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.mainloop()

# import turtle as t
# t.shape('turtle') # 이동점 모양을 거북이 형상으로 함
# t.speed('fastest') # 거북이 이동속도를 가장 빠르게.   fastest / fast / normal / slow / slowest 설정 가능

# n=30 # 30번 꺾기
# i=10
# for _ in range(n):
#     t.fd(i)  # t.forward(100) 을 줄여서 t.fd(100) 으로 됨
#     i+=10
#     t.right(90)
# t.mainloop()

# #조건문

# #if => yes / no

# print(True)

# print(False)
# print()

# # 비교 연산자
# print(10 == 100)
# print(10 != 100)
# print(10 > 100)
# print(10 < 100)
# print(10 >= 100)
# print(10 <= 100)

#논리 연산자
# and 그리고
# or 또는
# not 아니다

# #not 연산자
# #참과 거짓을 반대로 바꿀 때 사용
# print(not False)
# print(not True)

# #예제1
# x = 10
# y = 20

# #True
# print(not x == y)
# #False
# print(not x != y)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# 정수 1개를 입력받아 정수가 1인 경우
# # 출력하는 코드 작성
# num1 = int(input("정수 1개 입력: "))
# if num1 == 1:
#     print("입력하신 정수는 1입니다.")

# # 조건식이 True 또는 False가 올경우 
# # True 입니다. False 입니다 라는 문자열이 
# # 출력되게 하시오.

# if True:
#     print("True입니다.")
# if False:
#     print("False입니다.")

# #문제1
# num1 = int(input("수입력: "))
# if num1 > 0:
#     print("{}은 양수".format(num1))
# if num1 < 0:
#     print("{}은 음수".format(num1))
# if num1 == 0:
#     print("0입니다.")

# #문제2 = > 사람

# num1 = int(input("수입력: "))
# num2 = num1 % 10

# #짝수
# if num2 == 0 or num2 == 2 or num2 == 4 or num2 == 6 or num2 == 8:
#     print("{}은(는) 짝수입니다.".format(num1))  
# #홀수
# if num2 == 1 or num2 == 3 or num2 == 5 or num2 == 7 or num2 == 9:
#     print("{}은(는) 홀수입니다.".format(num1))
 
# #문제3
# num1 = int(input("수입력: "))

# if num1 % 2 == 0:
#     print("짝수")
# # if num1 % 2 != 0:
# #     print("홀수")
# if num1 % 2 == 1:
#     print("홀수")





