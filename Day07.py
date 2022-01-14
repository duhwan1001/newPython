# sel = int(input("1. easy game\n2. hard game\n3. exit\n >> "))
# if(sel == 1):
#     print("easy game start")
# if(sel == 2):
#     print("hard game start")
# if(sel == 3):
#     print("exit")

# num = int(input("숫자를 입력하세요 >> "))
# num = num % 2
# if num == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# num = int(input("숫자를 입력하세요 >> "))
# if num % 3 == 0:
#     print("{}는 3의 배수입니다".format(num))
# else:
#     print("{}는 3의 배수가 아닙니다".format(num))

# num1 = int(input("첫번째 숫자를 입력하세요 >> "))
# num2 = int(input("두번째 숫자를 입력하세요 >> "))

# print("입력한 숫자 {}, {}".format(num1,num2))
# if num1 < num2:
#     print("{}가 더 큰 숫자 입니다.".format(num2))
# else: 
#     print("{}가 더 작은 숫자 입니다.".format(num1))

# Quiz7. 세 수를 입력 받아 큰 수를 출력하시오
# num1 = int(input("첫번째 숫자를 입력하세요 >> "))
# num2 = int(input("두번째 숫자를 입력하세요 >> "))
# num3 = int(input("세번째 숫자를 입력하세요 >> "))

# if num1 > num2 and num1 > num3:
#     print("1 제일 큰 수 {}".format(num1))
# elif num2 > num1 and num2 > num3:
#     print("2 제일 큰 수 {}".format(num2))
# else:
#     print("3 제일 큰 수 {}".format(num3))

# Quiz8. 두 수를 입력 받아 큰 수가 짝수이면 출력하시오
# num1 = int(input("첫번째 숫자를 입력하세요 >> "))
# num2 = int(input("두번째 숫자를 입력하세요 >> "))

# if num1 > num2 and num1 % 2 == 0:
#     print("큰 숫자는 {}이며 짝수입니다.".format(num1))
# if num2 > num1 and num2 % 2 == 0:
#     print("큰 숫자는 {}이며 짝수입니다.".format(num1))
# res = 0
# if num1 < num2:
#     res = num2
# else:
#     res = num1
# if res % 2 == 0:
#     print("큰 숫자는 {}이며 짝수입니다.".format(res))

# Quiz9. 두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오 
# num1 = int(input("첫번째 숫자를 입력하세요 >> "))
# num2 = int(input("두번째 숫자를 입력하세요 >> "))

# sum = num1 + num2
# print("입력한 수 : {}, {}".format(num1,num2))
# if sum % 2 == 0 and sum % 3 == 0:
#     print("입력한 수의 합은 {}이며 짝수이자 3의 배수입니다.".format(sum))
# else:
#     print("해당 없음")
# if sum % 2 == 0:
#     print("입력한 수의 합은 {}이며 짝수입니다.".format(sum))
# if sum % 3 == 0:
#     print("입력한 수의 합은 {}이며 3의 배수입니다.".format(sum))

# 예제3. 정수 입력 받아서 1부터 4일때 입력 한 것 출력
# num1 = int(input("첫번째 숫자를 입력하세요 >> "))
# if num1 == 1:
#     print("1입니다")
# elif num1 == 2:
#     print("2입니다")
# elif num1 == 3:
#     print("3입니다")
# elif num1 == 4:
#     print("4입니다")
# else:
#     print("1~4가 아닙니다.")

# if num1 == 1:
#     print("1입니다")
# if num1 == 2:
#     print("2입니다")
# if num1 == 3:
#     print("3입니다")
# if num1 == 4:
#     print("4입니다")
# if num1 != 1 and num1 != 2 and  num1 != 3 and num1 != 4:
#     print("1~4가 아닙니다.")

# Quiz10. 계절 구하기 3-5 봄 / 6 - 8 여름 / 9 - 11 가을 / 12 - 2 겨울
num1 = int(input("월을 입력하세요 >> "))
if 3 <= num1 <= 5:
    print("봄")
elif 6 <= num1 <= 8:
    print("여름")
elif 9 <= num1 <= 11:
    print("가을")
elif 12 <= num1 <= 2:
    print("겨울")