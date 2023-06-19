import math
for i in range(1, 101):
    flag = True
    if i > 1 and (i == 2 or i == 3):
        print(i)
        flag = False
        continue
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
    if flag:
        print(i)
