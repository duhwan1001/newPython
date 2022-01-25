import time
import os

currentMoney = 0
inputMoney = 0
change = 0
while True:
    print()
    print("--- Menu ---")
    print("1. 콜라 / 300")
    print("2. 사이다 / 300")
    print("3. 커피 / 200")
    print("4. 돈 넣기")
    print("5. 잔돈 반환")
    print("6. 종료")
    print("------------")
    print("현재 금액 : {:,}".format(currentMoney))
    sel = int(input("메뉴 선택 : "))
    print()
    time.sleep(0.7)
    os.system("cls")
               
    if sel == 1:
        if currentMoney > 300:
            currentMoney -= 300
            print("콜라 맛있게 드세요 !")
        else:
            print("투입 금액이 부족합니다.")
    elif sel == 2:
        if currentMoney > 300:
            currentMoney -= 300
            print("사이다 맛있게 드세요 !")
        else:
            print("투입 금액이 부족합니다.")
    elif sel == 3:
        if currentMoney > 300:
            currentMoney -= 200
            print("커피 맛있게 드세요 !")
        else:
            print("투입 금액이 부족합니다.")
    elif sel == 4:
        inputMoney = int(input("돈 넣기\n투입 금액을 입력해주세요."))
        currentMoney += inputMoney
        print("{:,}원이 충전되었습니다.".format(inputMoney))
    elif sel == 5:
        print("잔돈을 반환합니다.")
        change += currentMoney
        currentMoney = 0
    elif sel == 6:
        print("자판기 프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다 1 ~ 6 사이의 숫자를 입력해주세요.")