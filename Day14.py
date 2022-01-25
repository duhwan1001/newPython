# from random import random

# while True:
#     a = int(random()*15)+1
#     b = int(random()*15)+1
#     c = int(random()*15)+1
#     if a != b and a != c and b != c:
#         print(a, b, c)
#         break
#     continue

# import time
# import os
# import turtle
# s = turtle.Screen()
# im1 = "c:\\a.gif"
# im2 = "c:\\b.gif"


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
        
# 문제1. 별 찍기, while문을 이용하여 입력받은 수 라인 만큼 마름모 형태의 별 만들기

#         ★ # 8
#       ★★★ # 6
#     ★★★★★ # 4
#   ★★★★★★★ # 2
# ★★★★★★★★★
#   ★★★★★★★
#     ★★★★★
#       ★★★
#         ★

# a = int(input("숫자 입력 >> "))
# i = 0
# while True:
#     inc = a % 2
#     dec = 0
#     bs = a - 1
#     for i in range(a):
#         print()
#         if inc != a:
#             print(" " * bs, end="★" * inc)
#             inc += 2
#             bs -= 2
#             dec = inc
#         else:
#             print(" " * bs, end="★" * dec)
#             dec -= 2
#             bs += 2
#     print()
#     i += 1
#     if i == a:
#         break

# T 풀이
# while True:
#     a = int(input(""))
#     for i in range(1, a+1, 1):
#         if i % 2 == 1:
#             print(" " * (a-i) + "★" * i)
#     for i in range(a-1, 0, -1):
#         if i % 2 == 1:
#             print(" " * (a-i) + "★" * i)
#     break

# 문제2. 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한 마리가 하루에 20g씩의 쌀을 먹고 10(10,20,30) 마다 쥐의 수가 2배 증가한다
#        먀칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇마리 인가?
#        쌀 한통 = 1kg (쌀을 먹은 후 2배 증가하는 조건)


# rice = 100000
# ratCnt = 2
# ratEat = 20
# dailyEat = ratCnt * ratEat
# day = 0

# while True:
#     day += 1
#     rice -= dailyEat
#     if day % 10 == 0:
#         ratCnt *= 2
#     if rice < 0:
#         break
# print("쌀 : 0\n소모되는데 걸린 시간 : {}일\n쥐 개체수 : {}".format(day, ratCnt))

# currentMoney = 0
# inputMoney = 0
# change = 0
# while True:
#     print()
#     print("--- Menu ---")
#     print("1. 콜라 / 300")
#     print("2. 사이다 / 300")
#     print("3. 커피 / 200")
#     print("4. 돈 넣기")
#     print("5. 잔돈 반환")
#     print("6. 종료")
#     print("------------")
#     print("현재 금액 : {:,}".format(currentMoney))
#     sel = int(input("메뉴 선택 : "))
#     print()
               
#     if sel == 1:
#         if currentMoney > 300:
#             currentMoney -= 300
#             print("콜라 맛있게 드세요 !")
#         else:
#             print("투입 금액이 부족합니다.")
#     elif sel == 2:
#         if currentMoney > 300:
#             currentMoney -= 300
#             print("사이다 맛있게 드세요 !")
#         else:
#             print("투입 금액이 부족합니다.")
#     elif sel == 3:
#         if currentMoney > 300:
#             currentMoney -= 200
#             print("커피 맛있게 드세요 !")
#         else:
#             print("투입 금액이 부족합니다.")
#     elif sel == 4:
#         inputMoney = int(input("돈 넣기\n투입 금액을 입력해주세요."))
#         currentMoney += inputMoney
#         print("{:,}원이 충전되었습니다.".format(inputMoney))
#     elif sel == 5:
#         print("잔돈을 반환합니다.")
#         change += currentMoney
#         currentMoney = 0
#     elif sel == 6:
#         print("자판기 프로그램을 종료합니다.")
#         break
#     else:
#         print("잘못 입력하셨습니다 1 ~ 6 사이의 숫자를 입력해주세요.")