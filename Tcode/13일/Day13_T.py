# 폴더클릭후 => CODE로 열기 
# 새파일 만들기

# #예제9 
# while True:
#     print("망함....")
#     break
#     print("2번째 출력은 나오나요?")
# print("휴")

# #예제10
# while True:
#     i = int(input("10보다 작은 정수 입력: "))
#     if i < 10:
#          print("i는 10보다 작습니다.")
#          break
#     else:
#         print("말좀들어요...")
#         continue
# print("반복종료")


# # 계절 구하기
# (1~3봄 4~6여름 7~9가을 10~12겨울)

# 1.while True 사용
# 2.잘못입력했을 경우에 반복문 처음으로 돌아가 다시 계절 입력받기
# 3.1~12 정상 입력시 반복 종료

# while True:
#     i = int(input("계절을 입력하세요: "))
    # if 1 <= i <= 3:
    #     print("봄")
    # elif 4 <= i <= 6:
    #     print("여름")
    # elif 7 <= i <= 9:
    #     print("가을")
    # elif 10 <= i <= 12:
    #     print("겨울")
    # else:
#         print("잘못입력하셨습니다.")
#         continue
#     break
# print("종료")

# while True:
#     i = int(input("계절을 입력하시오: "))
#     if 1 <= i <= 12:
#         if 1 <= i <= 3:
#             print("봄")
#         elif 4 <= i <= 6:
#             print("여름")
#         elif 7 <= i <= 9:
#             print("가을")
#         elif 10 <= i <= 12:
#             print("겨울")
#         break
#     else:
#         print("잘못입력하셨습니다.")
#         continue
# print("종료")

#문제5 =>ppt보기

# #문제6
# while True:
#     user = int(input("입력: "))
#     if user == 0:
        # print("program exit!")
#         break
#     else:
#         print("다시입력!")
#         continue


# #문제7
# a = 0
# while True:
#     user = int(input("입력: "))
#     a += user
#     if user == 0:
#         print("program exit!")
#         print("합: ",a)
#         break
#     else:
#         print("다시입력!")
#         continue

# #문제8 
# for i in range(5):
#     for j in range(10):
#         print("*",end= " ")
#     print()

# #문제9
# i = 0 # 초기값
# while i < 5 : # 종료값
#     i += 1 # 증가값
#     j = 0 # 초기값
#     while j < 10: # 종료값
#         print("*",end= " ")
#         j += 1 # 증가값
#     print()


#RANDOM모듈

# # from 모듈명 import 함수명
# from random import random 

# # 0.0 ~ 1.0미만의 임의의 값 생성
# print(random())

# # 0.0 ~ 10.0미만의 임의의 값 생성
# print(random()*10)

# # 0 ~ 10미만의 임의의 값 생성
# print(int(random()*10))

# # 1 ~ 10까지의 임의의 값 생성
# print(int(random()*10)+1)

# # 1 ~ 45까지의 임의의 값 6개 생성
# for i in range(6):
#     print(int(random()*45)+1)

# # 1 ~ 100까지의 짝수 임의의 값 생성
# print((int(random()*50)+1)*2)

# # 1 ~ 100까지의 홀수 임의의 값 생성
# print((int(random()*50)+1)*2-1)

# # randrange함수
# from random import randrange
# print(randrange(2,101,2)) #짝수
# print(randrange(1,101,2)) #홀수

# #문제1
# from random import random
# for i in range(6):
#     print(int(random()*100)+1) 

# #문제2
# from random import random
# while True:
#     rand = (int(random()*100)+1)
#     print(rand)
#     if rand == 50:
#         break


