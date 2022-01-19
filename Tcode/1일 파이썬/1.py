# # 문자열 출력
# print("파이썬")
# print('Python')

# #숫자 출력
# print(1)

# #줄바꿈
# print()

# #숫자연산결과
# print(1+10)

# #하나만 출력하기
# print("HI")
# #여러개 출력하기 (,컴마)
# print("HI",100,'BYE')

# #예제1
# print("10더하기 20은",10+20)
# print("10곱하기 20은",10*20)

# print("==========================")
# print("============name:khl======")
# print("============call:010======")
# print("============address:서울==")
# print("============email:apeach==")
# print("==========================")
# # SyntaxError: EOL while scanning string literal
# # SyntaxError: unexpected EOF while parsing
# # IndentationError: unexpected indent

# #예제3
# print("Uncle's present")
# #예제4
# print('Uncle\'s present')

# # 이스케이프 문자

# #1.\n
# print("다음 라인으로\n이동")
# #2.\t
# print("Tab은\t공백")
# #3.\',\",\\
# print("\',\",\\문자 사용하는 방법")

# #end 옵션

# print("welcome to",end=" ")
# print("IT news",end=" ")
# print("web site")

# # 한 줄 주석 (맨 앞에 #)

# # 여러 줄 주석 (''',"""  열고 닫기)
# '''
# MULTI
# LINE
# 주석
# '''

# #꿀팁

# print("welcome to",end=" ")
# print("IT news",end=" ")
# print("web site",end=" ")

'''print("welcome to",end=" ")
print("IT news",end=" ")
print("web site",end=" ")'''

# ctrl + s 저장
# ctrl + z 이전으로 돌아가기
# ctrl + / 한줄 주석
# ctrl + F5 터미널 실행

# # 실습
# print("\t #### 회비정보 ####")
# print("="*40)
# print("이름\t나이\t전화번호\t회비")
# print("="*40)
# print("김동완\t38\t010-1111-1111\t\\20,000")
# print("서지수\t24\t010-1234-5678\t\\30,000")
# print("이지은\t25\t010-2525-2345\t\\50,000")
# print("----------------------------------------")
# print("총합계\t\t\t\t\\100,000")
# print("="*40)

# 서식문자
#1. 단일 문자
print("%c" %("안"))
print("{}".format("녕"))

#2.문자열 및 정수 출력
print("%s %d" %("펭수",20))
print("{} {}".format("펭수",20))

#2.문자열 및 정수 출력
print("%s님의 나이는 %d살 입니다." %("펭수",20))
print("{}님의 나이는 {}살 입니다.".format("펭수",20))







