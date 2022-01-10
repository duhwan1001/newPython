#3. 문자열 및 실수 출력
#C스타일
print("%s님의 키는 %fcm 입니다." %("두", 12.345))
#P스타일
print("{}님의 키는 {:f}cm 입니다.".format("두", 12.345))
print("{}님의 키는 {:.2f}cm 입니다.".format("두", 12.345))

#4. 고정길이 출력
#C스타일 \n == 줄바꿈
print("%d원\n%10d원" %(10000,200000))
#P스타일
print("{}원\n{:5}원".format(10000,2000010))

#5. 정렬하여 출력
#C스타일
print("%20s" %("오른쪽정렬"))
print("%10s" %("오른쪽정렬"))
print("%-10s" %("왼쪽정렬"))
print("%10s,%-10s" %("오른쪽", "왼쪽"))
#P스타일
print("{:>20}".format("오른쪽정렬"))
print("{:>10}".format("오른쪽정렬"))
print("{:<10}".format("왼쪽정렬"))
print("{:>},{:<}".format("오른쪽", "왼쪽"))

#6.빈 여백 0으로 채운후 출력
#C스타일
print("%5d\t%05d" %(1,1))
#P스타일
print("{:5}\t{:05}".format(1,1))

#7.P스타일
print("{:>5},{:_>20}".format(1,1000000000))
print("{:,}".format(1000000000))

#실습
print("\t\t{}".format("파이썬 쇼핑몰 "))
print("{}{}{}".format("번호", " : ",1078718855))
print("{}{}{}".format("주소", " : ","서울시 종로구 종로3가"))
print("{}{}{}".format("성명", " : ","김사장"))
print("{}{}{}".format("전화", " : ","070-1234-5678"))
print("{}".format("-"*52))
print("\t{}\t\t\t{}\t{}\t{}".format("품명","단가","수량","금액"))
print("{}".format("-"*52))
print("{:>11}\t\t{:>6,}\t{:>4}\t{:>,}".format("블루투스 이어폰", 85000,"1", 85000))
print("{:>12}\t\t\t{:>6,}\t{:>4}\t{:>6,}".format("USB3.0 8G", 8000,"1", 8000))
print("{}".format("-"*52))
print("{}\t\t\t\t\t\t{:,}".format("소 계", 93000))
print("{}".format("-"*52))
print("{}\t\t\t\t\t{:,}".format("청구금액", 93000))
print("{}\t\t\t\t\t{:,}".format("받은금액", 100000))
print("{}\t\t\t\t\t{:,}".format("거스름돈", 7000))
print("{}".format("-"*52))

#변수

#1. 선언 a,b,c
#2. 할당(정수, 실수, 문자열)
#3. 참조 print()

a = 100
print(type(a))
b = 3.14
print(type(b))
c = "string"
print(type(c))

import keyword
# False = 10 # 키워드 사용 불가
print(keyword.kwlist)

print = 10
print(1)

#예제
#1. 자신의 이름, 나이 사는곳을 변수에 담아 출력해보기
name = "KIM"
age = "24"
adr = "daejeon"

print("이름은 " + name + "나이는 " + age + "주소는 " + adr)
print("이름은 ",name,"나이는 ",age,"주소는 ",adr)
print("이름은 {} 나이는 {} 주소는 {}".format(name, age, adr))
print("==" * 10)

#2. 자신의 키 몸무게를 변수에 담아 출력하기
height = "214"
weight = "10"
print("키는 {}cm 몸무게는 {}kg".format(height,weight))
print("==" * 10)

#3. ? + ? = 30과 같은 결과가 나오도록 변수 설정
num1 = 24
num2 = 6
print(str(num1) + " + " +  str(num2) + " = " + str(num1 + num2))
print("==" * 10)

#4. 이름과 출생년도 변수에 담아 만 나이 출력하기
birthYear = 1999
currentYear = 2022
print("이름 : " + name + "\n생년월일 : " + str(birthYear) + "\n만 나이는 : " + str(currentYear - birthYear))
print("==" * 10)

#5. 실수를 변수에 담아 실수의 제곱 출력하기
newFloat = 7.14
print("{:.2f}의 제곱은 {}".format(newFloat,newFloat ** newFloat))
print("{:.2f}의 제곱은 {}".format(newFloat,newFloat * newFloat))
print("==" * 10)

#6. 정수 3개 변수에 담아 그 합과 평균을 서식문자로 출력
newNum1 = 210
newNum2 = 732
newNum3 = 504
# print("정수 3개" + str(newNum1) + str(newNum2) + str(newNum3)
#         + "\n합 : " + str(newNum1+newNum2+newNum3) 
#         + "\n평균 : " + str((newNum1+newNum2+newNum3)/3))
print("합 : {} 평균 : {}".format(newNum1+newNum2+newNum3,(newNum1+newNum2+newNum3)/3))
print("==" * 10)

#7. 자유롭게 변수에 담아 출력해보기
newNum1 = 210
newNum2 = 732
newNum3 = 504
sum = newNum1+newNum2+newNum3
print("합 : {} 평균 : {}".format(sum,(sum)/3))


