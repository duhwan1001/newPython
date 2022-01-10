# 문자열 출력
print("파이썬")
print('Python')

# 숫자 출력
print(1)
print(2)

# 줄 바꿈
print()

# 숫자 연산 결과
print(1 + 10)

# 하나만 출력하기
print("HI")

# 여러개 출력하기
print("HI", 1, 'welcome')

print("10 더하기 20은", 10+20)
print("10 곱하기 20은", 10*20)

print("======================")
print("======================")
print("==", "name : Du Hwan KIM", "==")
print("==", "call : 010 1234 5678", "==")
print("==", "email : kdhz2012@gmail.com", "==")
print("==", "address : Du Hwan KIM", "==")
print("======================")
print("======================")

print("Uncle's present")
print('Uncle\'s present')

# 이스케이프 문자

#1. \n
print("다음 라인으로\n이동")
#2. \t
print("Tab은\t공백")
#3. \', \", \\
print("\', \", \\ 문자 사용하는 방법")

#end 옵션
print("welcome to")
print("IT news")
print("web site")

# 한 줄 주석 (맨 앞에 #)

# 여러 줄 주석 (''',""" 열고 닫기)
'''
MULTI 
LINE
주석
'''

#꿀팁

# print("welcome to")
# print("IT news")
# print("web site")

'''print("welcome to")
print("IT news")
print("web site")'''

# ctrl + s = 저장
# ctrl + z = 이전으로 돌아가기
# ctrl + / = 한줄 주석
# ctrl + F5 = 터미널 실행

print("\t#### 회비 정보 ####")
print("=" * 40)
print("이름\t나이\t전화번호\t회비")
print("=" * 40)
print("김두환\t24\t010-1111-1111\t\\35,000")
print("김두환\t24\t010-1111-1111\t\\35,000")
print("김두환\t24\t010-1111-1111\t\\30,000")
print("-" * 40)
print("총합계\t\t\t\t\\100,000")
print("=" * 40)

# 서식 문자
#1.단일 문자
print("%c" %("안")) #C
print("{}".format("녕")) #Python

#2.문자열 및 정수 출력
print("%s의 나이는 %d살 입니다." %("두", 20)) #C
print("{}의 나이는 {}살 입니다.".format("두", 20)) #Python