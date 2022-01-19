# 1:5분까지

# 다한 사람 2번 다른 방법으로도 풀어보기!

# #조건문 연습 2단계
# 4번
# N = int(input("수입력: "))

# #1번
# if N >= 0 :
#     print("절대값은 {} 입니다.".format(N))
# elif N < 0:
#     print("절대값은 {} 입니다.".format(-N))
# else:
#     print("입력이 바르지 않습니다.")

# #2번
# print(abs(N))

# #5번
# 사과 = int(input("사과개수를 입력해주세요: "))
# 배 = int(input("배 개수를 입력해주세요: "))
# 현금 = int(input("소지하신 금액을 입력해주세요: "))
# 총금액 = 사과 * 3000 + 배 * 2000

# # 현금 - 총금액이 0보다 클경우
# if 현금 - 총금액 >= 0:
#     print("현재 보유 금액: {:,}원\n총 금액: {:,}원\n결재후 잔액: {:,}원".\
# format(현금,총금액,현금-총금액))
# else:
#     print("구매불가\n{:,}원이 더 필요합니다.".format(-(현금-총금액)))

# # 현금이 총금액보다 같거나 클경우
# if 현금 >= 총금액:
#     print("잔액:{:,}원".format(현금-총금액))
# else:
#     print("구매불가\n필요한 금액:{:,}원".format(총금액-현금))

# #문제6
# A = int(input("수입력: "))
# if A % 15 == 0:
#     print("{}은 15의 배수입니다.".format(A))
# elif A % 3 == 0:
#     print("{}은 3의 배수입니다.".format(A))
# elif A % 5 == 0:
#     print("{}은 5의 배수입니다.".format(A))
# else:
#     print("해당없음X")

# 2:02까지


# #문제7
# A = int(input("세자리 수 입력: "))
# B = int(input("세자리 수 입력: "))

# r_A = A%10*100 + A//10%10*10 + A//100 
# r_B = B%10*100 + B//10%10*10 + B//100

# print(r_A)
# print(r_B)

# if r_A > r_B:
#     print("뒤집었을때 큰수는 {}".format(A))
# elif r_A < r_B:
#     print("뒤집었을때 큰수는 {}".format(B))
# else:
#     print("두수는 같습니다.")

# #문제8 
# N = int(input("몇일? "))
# print("{}일 당번은....".format(N))
# if N % 4 == 1:
#     print("A가 당번입니다.")
# elif N % 4 == 2:
#     print("B가 당번입니다.")
# elif N % 4 == 3:
#     print("C가 당번입니다.")
# else:
#     print("D가 당번입니다.")

# #문제9
# N = int(input("N일 후 요일은? "))
# if N % 7 == 1:
#     print("{}일후는 수요일".format(N))
# elif N % 7 == 2:
#     print("{}일후는 목요일".format(N))
# elif N % 7 == 3:
#     print("{}일후는 금요일".format(N))
# elif N % 7 == 4:
#     print("{}일후는 토요일".format(N))
# elif N % 7 == 5:
#     print("{}일후는 일요일".format(N))
# elif N % 7 == 6:
#     print("{}일후는 월요일".format(N))
# else:
#     print("{}일후는 화요일".format(N))


#문제 11번 => 0시 20분 입력시
# 11:50분 출력

# 56

# # 문제 10
# 시간 = int(input("시간을 입력해주세요: ")) 
# 분 = int(input("분을 입력해주세요: "))

# 총분 = (시간*60) + 분

# 현재시간 = (총분 + 30)//60 
# 현재분 =  (총분 + 30)%60

# print("현재시간의 30분 후는 {}시 {}분 입니다".format(현재시간,현재분))


# # 문제 11
# 시간 = int(input("시간을 입력해주세요: ")) 
# 분 = int(input("분을 입력해주세요: "))

# 총분 = (시간*60) + 분 -30

# if 총분 < 0:
#     총분 = 총분 + 1440

# 현재시간 = 총분 //60 
# 현재분 =  총분 %60

# print("현재시간의 30분 전은 {}시 {}분 입니다".format(현재시간,현재분))

#문제12
print("="*30)
print("1.아메리카노")
print("2.카페라떼")
print("3.우유")
print("="*30)
메뉴 = input("메뉴선택: ")
if 메뉴 == "1":
    a = "아메리카노"
elif 메뉴 == "2":
    a = "카페라떼"
elif 메뉴 == "3":
    a = "우유"
print("="*30)
print("1.ICE")
print("2.HOT")
print("="*30)
온도 = input("온도선택: ")
if 온도 == "1":
    b = "아이스"
elif 온도 == "2":
    b = "핫"
print("선택하신 음료는 {} {} 입니다.".format(b,a))
