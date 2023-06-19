import random as rd
nums = int(input("要扔多少次非标:"))
Fcnt = 0
for i in range(nums):
    x = rd.uniform(-1, 1)
    y = rd.uniform(-1, 1)
    if x * x + y * y <= 1:
        Fcnt += 1
print("中标数：", Fcnt)
print("π的近似值为：", Fcnt / nums * 4)
