# a = int(input("숫자 입력"))
# odd = 0
# even = 0
# for i in range(1,a+1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print("1부터{}까지의 짝수 홀수합은\n짝수 : {}\n홀수 : {}".format(a, even, odd))

# Quiz5. 시작 값, 끝 값, 증가값(1) 입력받아 시작과 끝값 사이의 7의 배수를 출력 하시오.
# a = int(input("시작값 입력 >>"))
# b = int(input("끝 값 입력 >>"))
# c = int(input("증가값(1) 입력 >>"))
# for i in range(a, b+1, c):
#     if i % 7 == 0:
#         print(i)

# Quiz6. 1~100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.
# a = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         a += i
# print(a)

# Quiz7. 두 수를 입력 받아 입력 받은 두 수의 범위안의 합을 구하시오
# a = int(input("첫번째 숫자 입력 >> "))
# b = int(input("두번째 숫자 입력 >> "))
# sum = 0
# for i in range(a, b+1):
#     sum += i
# print(sum)

# Quiz8. 첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로
#        한달(30일) 동안 저축한 금액을 구하시오
# day = 10
# sum = 0
# for i in range(1, 31):
#     print("{}일째날 예금한 금액 : {:,}".format(i, day))
#     sum += day
#     day = day * 2
#     print("n현재 총액 : {:,}".format(sum))
# print()
# print("30일동안 저축한 금액 : {:,}".format(sum))

# Quiz9. Turtle을 이용한 다각형 그리기(반복문 사용)
# import turtle as t
# a = int(input("숫자 입력 >> "))
# for i in range(1,a+1):
#     t.forward(100)
#     t.left(360/a) # 도형의 외각 = 360 / 변개수
# t.mainloop()

# 중첩 for문 이해하기
# for i in range(5):
#     print("첫 번째 for문")
#     for j in range(2):
#         print("두 번째 for문")

# for i in range(3):
#     for j in range(3):
#         print("이중 for 문 (i : {}\tj : {})".format(i, j))

# Quiz1. 중첩 for문 이용하여 구구단표 작성
# for i in range(2, 10):
#     print()
#     for j in range(1,10):
#         print("{} x {} = {}".format(i, j, (i*j)),end="\t")
# print()

# 숙제
for i in range(1,10):
    print()
    for j in range(2, 10):
        print("{} x {} = {}".format(j, i, (i*j)),end="\t")
print()