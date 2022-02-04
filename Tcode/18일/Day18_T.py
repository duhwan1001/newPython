# #String문자열 함수

# #find(), count(), lower(), upper()사용

# st = "Python String"

# # 변수명.문자열함수명()
# #find()
# print(st.find("String"))
# #count()
# print(st.count("t"))
# #lower()
# print(st.lower())
# #upper()
# print(st.upper())

# st1 = "   Python String   "

# print(st1)
# #strip() 양쪽
# print(st1.strip())
# #rstrip() 오른쪽
# print(st1.rstrip())
# #lstrip() 왼쪽
# print(st1.lstrip())

# st2 = "Python String"

# #replace()
# print(st2.replace("String","문자열"))
# #split()
# print(st2.split(" "))

# #문제1
# st = "It is a fun python class"
# print(len(st))

# print(st.count("a"))

# print(st.count("s"))

# #문제2
# st3 = "Have a nice day"

# print("a의 문자 개수: {}".format(st3.count("a")))
# print("day의 문자 개수: {}".format(st3.count("day")))
# print("dak의 문자 개수: {}".format(st3.count("dak")))

# # count()함수 없이
# a,b,c = 0,0,0
# st3_1 = st3.split(" ")
# print(st3_1)
# for i in st3:
#     if i == "a":
#         a += 1
# for i in st3_1:
#     if i == "day":
#         b += 1
#     elif i == "dak":
#         c += 1
# print("a개수: {}\tday개수: {}\tdak개수:{}".format(a,b,c,))

# # 함수 없이
# a,b,c = 0,0,0
# for i in st3:
#     if i == "a":
#         a += 1

# if "day" in st3:
#     b += 1
# elif "dak" in st3:
#     c += 1

# print("a개수: {}\tday개수: {}\tdak개수:{}".format(a,b,c,))

# # 인덱스 접근
# a,b,c = 0,0,0

# for i in range(len(st3)):
#     if st3[i] == "a":
#         a += 1
#     elif st3[i:i+3] == "day":
#         b += 1
#     elif st3[i:i+3] == "dak":
#         c += 1

# print("a개수: {}\tday개수: {}\tdak개수:{}".format(a,b,c,))
#문제3
st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
어피치 -2000년 11월 21일
라이언 -1980년 9월 12일"""
# #:접근
# st1 = st.replace("-",":")
# print(st1)
# a = 0
# b = st1.count(":")
# for i in range(b):
#     a = st1.find(":",a+1)
#     print(a)
#     st1 = st1.replace(st1[a+1:a+5],"1999")
# print(st1)

# #년접근
# st1 = st.replace("-",":")
# # print(st1)
# a = 0
# b = st1.count("년")
# for i in range(b):
#     a = st1.find("년",a+1)
#     st1 = st1.replace(st1[a-4:a],"1999")
# print(st1)

# #문제4
# user = input("성함과 나이를 입력해주세요(공백구분!): ")
# # a = user.split(" ")
# # print("성함: {}\t나이: {}".format(a[0],a[1]))

# a,b = user.split(" ")
# print("성함: {}\t나이: {}".format(a,b))

# #문제5
# a = input("수식을 입력하시오(ex:5*5): ")

# if "+" in a:
#     b,c= a.split("+")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} + {} = {}".format(b,c,b+c))
# elif "-" in a:
#     b,c= a.split("-")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} - {} = {}".format(b,c,b-c))
# elif "*" in a:
#     b,c= a.split("*")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} * {} = {}".format(b,c,b*c))
# elif "/" in a:
#     b,c= a.split("/")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} / {} = {}".format(b,c,b/c))


#문제6 
# 생년월일(8자리) 입력받고 년,월,일을 추출하는 프로그램 만들기
# a = input("생년월일 8자리를 입력해주세요: ")

# print("년 : {}\n월 : {}\n일 : {}".format(a[:4],a[4:6],a[6:]))


# #2번
# a = input("생년월일 8자리를 입력해주세요(/기준): ")
# b = a.split("/")
# print(b)
# print("년:{}".format(b[0]))
# print("월:{}".format(b[1]))
# print("일:{}".format(b[2]))

