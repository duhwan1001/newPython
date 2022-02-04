# #활용 ) 빈 딕셔너리에 요소 추가

# #1. 선언
# dict_d = {}

# #2. 요소 추가전 출력
# print(dict_d)

# #3. 요소 추가
# dict_d['이름'] = "name"
# dict_d['키'] = "999cm"
# dict_d['몸무게'] = "999kg"

# #4. 요소 추가 후 출력
# print(dict_d)

# #1. 선언
# dict_e = {
#     "이름" : "라이언",
#     "본적" : "나주 라씨",
#     "반려묘" : "춘식이"
# }

# #2. 요소 제거전 출력
# print(dict_e)

# #3. 요소 제거(이름, 본적)
# del(dict_e["이름"])
# dict_e.pop("본적")

# #4. 요소 제거 후 출력
# print(dict_e)

# dictionary 함수
# update() : 사전형 자료에 값을 추가
# # 1. 선언
# dict_f = {1:"a", 2:"b", 3:"c"}

# #2. 키 - 값 추가
# dict_f.update({4:"d"})

# #3. 확인
# print(dict_f)

# get() : 사전형의 값을 반환
# dict_f = {1:"a", 2:"b", 3:"c"}

# print(dict_f.get(1))
# print(dict_f.get(3))
# print(dict_f.get(9))

# keys() : 사전형의 모든 키를 반환
# dict_f = {1:"a", 2:"b", 3:"c"}

# print(dict_f.keys())

# for i in dict_f.keys():
#     print(i)
# # values() : 사전형의 모든 값 반환
# print(dict_f.values())

# for i in dict_f.values():
#     print(i)

# # items() : 사전형의 모든 키 - 값 쌍으로 튜플로 반환
# print(dict_f.items())

# for key, value in dict_f.items():
#     print(key,"\t", value) # i[0]

# clear() : 모든 키 - 값을 삭제해서 빈 사전형 자료만 남겨놓는다
# dict_f = {1:"a", 2:"b", 3:"c"}
# dict_f.clear()
# print(dict_f)

# dict_q = {}
# while True:

#     print("입력을 종료하려면 exit를 입력하세요")

#     a = input("key >> \n")
#     b = input("value >> \n")
#     if a == "exit" or b == "exit":
#         break
#     dict_q.update({a : b})
#     print(dict_q)

# product = {"선반" : 11, "침대" : 13, "책상" : 7}
# # print("현재 보유중인 물품")
# # for i in product.keys():
# #     print(i , "\t")
# # findProduct = input()
# # print(product.get(findProduct), "개 보유중")
# findProduct = input()
# if product.get(findProduct) == None:
#     product[findProduct] = int(input("수량 입력"))
#     print("현재 재고 : {}".format(product))
# else:
#     print(product.get(findProduct), "개 보유중")

# 딕셔너리 정리하기 문제4
# 책 = {}
# n = int(input("등록할 책의 개수를 입력하세요 : "))
# for i in range(1, n+1):
#     입력 = input("책의 등록번호를 입력하시오 : ")
#     책[입력] = input("책이름을 적어주세요 : ")
# print(책)
# for i in range(1, n+1):
#     책등록번호 = input("책의 등록번호를 입력하시오 : ")
#     책이름 = input("책이름을 적어주세요 : ")
#     책.update({책등록번호:책이름})
# print(책)

import os

menu = {}

while True:
    print("메뉴 등록 프로그램")
    print("-" * 10)
    print("1. 메뉴 등록")
    print("2. 메뉴별 가격")
    print("3. 메뉴 가격 수정")
    print("4. 종료")
    print("-" * 10)
    sel = int(input("메뉴를 선택하세요 >> "))
    if sel == 1:
        os.system("cls")
        print("메뉴 등록") 
        name = input("등록할 메뉴 이름을 입력하세요 >> ")
        price = input("메뉴의 가격을 입력하세요 >> ")
        menu.update({name : price})
    elif sel == 2:
        os.system("cls")
        print("메뉴별 가격")
        print("메뉴\t가격")
        for name, price in menu.items():
            print("{}\t{:,}원".format(name,int(price)))
    elif sel == 3:
        os.system("cls")
        print("메뉴 가격 수정")
        print("등록 되어있는 메뉴 :")
        for i in menu.keys():
            print(i, end=" ")
        name = input("수정할 메뉴를 입력하세요 >>")
        price = input("수정할 가격을 입력하세요 >> ")
        menu[name] = price
    elif sel == 4:
        print("종료합니다.")
        break