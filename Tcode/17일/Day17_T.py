# #활용 ) 빈 딕셔너리에 요소 추가

# #1. 선언
# dict_d = {}

# #2. 요소 추가전 출력
# print("요소 추가전 출력: {}".format(dict_d))

# #3. 요소 추가 (이름,키,몸무게)
# dict_d["이름"] = "어피치"
# dict_d["키"] = 190
# dict_d["몸무게"] = 90

# #4. 요소 추가 후 출력
# print("요소 추가 후 출력: {}".format(dict_d))

# #활용) 딕셔너리에 요소 제거
# #1. 선언
# dict_e = {
#     "이름":"라이언",
#     "본적":"나주 라씨",
#     "반려묘":"춘식이"
# }
# #2.요소 제거전 출력
# print("요소 제거전 출력: {}".format(dict_e))

# #3.요소 제거 (이름, 본적)
# del dict_e["이름"]
# del dict_e["본적"]

# #4. 요소 제거후 출력
# print("요소 제거전 출력: {}".format(dict_e))

# # 존재하지 않는 키에 접근
# dict_e = {}
# print(dict_e["본적"])
# # KeyError: '본적'

# 딕셔너리 함수
# #update() : 사전형 자료에 값을 추가
# #1. 선언
# dict_f = {1:"a",2:"b",3:"c"}

# #2. 키 - 값추가
# dict_f.update({4:"d"})

# #3. 확인
# print(dict_f)


# #get() 사전형의 값을 반환
# dict_f = {1:"a",2:"b",3:"c"}

# print(dict_f.get(1))
# print(dict_f.get(3))
# print(dict_f.get(9))

# # keys()  사전형의 모든 키를 반환
# dict_f = {1:"a",2:"b",3:"c"}
# print(dict_f.keys())

# for i in dict_f.keys():
#     print(i)

# #values() 사전형의 모든 값 반환
# print(dict_f.values())

# for i in dict_f.values():
#     print(i)

# #items() 사전형의 모든 키 - 값 쌍으로 튜플로 반환
# print(dict_f.items())

# for key,value in dict_f.items():
#     print(key,"\t",value)

# #clear() 모든 키-값을 삭제해서 빈 사전형 자료만 남기
# dict_f = {1:"a",2:"b",3:"c"}
# dict_f.clear()
# print(dict_f)

#딕셔너리 종합 문제1
카카오톡식구 = {}

# # 기본
# for i in range(5):
#     k = input("이름(key)입력: ")
#     v = input("값(value)입력: ")
#     카카오톡식구[k] = v

# print(카카오톡식구)

# #응용
# for i in range(5):
#     k = input("이름(key)입력: ")
#     v = input("값(value)입력: ")
#     카카오톡식구.update({k:v})

# print(카카오톡식구)
# #딕셔너리 정리하기 문제2

# 재고 = {"커피":7,"펜":3,"종이컵":9,"콜라":20,"사이다":9}

# 입력 = input("물건의 이름을 입력하시오: ")
# print("{}의 현재 수량은 {}개 입니다.".format(입력,재고[입력]))

# print("{}의 현재 수량은 {}개 입니다.".format(입력,재고.get(입력)))

# #딕셔너리 정리하기 문제3

# 재고 = {"커피":7,"펜":3,"종이컵":9,"콜라":20,"사이다":9}

# 입력 = input("물건의 이름을 입력해주세요: ")
# if 재고.get(입력) == None:
#     재고[입력] = int(input("수량을 입력하세요: "))
#     print("현재 재고: {}".format(재고) )
# else:
#     print("{}의 현재 수량은 {}개 입니다.".format(입력,재고.get(입력)))

# 창고물품 = {"커피" : 7,"펜" : 3,"종이컵" : 9,"콜라" : 20,"사이다" : 9}

# 물건 = input("물건을 입력하세요: ")
# if 물건 not in 창고물품:
#     추가물건 = input("존재하지 않는 물건입니다. \n추가할 물건의 이름을 입력해주세요: ")
#     재고 = input("해당 물건의 재고를 입력해주세요: ")
#     창고물품.update({추가물건:재고})
#     print(창고물품)
# else:
#     print("{}의 재고는 {}입니다.".format(물건,창고물품[물건]))


# # 딕셔너리 정리하기 문제4
# 책 = {}
# n = int(input("등록할 책의 개수를 입력하세요: "))
# for i in range(1,n+1):
#     입력 = input("책의 등록번호를 입력하시오: ")
#     책[입력] = input("책이름을 적어주세요: ")
# print(책)
# for i in range(1,n+1):
#     책등록번호 = input("책의 등록번호를 입력하시오: ")
#     책이름 =  input("책이름을 적어주세요: ")
#     책.update({책등록번호:책이름})
# print(책)

# 실습
#1. 기획 
# 메뉴등록/메뉴별 가격/메뉴 가격수정/종료
# #2. 구성
# while True:
#     print("-"*25)
#     print("1. 메뉴 등록")
#     print("2. 메뉴별 가격")
#     print("3. 메뉴 가격 수정")
#     print("4. 종료")
#     print("-"*25)
#     num = int(input("번호 입력: "))
#     if num == 1:
#         pass
#     elif num == 2:
#         pass
#     elif num == 3:
#         pass
#     elif num == 4:
#         pass
#     else:
#         print("번호를 다시 입력해주세요.")

#3.실행
#2. 구성
menu = {}
while True:
    print("-"*25)
    print("1. 메뉴 등록")
    print("2. 메뉴별 가격")
    print("3. 메뉴 가격 수정")
    print("4. 종료")
    print("-"*25)
    num = int(input("번호 입력: "))
    if num == 1:
        name = input("메뉴입력: ")
        if menu.get(name) == None:
            menu[name] = input("가격: ")
        else:
            print("입력하신 메뉴는 존재 합니다.") 
    elif num == 2:
        for k,v in menu.items():
            print("메뉴: {}  가격: {}".format(k,v))
    elif num == 3:
        name = input("수정할 메뉴 이름: ")
        if menu.get(name) == None:
            print("입력하신 메뉴는 존재하지 않습니다.")
        else:
            menu[name] = input("메뉴 가격: ")
    elif num == 4:
        print("종료 합니다.")
        break
    else:
        print("번호를 다시 입력해주세요.")
