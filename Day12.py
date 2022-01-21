# sum = 0
# for i in range(5):
#     print("상위 For문 {}일때 하위 For문".format(i), end=" : ")
#     for j in range(5):
#         print(i*j, end="")
#     print()

# Quiz4. 이중 for문 이용 1  2   3   4   5
#                        6  7   8   9   10 ~~ 25까지
# sum = 0
# for i in range(5):
#     print()
#     for j in range(5):
#         sum += 1
#         print(sum, end="\t")
# print()

# sum = 0
# for i in range(5):
#     sum += 1
#     print(sum, end="\t")
#     for j in range(5):
#         print()
# print()

# 예제6) 1-10까지 짝수, 홀수 합을 for문을 사용하여 구하여라.
# odd = 0
# even = 0
# for i in range(11):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print("홀수의 합 : {}\n짝수의 합 : {}".format(odd, even))

# while문으로
# odd = 0
# even = 0
# i = 0
# while i < 10:
#     i = i + 1
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print("홀수의 합 : {}\n짝수의 합 : {}".format(odd, even))

# i = 0
# while i <= 5:
#     print(i)
#     i+=1

# 예제
# while True:
#     print("망함...")
i = 0
flag = True
while flag:
    i +=1
    if i == 10:
        flag = False
    print(i)