# 폴더클릭후 => CODE로 열기 
# 새파일 만들기


# # 예제5 실수를 변수에 담아 실수의 제곱 출력하기
# a = 3.3
# print("{:.2f}".format(a*a))
# print("{:.2f}".format(a**2))
# 예제6 정수 3개 변수에 담아 그 합과 평균을 서식문자로 출력
# a = 10
# b = 20
# c = 30
# print("합: {} 평균: {}".format(a+b+c,(a+b+c)/3))

# # 예제7 자유롭게 변수에 담아 출력해보기
# a = 10
# b = 20
# c = 30
# d = a+b+c
# print("합: {} 평균: {}".format(d,d/3))

# 입력 input()
# 사용자로 부터 값을 입력받아 코드내에서 사용하기 위한 함수

# name = input("성함을 입력하세요: ")
# print(name)

# #문제1
# name = input("이름: ")
# age = input("나이: ")
# email = input("이메일: ")
# print("{}님의 나이는 {}살 이며, 이메일은 {}입니다.".format(name,age,email))

# #문제2
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# num3 = input("수입력: ")
# print(type(num1))

# #1번
# num1 = int(num1)
# num2 = int(num2)


# #2번
# print("{} + {} + {} = {} " .format(num1,num2,num3,int(num1)+int(num2)+int(num3)))
# print("{} - {} - {} = {} " .format(num1,num2,num3,int(num1)-int(num2)-int(num3)))


# #3번
# print("{} + {} = {} " .format(num1,num2,num1+num2))
# print("{} - {} = {} " .format(num1,num2,num1-num2))


# #문제3
# 수학 = int(input("수학 점수를 입력해주세요: "))
# 영어 = int(input("영어 점수를 입력해주세요: "))
# 파이썬 = int(input("파이썬 점수를 입력해주세요: "))

# print("평균은 {}점 입니다.".format((수학+영어+파이썬)/3))

# 수학 = int(input("수학점수를 입력해주세요: "))
# 영어 = int(input("영어점수를 입력해주세요: "))
# 파이썬 = int(input("파이썬 점수를 입력해주세요: "))

# 평균 = (수학 + 영어+ 파이썬) / 3

# print("평균은 {}점 입니다.".format(평균))


# # 문제4 
# 사과가격 = 3000
# 배가격 = 2000
# print("*** 사과 {}원 배{}원 ***".format(사과가격,배가격))
# 사과 = int(input("사과 개수를 입력해주세요: "))
# 배 = int(input("배 개수를 입력해주세요: "))

# 총금액 = 사과*사과가격 + 배*배가격

# print("총금액은 {:,}원 입니다.".format(총금액))

# #문제5
# 시 = int(input("시간을 입력하세요: "))
# 분 = int(input("분을 입력하세요: "))
# 초 = int(input("초를 입력하세요: "))

# 총초 = 시*3600 + 분*60 + 초

# print("총 초는 {}초 입니다.".format(총초))

# #문제6
# print("섭씨온도를 화씨온도로 바꿔드립니다!!")
# 섭씨온도 = int(input("섭씨온도를 입력해주세요: "))
# 화씨온도 = (섭씨온도*1.8)+32
# print("섭씨온도 : {} > 화씨온도 : {}".format(섭씨온도,화씨온도))

# print("화씨온도를 섭씨온도로 바꿔드립니다!!")
# 화씨온도 = int(input("섭씨온도를 입력해주세요: "))
# 섭씨온도 = (화씨온도-32)/1.8
# print("화씨온도 : {} > 섭씨온도 : {}".format(화씨온도,섭씨온도))


# #문제7 
# # BMI = 몸무게(kg) / ( 신장(m) X 신장(m) )
# #BMI 공식 이용하여 키, 몸무게 입력받아 출력
# # 키180 몸무게70 BMI 21.6 나오게 하기
# # 서식문자 사용X 
# 키 = int(input("키를 입력해주세요: "))
# 몸무게 = int(input("몸무게를 입력해주세요: "))
# 신장 = 키/100
# BMI = 몸무게 / (신장*신장)
# print(round(BMI,1))