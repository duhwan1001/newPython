# while True:
#     i = int(input("1 ~ 12 입력 >> "))
#     if 1 <= i <= 3:
#         print("봄")
#     elif 4 <= i <= 6:
#         print("여름")
#     elif 7 <= i <= 9:
#         print("가을")
#     elif 10 <= i <= 12:
#         print("겨울")
#     else:
#         print("다시 입력하세요")
#         continue
#     break

# for i in range(5):
#     print(i+1)
    
# wi = 0
# while True:
#     wi += 1
#     print(wi)
#     if wi == 5:
#         break

# Quiz6. while 사용하여 아래 문제를 푸시오
# 특정키 (0)를 입력할 때 까지 반복되도록 프로그램 작성 하시오.
# i = 0
# while True:
#     i = int(input("숫자 입력 >> "))
#     print("입력한 숫자 : {}".format(i))
#     if i == 0:
#         print("0을 입력하여 종료합니다.")
#         break
#     continue

# i = 0
# sum = 0
# while True:
#     i = int(input("숫자 입력 >> "))
#     sum += i
#     print("입력한 숫자 : {}".format(i))
#     if i == 0:
#         print("0을 입력하여 종료합니다.")
#         print("합 : {}".format(sum))
#         break
#     continue

# for i in range(5):
#     for j in range(10):
#         print("*", end=" ")
#     print("")

# i = 0
# j = 0
# while True:
#     if i == 5:
#         break
#     i += 1
#     j = 0
#     while True:
#         if j == 10:
#             break
#         j += 1
#         print("*", end=" ")
#     print()

# from random import random

# for i in range(6):
#     print(int(random()*45)+1)

# for i in range(6): # 짝수
#     print((int(random()*50)+1)*2)

# for i in range(6): # 홀수
#     print((int(random()*50)+1)*2-1)

# randrange 함수
# from random import randrange
# print(randrange(2, 101, 2))
# print(randrange(1, 101, 2))

from random import random
cnt = 0
while True:
    rnum = int(random()*100)+1
    print(rnum)
    cnt +=1 
    if rnum == 50:
        print("{}이 출력되었습니다. {}번 만에 출력되었습니다.".format(rnum, cnt))
        break
