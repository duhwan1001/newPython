# 폴더클릭후 => CODE로 열기 
# 새파일 만들기
# #문제4
# print("1.easy game")
# print("2.hard game")
# print("3.exit")
# num1 = int(input("선택: "))
# if num1 == 1:
#     print("easy game start")
# if num1 == 2:
#     print("hard game start")
# if num1 == 3:
#     print("exit!")

# # 예제2
# num1 = int(input("수입력: "))
# if num1 % 2 == 0:
#     print("{}은 짝수".format(num1))
# if num1 % 2 == 1:
#     print("{}은 홀수".format(num1))

# if num1 % 2 == 0:
#     print("{}은 짝수".format(num1))
# else:
#     print("{}은 홀수".format(num1))

# #문제5
# num1 = int(input("수입력: "))
# if num1 % 3 == 0:
#     print("{}은 3의 배수입니다.".format(num1))
# else:
#     print("3의배수가 아닙니다.")

# #문제6
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# if num1 > num2:
#     print("{}이 {}보다 크다.".format(num1,num2))
# else:
#     print("{}이 {}보다 크다.".format(num2,num1))

# #문제7
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# num3 = int(input("수입력: "))

# if num1 > num2 and num1 > num3:
#     print("제일 큰 수 {}".format(num1))
# if num2 > num1 and num2 > num3:
#     print("제일 큰 수 {}".format(num2))
# if num3 > num1 and num3 > num2:
#     print("제일 큰 수 {}".format(num3))

# if num1 > num2 and num1 > num3:
#     print("제일 큰 수 {}".format(num1))
# else:
#     if num2 > num1 and num2 > num3:
#         print("제일 큰 수 {}".format(num2))
#     else:
#         print("제일 큰 수 {}".format(num3))

# #문제8 
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))

# if num1 > num2 and num1 % 2 == 0:
#     print("{}이 크면서 짝수이다.".format(num1))
# if num2 > num1 and num2 % 2 == 0:
#     print("{}이 크면서 짝수이다.".format(num2))

# #문제9 
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# sum1 = num1 + num2

# if sum1 % 2 == 0 and sum1 % 3 == 0:
#     print("{}은 합이 짝수이며 3의 배수인 경우".format(sum1))
# else:
#     print("해당X")

# #문제7
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# num3 = int(input("수입력: "))

# if num1>num2 and num1>num3:
#     print("{}이 제일 큰 수".format(num1))
# elif num2>num1 and num2>num3:
#     print("{}이 제일 큰 수".format(num2))
# else:
#     print("{}이 제일 큰 수".format(num3))

# #예제3
# num1 = int(input("수입력: "))
# if num1 == 1:
#     print("1입니다.")
# elif num1 == 2:
#     print("2입니다.")
# elif num1 == 3:
#     print("3입니다.")
# elif num1 == 4:
#     print("4입니다.")
# else:
#     print("1,2,3,4의 값을 제외한 값 입력")

# elif 사용하지 말고 3가지 이상 방법으로 풀어보기

# #1번
# a = int(input("수입력: "))
# if a == 1  or a == 2 or a == 3 or a == 4 :
#     print("{}".format(a))
# else:
#     print("1,2,3,4의 값을 제외한 값 입력")

# #2번 
# a = int(input("수입력: "))
# if 1 <= a <= 4:
#     print("{}".format(a))
# else:
#     print("1,2,3,4의 값을 제외한 값 입력")

# #3번
# a = int(input("수입력: "))
# if a == 1:
#     print(a)
# else:
#     if a == 2:
#         print(a)
#     else:
#         if a == 3:
#             print(a)
#         else:
#             if a == 4:
#                 print(a)
#             else:
#                 print("해당사항X")

# #문제10 계절 구하기
# # 3 ~ 5 봄 6 ~ 8 여름 9 ~ 11 가을 12 ~ 2 겨울

# 계절 = int(input("계절을 입력해주세요: "))
# if 3 <= 계절 <= 5:
#     print("{}월은 봄 입니다.".format(계절))
# elif 6 <= 계절 <= 8:
#     print("{}월은 여름 입니다.".format(계절))
# elif 9 <= 계절 <= 11:
#     print("{}월은 가을 입니다.".format(계절))
# else:
#     print("{}월은 겨울 입니다.".format(계절))