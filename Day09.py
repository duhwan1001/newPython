# Quiz3. // 문제 6
# num = int(input("숫자를 입력하세요"))
# if num % 4 == 0:
#     if num % 100 == 0:
#         if num % 400 == 0:
#             print("윤년")
#         else: 
#             print("평년")
#     else:
#         print("평년")
# else:
#     print("평년")

# 숙제 : 문제 6번 다른 방법으로 풀어보기 2개 이상
# sol1
# num = int(input("숫자를 입력하세요"))
# if num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
#     print("윤년")
# else:
#     print("평년")

# sol2
# num = int(input("숫자를 입력하세요"))
# if num % 4 == 0:
#     if num % 100 == 0:
#         if num % 400 == 0:
#             print("윤년")
#         elif not num % 4 == 0:
#             print("평년")
#     elif not num % 100 == 0:
#         print("평년")
# elif not num % 400 == 0:
#     print("평년")

# Quiz4.
# num = int(input("숫자를 입력하세요"))
# print(abs(num))

# Quiz5.
# print("사과 3000원, 배 2000원")
# appleCnt = int(input("구입할 사과의 숫자를 입력하세요"))
# pearCnt = int(input("구입할 배의 숫자를 입력하세요"))
# money = int(input("가지고 있는 돈을 입력하세요"))

# apple = appleCnt * 3000
# pear = pearCnt * 2000
# summ = apple + pear

# res = money - summ

# if res < 0:
#     print("구매불가\n필요한 금액 : {}".format(abs(res)))
# else:
#     print("구매성공!\n남은 금액 : {}".format(res))

# if money >= summ:
#     print("잔액 : {:,}원".format(money - summ))
# else:
#     print("구매불가\n필요한 금액 : {:,}".format(summ-money))
# Quiz6. 
# num = int(input("숫자를 입력하세요"))
# if num % 15 == 0:
#     print("3의 배수입니다.")
# elif num % 3 == 0:
#     print("5의 배수입니다.")
# elif num % 5 == 0:
#     print("15의 배수입니다.")
# else:
#     print("해당없음")

# Quiz7 123 -> 321
# num1 = int(input("첫번째 숫자 : 3자리수로 입력하세요"))
# num2 = int(input("두번째 숫자 : 3자리수로 입력하세요"))

# # r_num1 = num1 / 100
# # secondN = num1 % 100 / 10
# # thirdN = num1 % 10

# # firstN = num2 / 100
# # secondN = num2 % 100 / 10
# # thirdN = num2 % 10

# # print("{} / {} / {}".format(round(num3),round(num2),num5))

# # print("입력하신 숫자 : {},{}".format(reverseN1,num2))

# r_A = num1 % 10 * 100 + num1//10%10*10 + num1//100
# r_B = num2 % 10 * 100 + num2//10%10*10 + num2//100

# if r_A > r_B:
#     print("뒤집었을때 큰수는 {}".format(num1))
# elif r_A < r_B:
#     print("뒤집었을때 큰수는 {}".format(num2))
# elif r_A == r_B:
#     print("두 수가 같습니다")

# Quiz8
# day = int(input("몇일차? >> "))
# res = ""
# if day % 4 == 1:
#     res = "A"
# elif day % 4 == 2:
#     res = "B"
# elif day % 4 == 3:
#     res = "C"
# else:
#     res = "D"
# print("{}일 차에는 {}가 당번입니다".format(day, res))

# Quiz9
# today = "화"
# day = int(input("몇일후? >> "))
# res = ""
# if day % 7 == 1:
#     res = "수"
# elif day % 7 == 2:
#     res = "목"
# elif day % 7 == 3:
#     res = "금"
# elif day % 7 == 4:
#     res = "토"
# elif day % 7 == 5:
#     res = "일"
# elif day % 7 == 6:
#     res = "월"
# else:
#     res = "화"
# print("{}일 후에는 {}요일입니다".format(day, res))

# Quiz10. 30분 추가
# time = int(input("시간을 입력해주세요 *24시간 형식* >>"))
# min = int(input("분을 입력해주세요 >>"))
# min = min + 30
# lessMin = 0
# if min > 60:
#     lessMin = min - 60
#     time = time + 1
#     print("{} : {}".format(time, lessMin))
# else:
#     print("{} : {}".format(time, min))

# Quiz11. 30분 빼기
# time = int(input("시간을 입력해주세요 *24시간 형식* >> "))
# min = int(input("분을 입력해주세요 >>"))
# min = min - 30
# lessMin = 0
# if min < 0:
#     lessMin = 60 + min
#     time = time - 1
#     print("{} : {}".format(time, lessMin))
# else:
#     print("{} : {}".format(time, min))

# Quiz12. 커피
# print("=" * 10)
# print("1.아메리카노\n2.카페라떼")
# print("=" * 10)
# menuSel = int(input("메뉴 선택 : "))
# coffee = ""
# if menuSel == 1:
#     coffee = "아메리카노"
# elif menuSel == 2:
#     coffee = "카페라떼"
# else:
#     print("잘못 선택하셨습니다.")
# print("=" * 10)
# print("1.ICE\n2.HOT")
# print("=" * 10)
# temSel = int(input("메뉴 선택 : "))
# temper = ""
# if temSel == 1:
#     temper = "아이스"
# elif temSel == 2:
#     temper = "핫"
# else:
#     print("잘못 선택하셨습니다.")
# print("=" * 10)
# print("선택하신 음료는 {} {} 입니다.".format(temper,coffee))
