# 폴더클릭후 => CODE로 열기 
# 새파일 만들기


#문제10 계절 구하기
# 3 ~ 5 봄 6 ~ 8 여름 9 ~ 11 가을 12 ~ 2 겨울

# 계절 = int(input("계절을 입력해주세요: "))
# if 3 <= 계절 <= 5:
#     print("{}월은 봄 입니다.".format(계절))
# elif 6 <= 계절 <= 8:
#     print("{}월은 여름 입니다.".format(계절))
# elif 9 <= 계절 <= 11:
#     print("{}월은 가을 입니다.".format(계절))
# else:
#     print("{}월은 겨울 입니다.".format(계절))

# #1번
# 계절 = int(input("계절을 입력해주세요: "))
# if 계절 < 0:
#     print("잘못입력하셨습니다.")
# elif 3 <= 계절 <= 5:
#     print("{}월은 봄 입니다.".format(계절))
# elif 6 <= 계절 <= 8:
#     print("{}월은 여름 입니다.".format(계절))
# elif 9 <= 계절 <= 11:
#     print("{}월은 가을 입니다.".format(계절))
# elif 13 <= 계절:
#     print("잘못입력하셨습니다.")
# else:
#     print("겨울 입니다.")

# #2번 방법
# 계절 = int(input("계절을 입력해주세요: "))
# if 3 <= 계절 <= 5:
#     print("{}월은 봄 입니다.".format(계절))
# elif 6 <= 계절 <= 8:
#     print("{}월은 여름 입니다.".format(계절))
# elif 9 <= 계절 <= 11:
#     print("{}월은 가을 입니다.".format(계절))
# elif 계절 == 12 or 계절 == 1 or 계절 == 2 :
#     print("{}월은 겨울 입니다.".format(계절))
# else:
#     print("잘못입력하셨습니다.")

# #3번 방법
# 계절 = int(input("계절을 입력해주세요: "))
# if 1 <= 계절 <= 12:
#     if 3 <= 계절 <= 5:
#         print("{}월은 봄 입니다.".format(계절))
#     elif 6 <= 계절 <= 8:
#         print("{}월은 여름 입니다.".format(계절))
#     elif 9 <= 계절 <= 11:
#         print("{}월은 가을 입니다.".format(계절))
#     else:
#         print("{}월은 겨울 입니다.".format(계절))
# else:
#     print("잘못입력하셨습니다.")

# #예제4
# num1 = int(input("수입력: "))
# if num1 % 3 == 0:
#     if num1 % 2 == 0:
#         print("3의 배수이며 짝수: {}".format(num1))
#     else:
#         print("조건에 만족하지 않는 수1") # 9 
# else:
#     print("조건에 만족하지 않는 수2") # 8 

# #조건문 연습

# #문제1
# 수학 = int(input("수학점수: "))
# 과학 = int(input("과학점수: "))
# 평균 = (수학 + 과학) / 2
# if 0 <= 평균 <= 100:
#     if 평균 >= 90:
#         print("이번학기 성적은 A입니다.")
#     elif 평균 >= 80:
#         print("이번학기 성적은 B입니다.")
#     elif 평균 >= 70:
#         print("이번학기 성적은 C입니다.")
#     else:
#         print("이번학기 성적은 D입니다.")
# else:
#     print("점수를 잘못입력하셨습니다.")

# #문제2
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = input("연산자 입력: ")
# if c == "+":
#     print("{} + {} = {}".format(a,b,a+b))
# elif c == "-":
#     print("{} - {} = {}".format(a,b,a-b))
# elif c == "*":
#     print("{} X {} = {}".format(a,b,a*b))
# elif c == "/":
#     print("{} / {} = {}".format(a,b,a/b))
# else:
#     print("연산자가 이상해요.")

#문제3
# 1 - 3봄 4 - 6 여름 7 - 9 가을 10 - 12겨울
# 월 = int(input("월을 입력해주세요: "))
# #1번
# if 1 <= 월 <= 3:
#     print("{}월은 봄입니다.".format(월))
# elif 4 <= 월 <= 6:
#     print("{}월은 여름입니다.".format(월))
# elif 7 <= 월 <= 9:
#     print("{}월은 가을입니다.".format(월))
# elif 10 <= 월 <= 12:
#     print("{}월은 봄입니다.".format(월))

# #2번
# if 1 <= 월 <= 12:
#     if 월 <= 3:
#         print("{}월은 봄입니다.".format(월))
#     elif 월 <= 6:
#         print("{}월은 여름입니다.".format(월))
#     elif 월 <= 9:
#         print("{}월은 가을입니다.".format(월))
#     elif 월 <= 12:
#         print("{}월은 겨울입니다.".format(월))
# else:
#     print("잘못입력하셨습니다.")

# #문제4
# # 비만도 = 현재체중 / 표준체중 * 100
# # 표준체중 = (키-100)*0.9

# 이름 = input("성함을 입력해주세요: ")
# 키 = float(input("키: "))
# 체중 = float(input("체중: "))

# 표준체중 = (키-100)*0.9
# 비만도 = 체중 / 표준체중 * 100

# print("{}님의 비만도는 {:.2f}입니다.".format(이름,비만도))

# if 비만도 < 100:
#     print("저체중")
# elif 100 <= 비만도 < 110:
#     print("정상")
# elif 110 <= 비만도 < 120:
#     print("과체중")
# elif 120 <= 비만도 < 130:
#     print("비만")
# else:
#     print("고도비만")


# #문제5
# 연도 = int(input("태어난 해를 입력해주세요: "))
# 띠 = 연도 % 12

# if 띠 == 0 :
#     print("원숭이")
# elif 띠 == 1:
#     print("닭")
# elif 띠 == 2:
#     print("개")
# elif 띠 == 3:
#     print("돼지")
# elif 띠 == 4:
#     print("쥐")
# elif 띠 == 5:
#     print("소")
# elif 띠 == 6:
#     print("범")
# elif 띠 == 7:
#     print("토끼")
# elif 띠 == 8:
#     print("용")
# elif 띠 == 9:
#     print("뱀")
# elif 띠 == 10:
#     print("말")
# elif 띠 == 11:
#     print("양")

# #문제6
# year = int(input("년도를 입력하시오: "))

# if year % 400 == 0:
#     print("{}년은 윤년입니다.".format(year))
# elif year % 100 == 0:
#     print("{}년은 평년입니다.".format(year))
# elif year % 4 == 0:
#     print("{}년은 윤년입니다.".format(year))
# else:
#     print("{}년은 평년입니다.".format(year))

# #숙제 문제6번 다른 방법으로 풀어보기 2개 이상