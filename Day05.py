# Quiz8. 123 입력시 => 백의자리 123 십의자리23 일의자리3 출력
# num = int(input("숫자를 3자리 입력하세요 >> "))
# print("입력하신 숫자는 {} 입니다".format(num))
# one = num % 10
# ten = num % 100
# hun = num
# print("백의자리 : {}\n십의자리 : {}\n일의자리 : {}".format(hun, ten, one))

# num1 = int(input("첫번째 숫자 입력 >> "))
# num2 = int(input("두번째 숫자 입력 >> "))
# result = num1 // num2 # / = 실수 값 리턴 || // = 정수 값 리턴
# remain = num1 % num2
# print("{}를 {}로 나누었을 때의\n몫 : {}\n나머지 : {}".format(num1, num2, result, remain))

# print(3/2)  # 실수    
# print(3//2) # 정수
# print(3%2)  # 나머지

# Quiz9. 123 입력시 => 백의자리1 십의자리2 일의자리3 출력
# num = int(input("숫자를 3자리 입력하세요 >> "))
# one = num % 10
# ten = num % 100 // 10
# hun = num // 100
# print("일의자리 : {}\n십의자리 : {}\n백의자리 : {}".format(one, ten, hun))
# print()
# print("역순자리수")
# print()
# one = num // 100
# ten = num % 100 # or //
# hun = num
# print("일의자리 : {}\n십의자리 : {}\n백의자리 : {}".format(one, ten, hun))
# print()
# print("역순자리수 1")
# print()
# one = num // 100
# ten = num % 100 // 10
# hun = num % 10
# print("일의자리 : {}\n십의자리 : {}\n백의자리 : {}".format(one, ten, hun))
# print()

# Quiz10. 생년월일 8자리를 정수로 입력받고. 년, 월, 일을 나눠서 출력하세요
# birthday = int(input("생년월일 8자리를 입력하세요 >> "))
# print(birthday) #0000 00 00

# year = birthday // 10000
# month = birthday % 10000 // 100
# day = birthday % 100
# print("년 : {}\n월 : {}\n일 : {}".format(year, month, day))

# 숫자의 왼쪽 값을 추출하고싶으면 /
# 오른쪽 값을 추출하고 싶으면 %

# Quiz11. 생년월일 6자리를 정수로 입력받고. 년, 월, 일을 나눠서 출력하세요
# birthday = int(input("생년월일 6자리를 입력하세요 >> "))
# print(birthday) #0000 00 00

# year = birthday // 10000
# month = birthday % 10000 // 100
# day = birthday % 100
# print("년 : {}\n월 : {}\n일 : {}".format(year, month, day))

# Quiz12. 0-9까지 10자리를 정수로 입력받고, 반을 나눠서 출력하시오
# num = int(input("숫자를 10자리 입력하세요 >> "))
# firstHalf = num // 100000
# secHalf = num % 100000
# print("입력한 숫자 : {}\n1-5자리의 수 : {}\n6-10자리의 수 : {}".format(num, firstHalf, secHalf))

# turtle(그래픽 모듈)
# # 호출 
# import turtle
# # 모양 설정
# turtle.shape("turtle")
# # 이동
# turtle.left(90)
# turtle.forward(100)
# # 유지
# turtle.mainloop()

# 예제1. 위로 줄긋기
# import turtle as t
# turtle.shape("turtle")
# turtle.left(90)
# turtle.forward(100)
# turtle.mainloop()

# 예제2. 삼각형 그리기
# import turtle as t
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.mainloop()

# Quiz1. input() 함수를 사용하여 한 변의 길이 값을 입력 받아 정삼각형을 그리는 코드를 작성하시오
# import turtle as t
# length = int(input("변의 길이를 입력하세요 >>"))
# t.forward(length)
# t.left(120)
# t.forward(length)
# t.left(120)
# t.forward(length)
# t.mainloop()

# Quiz2. input() 함수를 사용하여 가로, 세로 길이 값을 입력 받아 사각형을 그리는 코드를 작성하시오.
import turtle as t
hor = int(input("가로의 길이를 입력하세요 >>"))
ver = int(input("세로의 길이를 입력하세요 >>"))
t.forward(hor)
t.left(90)
t.forward(ver)
t.left(90)
t.forward(hor)
t.left(90)
t.forward(ver)
t.mainloop()


