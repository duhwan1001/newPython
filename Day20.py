# 숙제1

# 1.약수 + 약수개수 = 함수
# def 약수_1(a):
#     cnt = 0
#     for i in range(1,a+1):
#         if a % i == 0:
#             print("{}의 약수입니다.")

# 2.(약수 + 약수개수 = 함수) + 리턴

# def yaksu(a):
#     li = []
#     for i in range(1, a+1):
#         if a % i == 0:
#             li.append(i)
#     return li,len(li)

# a,b = yaksu(8)
# print(a,b)

# 튜플
tuple1 = (10,20,30)

# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])

# 요소 변경 => TypeError(요소 변경 불가능)
# tuple1[0] = 1
# print(tuple1[0])

# 요소 교환
# a, b = (10, 20)
# print("교환전")
# print(a)
# print(b)

# a,b = b,a
# print("교환후")
# print(a)
# print(b)

# 요소를 하나만 가지는 튜플
# a = (273, )

# print(a[0])

# 리스트와 튜플의 특이한 사용법
[a,b] = [10, 20]
(c, d) = (30, 40)

print(a,b,c,d)

# ---------------------- 문제풀이

#1
#1-1
# a = int(input())
# if a % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

#1-2
# a = int(input())

# odd = 0
# even = 0

# for i in range(1,a+1):
#     if i % 2 == 0:
#         print("{} : 짝수".format(i))
#     else:
#         print("{} : 홀수".format(i))

#1-3
# a = int(input())

# odd = 0
# even = 0

# for i in range(1,a+1):
#     if i % 2 == 0:
#         odd += i
#     else:
#         even += i
# print("{} : 짝수의 합".format(odd))
# print("{} : 홀수의 합".format(even))

#1-4
# a = int(input())
# li = []

# li.append(a)

# print(li)

#1-5
# a = int(input())

# li = []

# for i in range(1,a+1):
#     li.append(i)
# print(li)

#1-6
# a = int(input())

# li = []

# for i in range(1,a+1):
#     if not i % 2 == 0:
#         li.append(i)
# print(li)

#1-7
# a = int(input())
# if a == 0:
#     print("0")
# elif a % 3 == 0:
#     print("3의 배수")
# else:
#     print("3의 배수 아님")

#1-8
# a = int(input())

# for i in range(1,a+1):
#     if i % 3 == 0:
#         print(i,end=" ")
# print()

#1-9
# n = int(input())
# print("{}일차 :".format(n),end=" ")
# if n % 4 == 1:
#     print("A")
# elif n % 4 == 2:
#     print("B")
# elif n % 4 == 3:
#     print("C")
# elif n % 4 == 0:
#     print("D")

#1-10
# n = int(input())
# who = ""
# for i in range(1, n+1):
#     if i % 4 == 1:
#         who = "A"
#     elif i % 4 == 2:
#         who = "B"
#     elif i % 4 == 3:
#         who = "C"
#     elif i % 4 == 0:
#         who = "D"
#     print("{}일차 : {}".format(i, who))

#1-11
# a = int(input())
# if a % 4 == 0 and not a % 100 == 0:
#     print("윤년")
# elif a % 400 == 0 and a % 100 == 0:
#     print("윤년")
# else:
#     print("윤년이 아님")

#1-12
# a = int(input())
# for i in range(1, a+1):
#     if i % 4 == 0 and not i % 100 == 0:
#         print("{} : 윤년".format(i))
#     elif i % 400 == 0 and i % 100 == 0:
#         print("{} : 윤년".format(i))

#2 ---------------- 

#13
# for i in range(4):
#     a =  int(input())
#     if a % 2 == 0:
#         print("{}은 짝수".format(a))
#     else:
#         print("{}은 홀수".format(a))

#14
# li = []
# li2 = []

# for i in range(4):
#     a = int(input())
#     li.append(a)
#     if a % 2 == 0:
#         li2.append("짝수")
#     else:
#         li2.append("홀수")

# for i in range(4):
#     print("{}은 {}".format(li[i],li2[i]))

#15
# a, b = input().split()

# if int(a[-1]) + int(b[-1]) >= 10:
#     print("받아올림 발생")
# else:
#     print("받아올림 발생 안함")

#16
# for i in range(5):
#     a, b = input().split()

#     if int(a[-1]) + int(b[-1]) >= 10:
#         print("받아올림 발생")
#     else:
#         print("받아올림 발생 안함")

#17
# sum = 0
# for i in range(5):
#     a = int(input())
    
#     sum += a

# avg = sum / 5
# print("평균 : {}".format(avg))

#18
# li = []
# sum = 0
# for i in range(5):
#     a = int(input())
#     li.append(a)
#     sum += a

# avg = sum / 5
# print("5과목의 평균 : {}".format(avg))
# for i in li:
#     if avg > i:
#         print("{}는 평균이하".format(i))

#19
# if int(a[-1]) + int(b[-1]) > 5:
#     print("반올림 발생")
# else:
#     print("반올림 발생 안함")

# #20
# for i in range(5):
#     a, b = input().split()
#     print(int(a[-1]), int(b[-1]))
#     if int(a[-1]) + int(b[-1]) > 5:
#         print("반올림 발생")
#     else:
#         print("반올림 발생 안함")

#21
# li = [
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "■" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"], #4열 5행
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ["□", "□", "□", "□" ,"□" ,"□" ,"□" ,"□" ,"□" ,"□"],
#     ]

# while True:

#     for i in range(len(li)):
#         print()
#         for j in range(len(li)):
#             print(li[i][j],end=" ")
#     print()
#     print("※ 예약가능 : ■, 예약불가 : □")

#     a ,b = input("예약하고자 하는 열과 행을 입력해주세요").split()
#     print()
#     a = int(a)
#     b = int(b)
#     if li[a-1][b-1] == "□":
#         li[a-1][b-1] = "■"
#         print("예약 완료하였습니다.")
#     elif li[a-1][b-1] == "■":
#         print("이미 예약된 자리입니다.")
#         print()

#22
# t = ("admin", "12345")
# a = input("관리자 아이디를 입력하세요 : ")
# b = input("관리자 비밀번호를 입력하세요 : ")
# if a == t[0]:
#     if b == t[1]:
#         print("관리자 계정으로 로그인에 성공하셨습니다.")
# else:
#     print("아이디 또는 비밀번호가 잘못 입력되었습니다.")

#23
# d = {"id" : "admin", "pw" : "12345"}
# a = input("관리자 아이디를 입력하세요 : ")
# b = input("관리자 비밀번호를 입력하세요 : ")
# if a == d["id"]:
#     if b == d["pw"]:
#         print("관리자 계정으로 로그인에 성공하셨습니다.")
# else:
#     print("아이디 또는 비밀번호가 잘못 입력되었습니다.")

#24
# d = {"사과" : "apple", "바나나" : "banana", "책" : "book", "학생" : "student", "책상" : "desk"}

# for k, v in d.items():
#     ans = input("{}에 해당하는 영어 단어 입력".format(k))
#     if ans == v:
#         print("정답")
#     else:
#         print("틀렸습니다")

#3
d = {}
while True:
    print("네비게이션 즐겨찾기 주소 등록 프로그램")
    print("1. 주소 등록")
    print("2. 주소 수정")
    print("3. 주소 목록")
    print("4. 검색")
    print("5. 종료")

    sel = int(input("선택 >> "))

    if sel == 1:
        print("주소 등록")
        a = input("저장할 이름을 입력하세요 >> ")
        b = input("저장할 주소를 입력하세요 >> ")
        d.update({a : b})
        print("저장하였습니다.")
    elif sel == 2:
        print("2. 주소 수정")
        print("수정할 즐겨찾기 이름을 입력하세요")
        for k in d.keys():
            print(k, end=" / ")
    elif sel == 3:
        print("3. 주소 목록")
        for k, v in d.items():
            print("저장명 : {}\n주소 : {}".format(k,v))
            print("-" * 50)
    elif sel == 4:
        print("4. 검색")
    elif sel == 5:
        print("종료합니다.")
        break



