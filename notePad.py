h, m = map(int,input().split(" "))
tot = (h * 60) + m
tot = tot - 45
if tot < 0:
    tot += 1440
h = tot // 60
m = tot % 60
print(h, m)