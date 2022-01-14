# Quiz10. 계절 구하기 3-5 봄 / 6 - 8 여름 / 9 - 11 가을 / 12 - 2 겨울
# num1 = int(input("월을 입력하세요 >> "))
# if 3 <= num1 <= 5 or -3 <= num1 <= -5:
#     print("봄")
# elif 6 <= num1 <= 8 or -6 <= num1 <= -8:
#     print("여름")
# elif 9 <= num1 <= 11 or -9 <= num1 <= -11:
#     print("가을")
# elif 12 <= num1 <= 2 or -12 <= num1 <= -2:
#     print("겨울")

# num1 = int(input("월을 입력하세요 >> "))
# if 3 <= num1 <= 5 or -3 <= num1 <= -5:
#     print("봄")
# elif 6 <= num1 <= 8 or -6 <= num1 <= -8:
#     print("여름")
# elif 9 <= num1 <= 11 or -9 <= num1 <= -11:
#     print("가을")
# elif 12 <= num1 <= 2 or -12 <= num1 <= -2:
#     print("겨울")
# else:
#     print("잘못 입력하셨습니다")


# 예제4. 3의 배수이며 짝수만 출력하는 프로그램
# num = int(input("숫자를 입력하세요 >> "))

# if num % 3 == 0:
#     if num % 2 == 0:
#         print("3의 배수이며 짝수입니다")
#     else:
#         print("조건에 만족하지 않습니다.") #9
# else:
#     print("조건에 만족하지 않습니다.") #8

# num1 = int(input("월을 입력하세요 >> "))
# if 1 <= num1 <= 12:
#     if 3 <= num1 <= 5:
#         print("봄")
#     elif 6 <= num1 <= 8:
#         print("여름")
#     elif 9 <= num1 <= 11:
#         print("가을")
#     elif 12 <= num1 <= 2:
#         print("겨울")
# else:
#     print("잘못 입력하셨습니다")

# Quiz1.
# math = int(input("수학 점수를 입력하세요 >> "))
# sci = int(input("과학 점수를 입력하세요 >> "))

# avg = (math + sci) / 2

# if avg > 90:
#     print("A 입니다.")
# elif avg > 80:
#     print("B 입니다.")
# elif avg > 70:
#     print("C 입니다.")
# else:
#     print("D 입니다.")

# Quiz2.
# num1 = int(input("첫번째 숫자를 입력하세요 >> "))
# num2 = int(input("두번째 숫자를 입력하세요 >> "))
# oper = input("연산자를 입력하세요\n+, -, /, *>> ")
# if oper == "+":
#     print("선택하신 연산자는 + 입니다. 결과는 {} 입니다".format(num1+num2))
# elif oper == "-":
#     print("선택하신 연산자는 - 입니다. 결과는 {} 입니다".format(num1-num2))
# elif oper == "*":
#     print("선택하신 연산자는 * 입니다. 결과는 {} 입니다".format(num1*num2))
# elif oper == "/":
#     print("선택하신 연산자는 / 입니다. 결과는 {} 입니다".format(num1/num2))
# else:
#     print("연산자 입력이 잘못되었습니다\nex) -, +, /, *")

# Quiz3.
# month = int(input("월을 입력하세요 >> "))
# if 3<= month <= 5:
#     print("봄입니다")
# elif 6<= month <= 8:
#     print("여름입니다")
# elif 9<= month <= 11:
#     print("가을입니다")
# elif month == 12 or 1 or 2:
#     print("겨울입니다")
# elif not 1<= month <= 12:
#     print("1에서 12월 사이로 입력해주세요")

# 연습2.pdf
# Quiz1.
# name = input("이름을 입력하세요 >> ")
# height = int(input("키를 입력하세요 >> "))
# weight = int(input("체중을 입력하세요 >> "))

# avgWeight = (height - 100) * 0.9
# res = weight / avgWeight * 100
# print(res)
# if res < 100:
#     print("저체중")
# elif res < 110:
#     print("정상체중")
# elif res < 120:
#     print("과체중")
# elif res < 130:
#     print("비만")
# elif res < 130:
#     print("고도비만")

# Quiz2.
# birthYear = int(input("태어난 연도를 입력하세요 >> "))
# sol = birthYear % 12
# if sol == 0:
#     print("원숭이")
# elif sol == 1:
#     print("닭")
# elif sol == 2:
#     print("개")
# elif sol == 3:
#     print("돼지")
# elif sol == 4:
#     print("고양이")
# elif sol == 5:
#     print("소")
# elif sol == 6:
#     print("호랑이")
# elif sol == 7:
#     print("토끼")
# elif sol == 8:
#     print("용")
# elif sol == 9:
#     print("뱀")
# elif sol == 10:
#     print("말")
# elif sol == 11:
#     print("양")

# Quiz3. // 문제 6
num = int(input("숫자를 입력하세요"))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print("윤년")
        else: 
            print("평년")
    else:
        print("평년")
else:
    print("평년")

# 숙제 : 문제 6번 다른 방법으로 풀어보기 2개 이상
