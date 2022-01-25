# list_1 = [300, 30, 333, "문자열", True]

# #슬라이싱
# print(list_1[1:1])

# #역순
# print(list_1[-1])
# print(list_1[-2])
# print(list_1[-3])

# 인덱스 사용전
# a=0
# b=0
# c=0

# a=int(input())
# b=int(input())
# c=int(input())

# sum=a+b+c
# print(sum)

# 인덱스 사용후
# a = [0,0,0]
# a[0]=int(input())
# a[1]=int(input())
# a[2]=int(input())

# sum = a[0] + a[1] + a[2]
# print(sum)

# 요소 변경
# list1 = [300, 30, 333, "문자열", True]

# list1[0] = "변경"
# print(list1)

# Quiz1. 과일 리스트 만들어서 인덱스 사용하여 요소 변경
# fruits = ["사과", "딸기", "포도"]
# fruits[0] = "배"
# fruits[1] = "갈배"
# fruits[-1] = "갈갈배"
# print(fruits)

# Quiz2. 숫자를 문자로 입력 받아서 끝ㅈ리로 짝수 홀수 구분하는 프로그램
# a = input()
# lastNum = a[-1]
# flag = False
# odd = [0,2,4,6,8]

# for i in range(len(odd)):
#     if lastNum == str(odd[i]):
#         flag = True

# if flag == True:
#     print("{}는 짝수입니다.".format(a))
# else:
#     print("{}는 홀수입니다.".format(a))

# 멤버 연산자
# print(1 in (1,2,3))
# print(1 in (2,3))
# print(1 not in (1,2,3))
# print(1 not in (2,3))

# a = input()
# b = a[-1]
# if b in ("0","2","4","6","8"):
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# # 리스트 요소에 이중으로 접근
# list_1 = [300, 30, 333, "문자열", True]
# print(list_1[3])
# print(list_1[3][0])

# # 리스트안에 리스트 사용
# list_2 = [[1,2,3],["넷","다섯","여섯"],[7,8,9]]
# print(list_2[1])
# print(list_2[1][1])
# print(list_2[1][1][1])

#index에러
# list_3 = [300, "문자열", True]
# print(list_3[3])
# IndexError: list index out of range

# Quiz4. A,B 선언하여 아래와 같이 리스트 지정
A = [["a","p","p","l","e"],["python","is","funny"],["happy","new","year"]]
B = ["apple"]
print("{} {} {} {} {}".format(A[0][0],A[0][1],A[0][2],A[0][3],A[0][4]))
print("{} {} {}".format(A[1][0],A[1][1],A[1][2]))
print("{} {} {}".format(A[2][0],A[2][1],A[2][2]))
print("{} {} {} {} {}".format(B[0][0],B[0][1],B[0][2],B[0][3],B[0][4]))

# 문자열의 길이 len()
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=" ")
    print()

