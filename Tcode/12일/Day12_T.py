# #문제6
# sum1 = 0
# for i in range(1,101,1):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             sum1 += i
#         print("합 : {}   {}".format(sum1,i)) 

# 들여쓰기 해서 횟수 확인해보기!

# # 문제2
# for i in range(1,10):
#     for j in range(2,10):
#         print("{} X {} = {}".format(j,i,j*i),end= "\t")
#     print()


# #문제3
# #1번
# for i in range(5):
#     print("상위 For문 {}일때 하위 For문".format(i),end=":")
#     for j in range(5):
#         print(i*j,end="")
#     print()

# print()

# #2번
# a = b = c = d = e = 0
# for i in range(5):
#     print("상위 for문 {}일때".format(i),end=" ")
#     for j in range(1):
#         print("하위 for문:{}{}{}{}{}".format(a,b,c,d,e))
#         b += 1
#         c += 2
#         d += 3
#         e += 4 

#문제4
# #1번
# for i in range(5):
#     for j in range(1,6):
#         print((i*5)+j,end="\t")
#     print()

# #2번
# for i in range(5):
#     for j in range(1,6):
#         if j % 5 == 0:
#             print((i*5)+j,end="\n")
#         else:
#             print(((i*5)+j),end="\t")

# #3번
# a = 0
# for i in range(5):
#     for j in range(5):
#         a += 1
#         print(a,end="\t")
#     print()

# # 4번
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5

# for i in range(5):
#     for j in range(1):
#         print("{}\t{}\t{}\t{}\t{}".format(a,b,c,d,e))
#         a += 5
#         b += 5
#         c += 5
#         d += 5
#         e += 5
# print()


# 예제6
#for문
# odd,even = 0,0
# for i in range(0,11,1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print("짝수의합: {}\t홀수의합: {}".format(even,odd))

# #while문
# odd ,even = 0,0
# i = 0
# while i <= 10:
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
#     i += 1

# print("짝수의합: {}\t홀수의합: {}".format(even,odd))

# #예제7

# i = 0 # 시작값
# while i <= 5: # 종료값
#     print(i)
#     i += 1 #  증가값

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print(i)
# print("다음문장")

# while True:
#     print("망함....")

# #ctrl + a => 반복 멈춤 => X누르기


#예제8
# 
# # 무한 반복 되는 코드
# i = 1
# while True:
#     if i <= 10:
#         print(i)
#         i += 1
#     else:
#         break

# i = 1
# a = True
# while a:
#     print(i)
#     if i == 10:
#         a = False
#     i += 1


