# #String 문자열 함수

# #find(), count()

# st1 = "     Python String    "
# #strip() 양쪽

# print(st1.strip())
# #rstrip() 오른쪽
# print(st1.rstrip())
# #lstrip() 왼쪽
# print(st1.lstrip())

# st2 = "Python String"

# #replace()
# print(st2.replace("String", "문자열"))

# #split()
# print(st2.split())

# st = "It is a fun python class"
# cnt_a = cnt_s = cnt = 0
# for i in st:
#     cnt += 1
#     if i == 'a':
#         cnt_a += 1
#     elif i == 's':
#         cnt_s += 1
# print("문자열의 길이 : {}".format(cnt))
# print("문자 'a'의 개수 : {}".format(cnt_a))
# print("문자 's'의 개수 : {}".format(cnt_s))

# 문제 2
# st3 = "Have a nice day"

# print("a : {}".format(st3.count("a")))
# print("day : {}".format(st3.count("day")))
# print("dak : {}".format(st3.count("dak")))

# # count() 함수 없이
# a=b=c = 0
# for i in st3:
#     if i == "a":
#         a += 1
# for i in st3.split():
#     if i == "day":
#         b += 1
#     if i == "dak":
#         c += 1
# print("a : {}".format(a))
# print("day : {}".format(b))
# print("dak : {}".format(c))

# # 함수 업싱
# a=b=c = 0
# for i in st3:
#     if i == "a":
#         a += 1

# if "day" in st3:
#         b += 1
# elif "dak" in st3:
#         c += 1
# print("a : {}".format(a))
# print("day : {}".format(b))
# print("dak : {}".format(c))

# 인덱스 접근
# st3 = "Have a nice day"
# a=b=c = 0
# for i in range(len(st3)):
#     print(st3[i:i+3])
#     if st3[i] == "a":
#         a += 1
#     elif st3[i:i+3] == "day":
#         b += 1
#     elif st3[i:i+3] == "dak":
#         st3[i:i+3]
#         c += 1
# print("a : {}".format(a))
# print("day : {}".format(b))
# print("dak : {}".format(c))

# st = """세글자 - 2017년 03월 24일
# 다섯섯글자 -2015년 04월 02일
# 네글글자 -2018년 05월14일
# """

# st = st.replace("-", ":")

# cnt = 0
# for i in st:
#     if i == "년":
#         st = st.replace(st[cnt-4:cnt], "1999")
#     cnt +=1

# print(st)

# name, age = input("이름과 나이").split()

# print("이름 : {}\n나이 : {}".format(name,age))

# a = input("ex)5*5\n")

# if "+" in a:
#     b,c = a.split("+")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} + {} = {}".format(b,c,b+c))
# if "+" in a:
#     b,c = a.split("+")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} + {} = {}".format(b,c,b+c))
# if "+" in a:
#     b,c = a.split("+")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} + {} = {}".format(b,c,b+c))
# if "+" in a:
#     b,c = a.split("+")
#     b = int(b.strip())
#     c = int(c.strip())
#     print("{} + {} = {}".format(b,c,b+c))

# 문제6
# 생년월일 8자리 입력받고 년월일 추출

a = input()
print("year : {}".format(a[0:4]))
print("month : {}".format(a[4:6]))
print("day : {}".format(a[6:8]))