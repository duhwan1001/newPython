# 입력 input()
# 사용자로 부터 값을 입력받아 코드내에서 사용하기

# name = input("성함을 입력하세요 >>")
# age = input("나이를 입력하세요 >>")
# email = input("이메일을 입력하세요 >>")
# print("이름 : {}\n나이 : {}\n이메일 : {}".format(name, age, email))

# n1 = int(input("첫번째 숫자 >>"))
# n2 = int(input("두번째 숫자 >>"))
# print((type(n1))) == <class 'str'>

# #1번
# n1 = int(n1)
# n2 = int(n2)

# #2번
# print("+의 경우 : {}".format(int(n1) + int(n2)))
# print("-의 경우 : {}".format(int(n1) - int(n2)))

# #3번
# print("+의 경우 : {}".format(n1 + n2))
# print("-의 경우 : {}".format(n1 - n2))

# Quiz3. 수학, 영어 점수를 입력받고 평균을 출력해 주는 프로그램을 작성하시오.
# math = int(input("수학 점수 입력 >>"))
# eng = int(input("영어 점수 입력 >>"))
# python = int(input("파이썬 점수 입력 >>"))
# print("평균 : {}".format((math+eng+python)/3))

# math = int(input("수학 점수 입력 >>"))
# eng = int(input("영어 점수 입력 >>"))
# python = int(input("파이썬 점수 입력 >>"))
# avg = (math + eng + python) / 3 # 변동성이 많은 코드는 따로 변수로 설정해주는 것이 좋다.
# print("평균 : {}".format(avg))

# Quiz4. 사과 3000원, 배 2000원 / 사과와 배의 개수를 입력받고, 총 금액을 출력하는 프로그램 작성
# applePrice = 3000
# pearPrice = 2000

# print("사과 3000원, 배 2000원 ") # 항상 사용자 중심적인 코드를 작성하자
# appleCnt = int(input("사과의 개수를 입력하세요 >>"))
# pearCnt = int(input("배의 개수를 입력하세요 >>"))

# appleRes = appleCnt * applePrice
# pearRes = pearCnt * pearPrice

# result = appleRes + pearRes

# print("사과의 개수 : {}개\n배의 개수 : {}개\n총 금액 : {:,}원".format(appleCnt, pearCnt, result))

# Quiz5. 시, 분, 초를 입력받고 총 몇 초 인지 출력하는 프로그램
# hour = int(input("시를 입력하세요 >> "))
# min = int(input("분을 입력하세요 >> "))   
# sec = int(input("초를 입력하세요 >> "))

# # hourToSec = hour * 3600
# # minToSec = min * 60

# result = hour * 3600 + min * 60 + sec # 다음과 같이 절대 변하지 않는 공식에 대해서는 이렇게 하여도 좋음

# print("입력하신 시/분/초는 {}시 {}분 {}초 입니다.\n이를 초로 환산한 값은 {:,}초 입니다.".format(hour, min, sec, result))


# Quiz6. 섭씨온도를 화씨온도로 변환하기
# F = (C * 1.8) + 32
# print("섭씨온도를 화씨온도로 바꿔드립니다!!")
# ct = int(input("섭씨온도를 입력해주세요 >> "))
# ft = (ct * 1.8) + 32
# print("섭씨온도 : {} > 화씨온도 : {}".format(ct, ft))

# print("화씨온도를 섭씨온도로 바꿔드립니다")
# ft = int(input("화씨온도를 입력해주세요 >> "))
# ct = (ft - 32) / 1.8
# print("화씨온도 : {} > 섭씨온도 : {}".format(ft, ct))

# Quiz7. BMI 공식 이용하여 키, 몸무게 입력받아 출력
# BMI = 몸무게(kg) / (신장(m) * 신장(m))
print("*** BMI 계산기 ***")
height = int(input("키를 입력하세요(cm) >> ")) / 100
weight = int(input("몸무게를 입력하세요(kg) >> "))
BMI = weight / (height * height)
print(round(BMI,5))
print(round(BMI,1))
