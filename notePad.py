sum1 = 0
for i in range(1, 101, 1):
    print(i)
    if i % 3 == 0:
        if i % 5 == 0:
            sum1 += i
    print("합 : {}".format(sum1))