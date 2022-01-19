# 폴더클릭후 => CODE로 열기 
# 새파일 만들기

# #문제8
# # 123 입력시 => 일자리 3 십자리23 백자리123
# a = int(input("세자리수를 입력해주세요: "))
# 일자리 = a % 10 
# 십자리 = a % 100
# 백자리 = a 
# print("일자리 {}\n십자리 {}\n백자리 {}".format(일자리,십자리,백자리))

# #예제1
# print("9999를 14로 나누었을 때의")
# print("몫: {}".format(9999/14))
# print("나머지 : {}".format(9999%14))

# print("9999를 14로 나누었을 때의")
# print("몫: {}".format(9999//14))
# print("나머지 : {}".format(9999%14))

# print(3/2) # 1.5 (실수)
# print(3//2) # 1 (정수)
# print(3%2) #1 (나머지)


# #문제9
# a = int(input("세자리수를 입력해주세요: "))
# 일자리 = a % 10 
# 십자리 = a % 100 // 10
# 백자리 = a // 100
# print("일자리 {}\n십자리 {}\n백자리 {}".format(일자리,십자리,백자리))

# a = int(input("세자리수를 입력해주세요: "))
# 역일자리 = a // 100  
# 역십자리 = a // 10
# 역백자리 = a 
# print("역일자리 {}\n역십자리 {}\n역백자리 {}".format(역일자리,역십자리,역백자리))


# a = int(input("세자리수를 입력해주세요: "))
# 역일자리1 = a // 100  
# 역십자리1 = a // 10 % 10
# 역백자리1 = a % 10
# print("역일자리1 {}\n역십자리1 {}\n역백자리1 {}".format(역일자리1,역십자리1,역백자리1))

# #문제10

# 생년월일 = int(input("생년월일(8자리)을 입력하시오: "))

# 년 = 생년월일 // 10000
# 월 = 생년월일 % 10000 // 100
# 일 = 생년월일 % 100

# print("년: {}\n월: {}\n일: {}".format(년,월,일))

# #문제11

# 생년월일 = int(input("생년월일(6자리)을 입력하시오: "))

# 년 = 생년월일 // 10000
# 월 = 생년월일 % 10000 // 100
# 일 = 생년월일 % 100

# print("년: {}\n월: {}\n일: {}".format(년,월,일))

# #문제12
# a = int(input("정수 10자리를 입력하시오: "))
# b = a // 100000
# c = a % 100000
# print("{}\n{}".format(b,c))

# #turtle (그래픽 모듈)
# # 호출
# import turtle as t
# # 모양 설정 
# t.shape("turtle")
# # 이동
# t.forward(100)
# # 유지
# t.mainloop()

# #예제1
# import turtle as t
# t.shape("turtle")
# t.left(90)
# t.forward(100)
# t.mainloop()

# #예제2
# import turtle as t
# t.shape("turtle")
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.mainloop()


# #문제1
# import turtle as t
# a = int(input("길이값: "))
# t.shape("turtle")
# t.left(120)
# t.forward(a)
# t.left(120)
# t.forward(a)
# t.left(120)
# t.forward(a)
# t.mainloop()

# #문제12
# import turtle as t
# a = int(input("세로 길이값: "))
# b = int(input("가로 길이값: "))
# t.shape("turtle")
# t.left(90)
# t.forward(a)
# t.left(90)
# t.forward(b)
# t.left(90)
# t.forward(a)
# t.left(90)
# t.forward(b)
# t.mainloop()
