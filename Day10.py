# for var in range(100):
#     print("출력", var)

# 0 ~ 99 / +5
# for i in range(1, 100, 5):
#     print(i)

# 0 ~ 39
# for i in range(40):
#     print(i)

# 10 ~ 99
# for i in range(10, 100):
#     print(i)

# 100의 자리
# for i in range(100, 1000):
#     print(i)

# 예제1) 문자열 10번 출력
# for i in range(10):
    # print("문자열 {}번째 출력".format(i+1))
# 예제2) 숫자10까지 출력
# for i in range(11):
#     print(i)

# for i in range(10,0,-1):
#     print("문자열",i)

# 예제2)10까지 한줄로 출력
# for i in range(11):
#     print(i, end=" ")
# print("\n")
# for i in range(5, 11):
#     print(i, end=" ")
# print("\n")
# for i in range(5, 11):
#     print(i, end=" ")
# print("안녕")

# 예제3)for문 사용하여 변수 설정 및 문자열 아무거나 입력 후
# 순차적으로 출력해보기
# for i in "string":
#     print(i)

# sum = 0
# for i in range(10):
#     sum += i
# print(sum)

# a = 22
# b = 33
# a += b / 55
# a = a+b / 55
# print(a)

# 예제4)시작/끝/증가값 입력받은후 합을 구하시오
# start = int(input("시작값 입력 : "))
# end = int(input("끝값 입력 : "))
# inc = int(input("증가값 입력 : "))
# sum = 0
# for i in range(start, end, inc):
#     sum = sum + i
# print(sum)

# 문제1
# sum1 = 0
# for i in range(1,11):
#     sum1 += i
# print(sum1)

# Quiz2.For문과 IF문을 이용하여 아래와 같이 출력.
# ans #1 
# for i in range(30):
#     if (i+1) % 5 == 0:
#         print(i+1, end="\n")
#     else:
#         print(i+1, end="\t")

# ans #2
# for i in range(1,31):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i, end="\t")

# ans #3
# for i in range(1,31):
#     if i % 5 != 0:
#         print(i, end="\t")
#     else:
#         print(i)

# ans #4
# a = 0
# for i in range(6):
#     for j in range(5):
#         a += 1
#         print(a, end="\t")
#     print()

# # Quiz3.변수 st = "" 다음 문자열에서 a와 s의 개수를 구하시오x
# st = "It is a fun python class"
# st = st.upper()
# print(st)
# aCnt = 0
# sCnt = 0
# for i in st:
#     if i == "A":
#         aCnt += 1
#     if i == "S":
#         sCnt += 1
# print("a(A)의 개수 : {}개\ns(S)의 개수 : {}개".format(aCnt,sCnt))
