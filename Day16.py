# A = ["red", "green", "yellow", "apple", "is","delicious"]
# print(A[:3])
# print(A[0], A[3], A[4], A[5])

# a = [1,2,3,4]
# sum = a[0] + a[1] + a[2] + a[3]
# print(sum)

# list_a = ["A","B","C"]

# print("#append사용해서 뒤에 요소 추가")
# list_a.append("D")
# list_a.append("E")
# print(list_a)

# list_a.insert(0, "추가")
# print(list_a)

# list_a.extend(["F","G","H"])
# print(list_a)

# list_a = ['추가', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# # del
# del list_a[0]
# print(list_a)

# # pop
# list_a.pop()
# print(list_a)

# list_b = [1,2,3,1,2,3,1,2,3]

# for i in range(3):
#     list_b.remove(3)
# print(list_b)

# list_c = [1,2,3,4,5]
# list_c.clear()
# print(list_c)

# a = [200, 101, 5, 32, 64, 0 ,72, 900, 99]
# # 100이상이며, 짝수 홀수를 구분한 수를 출력
# for i in range(len(a)):
#     if a[i] > 100 and a[i] % 2 == 0:
#         print("100이상의 짝수 : {}".format(a[i]))
#     if a[i] > 100 and a[i] % 2 == 1:
#         print("100이상의 홀수 : {}".format(a[i]))

# a = [200, 101, 5, 32, 64, 0 ,72, 900, 99]
# # 자리수 계산
# for i in range(len(a)):
#     print("a[{}]의 자릿수는 : {} 입니다.".format(i, len(str(a[i]))))

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# b = [[],[],[]]

# for i in a:
#     b[(i+2)%3].append(i)
# print(b)

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# b = [[],[],[],[]]

# for i in a:
#     b[(i+3)%4].append(i)
# print(b)

dict_a = {"name" : "두", "age" : 24}
print(dict_a)

print(dict_a["name"])