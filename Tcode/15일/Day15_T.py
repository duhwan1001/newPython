# mgr.kgitbank.com

# 로그인 => 강의 평가 

# import time
# import os

# m = 0
# while True:
#     print("---- Menu ----")
#     print("1.콜라 / 300 ")
#     print("2.사이다 / 300 ")
#     print("3.커피 / 200" )
#     print("4.돈넣기")
#     print("5.잔돈 반환")
#     print("6.종료")
#     print("-"*12)
#     print("현재금액",m)
#     menu = int(input("메뉴선택: "))
#     print()
#     time.sleep(0.7)
#     os.system("cls")
#     if menu == 1:
#         if m < 300:
#             print("금액이 부족합니다.")
#         else:
#             print("콜라 맛있게 드세요!")
#             m -= 300
#     elif menu == 2:
#         if m < 300:
#             print("금액이 부족합니다.")
#         else:
#             print("사이다 맛있게 드세요!")
#             m -= 300
#     elif menu == 3:
#         if m < 200:
#             print("금액이 부족합니다.")
#         else:
#             print("커피 맛있게 드세요!")
#             m -= 200
#     elif menu == 4:
#         a = int(input("돈을 넣어주세요: "))
#         m += a
#     elif menu == 5:
#         print("잔돈을 반환합니다.")
#         m = 0
#     elif menu == 6:
#         print("종료!")
#         break
#     else:
#         print("잘못입력하셨습니다.")
#         continue 
#     time.sleep(0.7)
#     os.system("cls")

#파이썬 자료형

#리스트[list]

# #리스트 선언
# list_1 = [300,30,333,"문자열",True]
# print(list_1)

# #인덱스
# print(list_1[0])
# print(list_1[1])
# print(list_1[2])

# #슬라이싱
# print(list_1[1:3])
# print(list_1[0:4])
# print(list_1[2:3])

# #역순
# print(list_1[-1])
# print(list_1[-3])
# print(list_1[-5])

# #인덱스 사용전
# a,b,c = 0,0,0
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# sum1 = a + b + c
# print(sum1)

# #인덱스 사용후
# a = [0,0,0]

# a[0] = int(input("수입력: "))
# a[1] = int(input("수입력: "))
# a[2] = int(input("수입력: "))

# sum2 = a[0] + a[1] + a[2]

# print(sum2)

# #요소 변경
# list_1 = [300,30,333,"문자열",True]
# print(list_1)
# list_1[0] = "변경"
# print(list_1)

# #문제1

# 과일 = ["딸기","바나나","키위","샤인머스켓","귤","사과","멜론"]

# 과일[1] = "망고"
# print(과일)
# 과일[-1] = "수박"
# print(과일)
# 과일[0:2] = "미니딸기","미니바나나"
# print(과일)

# #문제2 => 연산자 사용X

# a = input("정수를 입력해주세요: ")
# b = a[-1]
# # print(b)

# if b == "0" or b == "2" or b =="4" or b == "6" or b == "8":
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# #멤버 연산자
# print(1 in (1,2,3))
# print(1 in (2,3))
# print(1 not in(1,2,3))
# print(1 not in(2,3))

# #문제3
# a = input("정수를 입력해주세요: ")
# b = a[-1]

# #짝수
# if b in("0","2","4","6","8"):
#     print("짝수")
# #홀수
# else:
#     print("홀수")

# #리스트 요소에 이중으로 접근
# list_1 = [300,30,333,"문자열",True]

# print(list_1[3])
# print(list_1[3][0])

# #리스트안에 리스트 사용
# list_2 = [[1,2,3],["넷","다섯","여섯"],[7,8,9]]

# print(list_2[1])
# print(list_2[1][1])
# print(list_2[1][1][1])

# #index에러
# list_3 = [300,"문자열",True]
# print(list_3[3])
# #IndexError: list index out of range

# #문제4

# A = [["a","p","p","l","e"],
# ["python","is","funny"],
# ["happy","new","year"]]
# B = ["apple"]

# print(A[0][0],A[0][1],A[0][2],A[0][3],A[0][4])
# print(A[1][0],A[1][1],A[1][2])
# print(A[2][0],A[2][1],A[2][2])
# print(A[0][0],B[0][1],B[0][2],B[0][3],B[0][4])

# # print(len(A))

# #문자열의 길이len 리스트의 요소의 개수len
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(len(A[i]))
#         print(A[i][j],end= " ")
#     print()



