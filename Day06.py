# Quiz3. input() 함수를 사용하여 한 변의 길이 값을 입력 받아 정육면체를 그리는 코드를 작성하시오
# import turtle as t
# length = int(input("변의 길이를 입력하세요 >>"))
# t.left(60)
# t.forward(length)
# t.left(60)
# t.forward(length)
# t.left(60)
# t.forward(length)
# t.left(60)
# t.forward(length)
# t.left(60)
# t.forward(length)
# t.left(60)
# t.forward(length)
# t.mainloop()

# Quiz4. input() 함수를 사용하여 한 변의 길이 값을 입력 받아 별을 그리는 코드를 작성하시오
# import turtle as t
# length = int(input("변의 길이를 입력하세요 >>"))
# angle = 144
# t.right(angle)
# t.forward(length)
# t.right(angle)
# t.forward(length)
# t.right(angle)
# t.forward(length)
# t.right(angle)
# t.forward(length)
# t.right(angle)
# t.forward(length)
# t.mainloop()

# 실습) 아무거나 그려보기(검색ㄱ)
# import turtle as t
# t.pensize(20)
# t.circle(25)
# t.penup()
# t.left(90)
# t.forward(28)
# t.right(90)
# t.forward(25)
# t.pendown()
# t.forward(100)
# t.penup()
# t.right(90)
# t.forward(28)
# t.left(90)
# t.forward(25)
# t.pendown()
# t.circle(25)
# t.penup()
# t.forward(200)
# t.mainloop()

# print(True)
# print(False)

# print(10 == 100)
# print(10 != 100)
# print(10 > 100)
# print(10 < 100)
# print(10 >= 100)
# print(10 <= 100)

# print("가방" < "하마")
# print("가방" > "하마")

# print(not False)
# print(not True)

# x = 10
# y = 20

# print(not x == y)
# print(not x != y)

# # 둘다 True 일때만 True
# print(True and True)
# print(True and False)
# print(False and True)   
# print(False and False)

# # 하나라도 True 이면 True
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# num = int(input("정수 1개를 입력하세요>> "))
# if num == 1:
#     print("정수가 1입니다")

# # 조건식이 True 또는 False가 올경우
# # True 입니다. False 입니다 라는 문자열이 출력되게 하시오.
# if True:
#     print("True입니다.")
# if False: # 조건식이 False면 출력되지 않는다.
#     print("False입니다.")

# Quiz1. 정수입력 받아서 양수 음수 구분하는 프로그램 작성

    # num = int(input("숫자를 입력하세요>> "))
    # print("입력하신 숫자 : {}".format(num))
    # if num > 0:
    #     print("입력하신 숫자는 양수입니다")
    # if num < 0:
    #     print("입력하신 숫자는 음수입니다")
    # if num == 0:
    #     print("입력하신 숫자는 0입니다")

# Quiz2. 정수입력 받아서 끝자리로 짝수 홀수 구분하는 프로그램
# num = int(input("숫자를 입력하세요>> "))
# print("입력하신 숫자 : {}".format(num))
# lastNum = num % 10
# if lastNum % 2 == 0:
#     print("입력하신 숫자는 짝수입니다")
# if lastNum % 2 != 0:
#     print("입력하신 숫자는 홀수입니다")

# Quiz2. 정수입력 받아서 짝수 홀수 구분하는 프로그램
# num = int(input("숫자를 입력하세요>> "))
# print("입력하신 숫자 : {}".format(num))
# if num % 2 == 0:
#     print("입력하신 숫자는 짝수입니다")
# if num % 2 != 0:
#     print("입력하신 숫자는 홀수입니다")
    
