# 폴더클릭후 => CODE로 열기 
# 새파일 만들기

#문제3

# st = "It is a fun fython class"
# a = 0
# s = 0
# for i in st:
#     if i == "a":
#         a += 1
#     elif i == "s":
#         s += 1
# print("a의 개수: {}\ts의 개수: {}".format(a,s))

# #문제4
# num1 = int(input("종료값 입력: "))
# 짝,홀 = 0,0
# for i in range(1,num1+1):
#     if i % 2 == 0:
#         짝 += i
#     else:
#         홀 += i
# print("짝수의 합: {}\t홀수의 합:{}".format(짝,홀))

# #문제5

# s = int(input("시작값 입력: "))
# e = int(input("끝값 입력: "))
# g = int(input("증가값 입력: "))

# for i in range(s,e+1,g):
#     if i % 7 == 0:
#         print(i,end="\t")
# print()


# #문제6
# sum1 = 0
# for i in range(1,101,1):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             sum1 += i
# print("합 : {}".format(sum1)) 

# #문제7 
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = 0

# for i in range(a,b+1):
#     c += i

# print("합: {}".format(c))

# #문제8 
# # 10737418230

# won = 10
# sum1 = 0
# for day in range(1,31):
#     sum1 += won
#     won *= 2
#     print(sum1,day)

# #문제9 
# # import turtle
# # forward (이동)
# # left (각도)
# # right(각도)
# # mainloop() => 유지 

# import turtle
# num1 = int(input("몇각형? "))
# for i in range(1,num1+1):
#     turtle.forward(100)
#     turtle.left(360/num1) # 도형의 외각 = 360 / 변개수 
# turtle.mainloop()

# #예제5(1)
# for i in range(3):
#     print("첫 번째 For문")
#     for j in range(2):
#         print("두 번째 For문")


# # 예제5(2)

# for i in range(3):
#     for j in range(3):
#         print("이중 For문 ( i: {}\tj :{})".format(i,j))

# #문제1
# for i in range(2,10,1):
#     for j in range(1,10,1):
#         print("{} X {} = {}".format(i,j,i*j),end= "\t")
#     print()
