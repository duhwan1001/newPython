# #문제3

# from random import random

# while True:
#     a = int((random()*15)+1)
#     b = int((random()*15)+1)
#     c = int((random()*15)+1)
#     if a != b and a != c and b != c:
#         print(a,b,c)
#         break

# import time
# import os
# import turtle
# s = turtle.Screen()
# im1 = "d:\\a.gif"
# im2 = "d:\\b.gif"

# s.addshape(im1)
# s.addshape(im2)

# print("동전 던지기 게임을 시작합니다.")

# from random import random
# a = int(random()*2)

# t1 = turtle.Turtle()
# if  a == 0:
#     print("앞면입니다!")
#     t1.shape(im1)
#     time.sleep(3)
#     os.system("cls")
# else:
#     print("뒷면입니다!")
#     t1.shape(im2)
#     time.sleep(3)
#     os.system("cls")

#정리하기문제1
#별찍기
#1단계(위)
# ★
# ★★
# ★★★
# ★★★★
# ★★★★★

# while True:
#     a = int(input("수입력: "))
#     for i in range(1,a+1,1):
#         print("★"*i)
#     break

#2단계(아래)
# ★★★★★
# ★★★★
# ★★★
# ★★
# ★

# while True:
#     a = int(input("수입력: "))
    # for i in range(a,0,-1):
    #     print("★"*i)
#     break

# # 3단계 (위 + 아래)

# while True:
#     a = int(input("수입력: "))
#     for i in range(1,a+1,1):
#         if i % 2 == 1:
#             print(" "*(a-i)+"★"*i)
#     for i in range(a-1,0,-1):
#         if i % 2 == 1:
#             print(" "*(a-i)+"★"*i)
#     break

# #정리하기 문제2
# rice = 100*1000
# mouse = 2
# day = 1
# while True:
#     rice -= mouse*20
#     if day % 10 == 0:
#         mouse *= 2
#     if rice <= 0:
#         break
#     day += 1
# print("{}일\t{}마리".format(day,mouse))
